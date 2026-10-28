"""Orchestration : chaque événement extérieur (nouvelle demande, SMS reçu, devis
envoyé, horloge) passe par ici. Toutes les règles de contact sont centralisées
dans `_can_send` pour qu'aucun chemin ne les contourne.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Callable

from . import consent
from .fiche import build_fiche, export_json, render_text
from .models import Company, Lead, LeadState, QuoteStatus
from .phones import to_e164
from .providers import ConsoleMailer, ConsoleSms, ConsoleVoice, Mailer, SmsProvider, VoiceProvider
from .qualifier import Qualifier, ScriptedQualifier
from .store import Store

RELANCES_JOURS = (3, 10, 20)

RELANCE_TEXTES = {
    1: "Bonjour {prenom}, ici l'assistant IA de {nom}. Avez-vous pu regarder le devis ? "
       "Si une question vous retient, répondez ici et {dirigeant} vous rappelle.",
    2: "Bonjour {prenom}, {nom} revient vers vous pour le devis. Qu'est-ce qui vous fait hésiter : "
       "le prix, le délai, le financement, autre chose ? Une réponse en un mot suffit.",
    3: "Bonjour {prenom}, dernier message de {nom} au sujet du devis. Si le projet est toujours d'actualité, "
       "{dirigeant} se tient à votre disposition. STOP pour ne plus recevoir de messages.",
}

HESITATIONS = {
    "prix": ("prix", "cher", "budget", "tarif", "moins cher"),
    "delai": ("delai", "délai", "date", "trop tard", "attendre", "pas pressé"),
    "financement": ("pret", "prêt", "banque", "financement", "aide", "maprimerenov"),
    "concurrent": ("autre entreprise", "concurrent", "autre devis", "comparer", "compare"),
}


@dataclass
class Engine:
    store: Store
    qualifier: Qualifier = field(default_factory=ScriptedQualifier)
    sms: SmsProvider = field(default_factory=ConsoleSms)
    voice: VoiceProvider = field(default_factory=ConsoleVoice)
    mailer: Mailer = field(default_factory=ConsoleMailer)
    clock: Callable[[], datetime] = datetime.now
    # Répliques à dire pendant un appel en cours (lead_id → textes), lues par le webhook voix.
    _calls: dict[str, list[str]] = field(default_factory=dict, init=False, repr=False)

    # ------------------------------------------------------------------ règles
    def _in_hours(self, company: Company, now: datetime) -> bool:
        start, end = company.heures_contact
        return now.weekday() < 6 and start <= now.time() <= end  # lundi → samedi

    def _can_send(self, lead: Lead, kind: str, now: datetime) -> bool:
        """kind : "reponse" (réponse immédiate à une demande ou à un message du client),
        "appel", ou "relance" (message que le client n'a pas sollicité à cet instant)."""
        if self.store.is_opted_out(lead.telephone):
            return False
        if kind == "reponse":
            return True
        company = self.store.get_company(lead.company_id)
        return self._in_hours(company, now)

    def _send(self, lead: Lead, text: str, kind: str = "reponse") -> bool:
        now = self.clock()
        if not self._can_send(lead, kind, now):
            self.store.log_event(lead.id, "envoi_bloque", f"{kind}: {text[:60]}", now)
            return False
        if lead.id in self._calls:  # appel en cours : la réplique est dite, pas envoyée par SMS
            self._calls[lead.id].append(text)
        else:
            self.sms.send(lead.telephone, text)
        self.store.log_message(lead.id, "out", text, now)
        return True

    # -------------------------------------------------------- nouvelle demande
    def new_lead(self, company_id: str, telephone: str, prenom: str = "", source: str = "site",
                 message: str = "", recommande: bool = False) -> Lead:
        now = self.clock()
        telephone = to_e164(telephone)
        company = self.store.get_company(company_id)
        lead = Lead(
            id=uuid.uuid4().hex[:10], company_id=company_id, telephone=telephone, prenom=prenom,
            source=source, message_initial=message, recommande=recommande, created_at=now.isoformat(),
        )
        self.store.save_lead(lead)
        self.store.log_event(lead.id, "demande_recue", source, now)
        if self.store.is_opted_out(telephone):
            lead.state = LeadState.OPTED_OUT
            self.store.save_lead(lead)
            self.store.log_event(lead.id, "ignore_stop", "numéro en opposition", now)
            return lead
        if recommande and company.jamais_contacter_recommandes:
            text = consent.consent_request_recommended(company, lead)
        else:
            text = consent.consent_request(company, lead)
        if self._send(lead, text):
            self.store.record_consent(lead, "demande_envoyee", text, now)
            self.store.log_event(lead.id, "premier_contact", "", now)
        return lead

    # --------------------------------------------------------------- SMS reçu
    def inbound_sms(self, telephone: str, text: str) -> None:
        now = self.clock()
        telephone = to_e164(telephone)
        lead = self.store.latest_lead_for_phone(telephone)
        if lead is None:
            self.store.log_event(None, "sms_inconnu", telephone, now)
            return
        self.store.log_message(lead.id, "in", text, now)
        company = self.store.get_company(lead.company_id)

        if consent.is_stop(text):
            self.store.opt_out(telephone, now)
            self.store.record_consent(lead, "stop", text, now)
            self.store.cancel_followups_for_phone(telephone)
            lead.state = LeadState.OPTED_OUT
            self.store.save_lead(lead)
            # Dernier message de confirmation, envoyé avant que l'opposition ne bloque tout.
            self.sms.send(telephone, consent.confirm_stop(company))
            self.store.log_message(lead.id, "out", consent.confirm_stop(company), now)
            return

        if lead.state is LeadState.OPTED_OUT:
            return

        open_quote = self.store.open_quote_for_lead(lead.id)
        if open_quote is not None:
            self._quote_reply(lead, company, open_quote, text)
            return

        if lead.state in (LeadState.AWAITING_CONSENT, LeadState.LATER):
            self._consent_reply(lead, company, text)
        elif lead.state is LeadState.QUALIFYING:
            self._qualify(lead, company)
        else:
            # Fiche déjà envoyée ou transfert en cours : on transmet au dirigeant.
            self._notify_owner(company, lead, f"Nouveau message de {lead.prenom or lead.telephone} : {text}")

    def _consent_reply(self, lead: Lead, company: Company, text: str) -> None:
        now = self.clock()
        choice = consent.parse_choice(text)
        if lead.recommande and company.jamais_contacter_recommandes and choice == "appel":
            choice = "plus_tard"  # pas d'appel IA pour un contact recommandé
        if choice is None:
            if lead.state is LeadState.LATER:
                lead.creneau_prefere = text.strip()
                self.store.save_lead(lead)
                self._handoff(lead, company, f"créneau demandé : {text.strip()}")
                return
            self._send(lead, "Pardon, je n'ai pas compris. Répondez 1 (appel maintenant), "
                             "2 (plus tard) ou 3 (par écrit ici).")
            return
        if choice == "appel":
            self.store.record_consent(lead, "accord_appel", text, now)
            lead.canal = "appel"
            if self._can_send(lead, "appel", now):
                lead.state = LeadState.QUALIFYING
                self.store.save_lead(lead)
                self.voice.start_call(lead.telephone, lead.id)
                self.store.log_event(lead.id, "appel_lance", "", now)
                if getattr(self.voice, "live", False):
                    self._send(lead, "Parfait, je vous appelle tout de suite.")
                    return  # la suite se passe dans call_answered / call_speech
                self._qualify(lead, company)  # sans opérateur voix : appel simulé par écrit
            else:
                lead.state = LeadState.QUALIFYING
                lead.canal = "ecrit"
                self.store.save_lead(lead)
                self._send(lead, "Il est un peu tard pour vous appeler. On peut avancer par écrit dès "
                                 "maintenant, ou on vous appelle demain matin. ")
                self._qualify(lead, company)
        elif choice == "ecrit":
            self.store.record_consent(lead, "accord_ecrit", text, now)
            lead.canal = "ecrit"
            lead.state = LeadState.QUALIFYING
            self.store.save_lead(lead)
            self._qualify(lead, company)
        else:  # plus tard
            self.store.record_consent(lead, "plus_tard", text, now)
            lead.state = LeadState.LATER
            self.store.save_lead(lead)
            if consent.normalize(text) in ("2", "2."):
                self._send(lead, "Entendu. Quand préférez-vous être rappelé (jour et heure) ?")
            else:
                lead.creneau_prefere = text.strip()
                self.store.save_lead(lead)
                self._handoff(lead, company, f"créneau demandé : {text.strip()}")

    def _qualify(self, lead: Lead, company: Company) -> None:
        now = self.clock()
        history = [(r["direction"], r["texte"]) for r in self.store.history(lead.id)]
        turn = self.qualifier.next_turn(company, lead, history)
        lead.fields.update({k: v for k, v in turn.fields.items() if v})
        if turn.asked_price:
            self.store.log_event(lead.id, "question_prix", "", now)
        self.store.save_lead(lead)
        self._send(lead, turn.reply)
        if turn.wants_human:
            self._handoff(lead, company, "le client demande à parler à quelqu'un", reply_sent=True)
        elif turn.done:
            self._deliver_fiche(lead, company)

    def _deliver_fiche(self, lead: Lead, company: Company) -> None:
        now = self.clock()
        fiche = build_fiche(company, lead)
        self.store.save_fiche(fiche, now)
        lead.state = LeadState.QUALIFIED
        self.store.save_lead(lead)
        body = render_text(company, lead, fiche) + "\n\n--- export logiciel de devis ---\n" + export_json(lead, fiche)
        self.mailer.send(company.email_fiches, f"[{fiche.classement.value}] Nouveau projet — {lead.prenom or lead.telephone}", body)
        self.store.log_event(lead.id, "fiche_envoyee", fiche.classement.value, now)
        if fiche.classement.value == "à visiter":
            self._notify_owner(company, lead, f"Projet à visiter : {fiche.resume[:200]}")

    def _handoff(self, lead: Lead, company: Company, raison: str, reply_sent: bool = False) -> None:
        now = self.clock()
        lead.state = LeadState.HANDED_OFF
        self.store.save_lead(lead)
        if not reply_sent:
            self._send(lead, f"C'est noté. {company.dirigeant} vous rappelle"
                             + (f" ({lead.creneau_prefere})." if lead.creneau_prefere else " dans l'heure en journée."))
        fiche = build_fiche(company, lead)
        self.store.save_fiche(fiche, now)
        self._notify_owner(company, lead, f"À rappeler ({raison}). {fiche.resume[:160]}")
        self.store.log_event(lead.id, "transfert_humain", raison, now)

    def _notify_owner(self, company: Company, lead: Lead, text: str) -> None:
        if company.tel_dirigeant:
            self.sms.send(company.tel_dirigeant, f"[Archibald] {lead.prenom or lead.telephone} — {text}")
        self.store.log_event(lead.id, "alerte_dirigeant", text[:80], self.clock())

    # ------------------------------------------------------------ appel en direct
    def call_answered(self, lead_id: str) -> list[str]:
        """Le client décroche : présentation (l'IA se déclare), puis première question."""
        lead = self.store.get_lead(lead_id)
        company = self.store.get_company(lead.company_id)
        self._calls[lead_id] = []
        if lead.state is not LeadState.QUALIFYING:
            self._calls.pop(lead_id)
            return []
        bonjour = f"Bonjour {lead.prenom}" if lead.prenom else "Bonjour"
        self._send(lead, f"{bonjour}, ici l'assistant IA de {company.nom}, suite à votre demande de devis. "
                         "J'ai quelques questions pour préparer la visite.")
        self._qualify(lead, company)
        said = self._drain(lead_id) or []
        if self.store.get_lead(lead_id).state is not LeadState.QUALIFYING:
            self._calls.pop(lead_id, None)
        return said

    def call_speech(self, lead_id: str, text: str) -> tuple[list[str], bool]:
        """Une réponse dite au téléphone. Retourne (répliques à dire, raccrocher ?)."""
        now = self.clock()
        lead = self.store.get_lead(lead_id)
        company = self.store.get_company(lead.company_id)
        self._calls.setdefault(lead_id, [])
        self.store.log_message(lead.id, "in", text, now)
        if consent.is_stop(text):
            self.store.opt_out(lead.telephone, now)
            self.store.record_consent(lead, "stop", text, now)
            self.store.cancel_followups_for_phone(lead.telephone)
            lead.state = LeadState.OPTED_OUT
            self.store.save_lead(lead)
            self._calls.pop(lead_id, None)
            return [f"C'est noté, {company.nom} ne vous recontactera plus. Au revoir."], True
        if lead.state is LeadState.QUALIFYING:
            self._qualify(lead, company)
        said = self._drain(lead_id) or []
        ended = self.store.get_lead(lead_id).state is not LeadState.QUALIFYING
        if ended:
            self._calls.pop(lead_id, None)
        return said, ended

    def call_ended(self, lead_id: str, status: str = "completed") -> None:
        """Fin d'appel (raccroché, pas de réponse…) : si le projet n'est pas complet, on continue par SMS."""
        self._calls.pop(lead_id, None)
        lead = self.store.get_lead(lead_id)
        if lead.state is not LeadState.QUALIFYING or lead.canal != "appel":
            return
        lead.canal = "ecrit"
        self.store.save_lead(lead)
        self.store.log_event(lead.id, "appel_interrompu", status, self.clock())
        self._send(lead, "Nous n'avons pas pu terminer l'appel. On peut continuer par écrit, ici.")
        self._qualify(lead, self.store.get_company(lead.company_id))

    def _drain(self, lead_id: str) -> list[str] | None:
        if lead_id not in self._calls:
            return None
        said, self._calls[lead_id] = self._calls[lead_id], []
        return said

    # ---------------------------------------------------------- devis et relances
    def quote_sent(self, lead_id: str, montant: int | None = None, quote_id: str | None = None) -> str:
        now = self.clock()
        quote_id = quote_id or uuid.uuid4().hex[:10]
        self.store.save_quote(quote_id, lead_id, montant, now)
        for rang, jours in enumerate(RELANCES_JOURS, start=1):
            self.store.add_followup(quote_id, now + timedelta(days=jours), rang)
        self.store.log_event(lead_id, "devis_envoye", quote_id, now)
        return quote_id

    def quote_status(self, quote_id: str, status: QuoteStatus) -> None:
        now = self.clock()
        q = self.store.get_quote(quote_id)
        self.store.set_quote_status(quote_id, status)
        self.store.log_event(q["lead_id"], f"devis_{status.name.lower()}", quote_id, now)

    def tick(self) -> int:
        """À appeler régulièrement (cron) : envoie les relances dues, dans les heures permises."""
        now = self.clock()
        sent = 0
        for f in self.store.due_followups(now):
            q = self.store.get_quote(f["quote_id"])
            if q["status"] != QuoteStatus.ENVOYE.value:
                self.store.mark_followup(f["id"], "annule")
                continue
            lead = self.store.get_lead(q["lead_id"])
            company = self.store.get_company(lead.company_id)
            if self.store.is_opted_out(lead.telephone):
                self.store.mark_followup(f["id"], "annule")
                continue
            if not self._in_hours(company, now):
                continue  # reste en file, partira au prochain passage dans les heures permises
            text = RELANCE_TEXTES[f["rang"]].format(
                prenom=lead.prenom or "", nom=company.nom, dirigeant=company.dirigeant
            ).replace("Bonjour ,", "Bonjour,")
            if self._send(lead, text, kind="relance"):
                self.store.mark_followup(f["id"], "envoye")
                self.store.log_event(lead.id, "relance_envoyee", f"J+{RELANCES_JOURS[f['rang'] - 1]}", now)
                sent += 1
        return sent

    def _quote_reply(self, lead: Lead, company: Company, quote, text: str) -> None:
        t = consent.normalize(text)
        if any(w in t for w in ("signe", "on y va", "c'est bon", "valide", "j'accepte", "ok pour le devis")):
            self._send(lead, f"Excellente nouvelle ! {company.dirigeant} vous recontacte pour la suite.")
            self._notify_owner(company, lead, f"Le client semble accepter le devis : « {text} »")
            return
        raison = next((r for r, mots in HESITATIONS.items() if any(consent.normalize(m) in t for m in mots)), "autre")
        self.store.set_hesitation(quote["id"], raison)
        self.store.cancel_followups(quote["id"])  # un humain reprend la main
        self._send(lead, f"Merci pour votre retour. {company.dirigeant} vous rappelle pour en parler.")
        self._notify_owner(company, lead, f"Hésitation sur le devis ({raison}) : « {text} »")

    # -------------------------------------------------------------- tableau de bord
    def dashboard(self, company_id: str) -> dict:
        leads = self.store.leads_for_company(company_id)
        ids = {lead.id for lead in leads}
        events = [e for e in self.store.events() if e["lead_id"] in ids]

        def count(kind: str) -> int:
            return sum(1 for e in events if e["kind"] == kind)

        delays = []
        for lead in leads:
            first = next((e for e in events if e["lead_id"] == lead.id and e["kind"] == "premier_contact"), None)
            if first:
                delays.append((datetime.fromisoformat(first["at"]) - datetime.fromisoformat(lead.created_at)).total_seconds())
        fiches = [self.store.get_fiche(lid) for lid in ids]
        classes = [f["classement"] for f in fiches if f]
        accords = sum(
            1 for lead in leads
            if any(c["event"] in ("accord_appel", "accord_ecrit", "plus_tard") for c in self.store.consents(lead.id))
        )
        return {
            "demandes": len(leads),
            "delai_median_premier_contact_s": sorted(delays)[len(delays) // 2] if delays else None,
            "taux_accord": round(accords / len(leads), 2) if leads else None,
            "stop": sum(1 for lead in leads if lead.state is LeadState.OPTED_OUT),
            "a_visiter": classes.count("à visiter"),
            "a_rappeler": classes.count("à rappeler"),
            "a_surveiller": classes.count("à surveiller"),
            "transferts_humain": count("transfert_humain"),
            "questions_prix": count("question_prix"),
            "devis_relances": count("relance_envoyee"),
            "devis_signes": count("devis_signe"),
        }
