"""Les règles qui ne doivent jamais casser : consentement, STOP, prix, humain, relances, horaires."""

from datetime import datetime, time, timedelta
from types import SimpleNamespace

import pytest

from archibald.cli import FakeClock
from archibald.engine import Engine
from archibald.models import Classement, Company, LeadState, QuoteStatus
from archibald.providers import ConsoleMailer, ConsoleSms, ConsoleVoice
from archibald.qualifier import ClaudeQualifier, ScriptedQualifier, Turn, guard
from archibald.scoring import besoin_architecte, classify
from archibald.store import Store

TEL = "+33611111111"
PATRON = "+33600000001"
COMPANY = Company(
    id="c1", nom="Durand Rénovation", dirigeant="Marc", tel_dirigeant=PATRON, email_fiches="marc@example.fr",
    metiers=["extension"], departements=["69"], budget_min=30000, heures_contact=(time(9), time(20)),
)


@pytest.fixture
def env():
    clock = FakeClock(datetime(2026, 10, 20, 18, 0))  # mardi
    store = Store()
    store.save_company(COMPANY)
    engine = Engine(store, ScriptedQualifier(), ConsoleSms(), ConsoleVoice(), ConsoleMailer(), clock)
    return SimpleNamespace(engine=engine, store=store, clock=clock, sms=engine.sms, mail=engine.mailer)


def to_client(env):
    return [t for to, t in env.sms.sent if to == TEL]


def qualify_fully(env, lead=None):
    lead = lead or env.engine.new_lead("c1", TEL, "Julie", message="Extension de 30 m² côté jardin")
    env.engine.inbound_sms(TEL, "3")
    for a in ("30 m², maison de 110 m²", "69005", "dans 3 mois", "60 000 €", "prêt accordé"):
        env.engine.inbound_sms(TEL, a)
    return env.store.get_lead(lead.id)


def test_premier_message_demande_l_accord_et_rien_d_autre(env):
    lead = env.engine.new_lead("c1", TEL, "Julie", message="Extension 30 m²")
    msgs = to_client(env)
    assert len(msgs) == 1
    assert "assistant IA" in msgs[0] and "STOP" in msgs[0] and "1, 2 ou 3" in msgs[0]
    assert env.engine.voice.calls == []
    assert env.store.get_lead(lead.id).state is LeadState.AWAITING_CONSENT
    assert [c["event"] for c in env.store.consents(lead.id)] == ["demande_envoyee"]


def test_reponse_floue_ne_lance_pas_la_qualification(env):
    lead = env.engine.new_lead("c1", TEL, "Julie")
    env.engine.inbound_sms(TEL, "c'est pour quoi ?")
    assert env.store.get_lead(lead.id).state is LeadState.AWAITING_CONSENT
    assert "1 (appel maintenant)" in to_client(env)[-1]


def test_accord_appel_en_journee_lance_l_appel(env):
    env.clock.now = env.clock.now.replace(hour=11)
    lead = env.engine.new_lead("c1", TEL, "Julie")
    env.engine.inbound_sms(TEL, "1")
    assert env.engine.voice.calls == [(TEL, lead.id)]
    assert "accord_appel" in [c["event"] for c in env.store.consents(lead.id)]


def test_pas_d_appel_apres_les_heures(env):
    env.clock.now = env.clock.now.replace(hour=21, minute=30)
    env.engine.new_lead("c1", TEL, "Julie")
    env.engine.inbound_sms(TEL, "1")
    assert env.engine.voice.calls == []
    assert "par écrit" in " ".join(to_client(env))


def test_contact_recommande_jamais_appele_par_l_ia(env):
    env.clock.now = env.clock.now.replace(hour=11)
    env.engine.new_lead("c1", TEL, "Julie", recommande=True)
    assert "vous rappelle personnellement" in to_client(env)[0]
    env.engine.inbound_sms(TEL, "1")
    assert env.engine.voice.calls == []


def test_preuve_de_consentement_conservee_3_ans(env):
    lead = env.engine.new_lead("c1", TEL, "Julie")
    env.engine.inbound_sms(TEL, "3")
    rows = env.store.consents(lead.id)
    assert [r["event"] for r in rows] == ["demande_envoyee", "accord_ecrit"]
    for r in rows:
        kept = datetime.fromisoformat(r["conserver_jusqu_au"]) - datetime.fromisoformat(r["at"])
        assert kept >= timedelta(days=3 * 365)
        assert r["texte"]


def test_stop_arrete_tout_y_compris_les_relances(env):
    lead = qualify_fully(env)
    env.engine.quote_sent(lead.id, 50000)
    env.engine.inbound_sms(TEL, "STOP")
    assert "ne vous contactera plus" in to_client(env)[-1]
    n = len(env.sms.sent)
    env.clock.advance(days=25)
    env.clock.now = env.clock.now.replace(hour=10)
    assert env.engine.tick() == 0
    env.engine.inbound_sms(TEL, "finalement oui")
    assert len(env.sms.sent) == n
    # Une nouvelle demande depuis ce numéro n'est pas relancée non plus.
    again = env.engine.new_lead("c1", TEL, "Julie")
    assert again.state is LeadState.OPTED_OUT and len(env.sms.sent) == n


def test_jamais_de_prix_en_mode_script(env):
    env.engine.new_lead("c1", TEL, "Julie")
    env.engine.inbound_sms(TEL, "3")
    env.engine.inbound_sms(TEL, "Combien ça coûte une extension de 30 m² ?")
    reply = to_client(env)[-1]
    assert "ne peux pas vous donner de prix" in reply
    assert "€" not in reply


def test_garde_fou_retire_un_montant_invente(env):
    lead = env.engine.new_lead("c1", TEL, "Julie")
    history = [("out", "Quel budget ?"), ("in", "Je ne sais pas, c'est combien en général ?")]
    turn = guard(Turn(reply="Comptez environ 45 000 € pour 30 m²."), COMPANY, history, ScriptedQualifier(), lead)
    assert "45 000" not in turn.reply and "€" not in turn.reply and "ne peux pas vous donner de prix" in turn.reply


def test_garde_fou_laisse_reprendre_le_montant_du_client(env):
    lead = env.engine.new_lead("c1", TEL, "Julie")
    history = [("out", "Quel budget ?"), ("in", "60 000 €")]
    turn = guard(Turn(reply="Merci, 60 000 € noté. Comment financez-vous ?"), COMPANY, history,
                 ScriptedQualifier(), lead)
    assert turn.reply.startswith("Merci, 60 000 €")


def test_demande_d_humain_previent_le_dirigeant(env):
    lead = env.engine.new_lead("c1", TEL, "Julie")
    env.engine.inbound_sms(TEL, "3")
    env.engine.inbound_sms(TEL, "Je préfère parler à quelqu'un")
    assert env.store.get_lead(lead.id).state is LeadState.HANDED_OFF
    assert any(to == PATRON and "parler" in t for to, t in env.sms.sent)


def test_plus_tard_enregistre_le_creneau(env):
    lead = env.engine.new_lead("c1", TEL, "Julie")
    env.engine.inbound_sms(TEL, "2")
    env.engine.inbound_sms(TEL, "jeudi vers 18h")
    lead = env.store.get_lead(lead.id)
    assert lead.creneau_prefere == "jeudi vers 18h" and lead.state is LeadState.HANDED_OFF


def test_qualification_complete_envoie_la_fiche(env):
    lead = qualify_fully(env, env.engine.new_lead("c1", TEL, "Julie", message="Extension 30 m²"))
    assert lead.state is LeadState.QUALIFIED
    to, subject, body = env.mail.sent[-1]
    assert to == "marc@example.fr" and "à visiter" in subject
    assert "69005" in body and '"classement": "à visiter"' in body


def test_classement():
    ok = {"type_travaux": "extension", "code_postal": "69005", "delai": "3 mois",
          "budget": "60 000 €", "financement": "prêt accordé"}
    assert classify(COMPANY, ok)[0] is Classement.A_VISITER
    assert classify(COMPANY, {**ok, "financement": "prêt en cours"})[0] is Classement.A_RAPPELER
    assert classify(COMPANY, {**ok, "budget": "12 000 €"})[0] is Classement.A_SURVEILLER
    assert classify(COMPANY, {**ok, "code_postal": "75011"})[0] is Classement.A_SURVEILLER
    assert classify(COMPANY, {**ok, "delai": "dans 2 ans"})[0] is Classement.A_SURVEILLER
    assert classify(COMPANY, {**ok, "delai": "d'ici 4 mois"})[0] is Classement.A_VISITER


def test_seuil_architecte():
    assert besoin_architecte({"surface_m2": "40", "surface_existante_m2": "120"}).startswith("oui")
    assert besoin_architecte({"surface_m2": "20", "surface_existante_m2": "100"}).startswith("non")
    assert besoin_architecte({"surface_m2": "20"}).startswith("à vérifier")


def test_relances_j3_j10_j20_puis_arret_si_signe(env):
    lead = qualify_fully(env)
    env.clock.now = datetime(2026, 10, 21, 10, 0)
    qid = env.engine.quote_sent(lead.id, 55000)
    env.clock.now += timedelta(days=3, minutes=1)
    assert env.engine.tick() == 1
    env.clock.now += timedelta(days=7)
    assert env.engine.tick() == 1
    env.engine.quote_status(qid, QuoteStatus.SIGNE)
    env.clock.now += timedelta(days=10)
    assert env.engine.tick() == 0


def test_relance_attend_les_heures_permises(env):
    lead = qualify_fully(env)
    env.clock.now = datetime(2026, 10, 21, 22, 0)
    env.engine.quote_sent(lead.id)
    env.clock.now += timedelta(days=3, minutes=1)  # samedi 22h01
    assert env.engine.tick() == 0
    env.clock.now += timedelta(hours=12)  # dimanche 10h01 : toujours pas
    assert env.engine.tick() == 0
    env.clock.now += timedelta(days=1)  # lundi 10h01
    assert env.engine.tick() == 1


def test_hesitation_sur_devis_remonte_au_dirigeant(env):
    lead = qualify_fully(env)
    qid = env.engine.quote_sent(lead.id)
    env.engine.inbound_sms(TEL, "C'est un peu cher pour nous")
    assert env.store.get_quote(qid)["raison_hesitation"] == "prix"
    assert any(to == PATRON and "prix" in t for to, t in env.sms.sent)


def test_tableau_de_bord(env):
    qualify_fully(env)
    d = env.engine.dashboard("c1")
    assert d["demandes"] == 1 and d["taux_accord"] == 1.0 and d["a_visiter"] == 1


# --- Claude, avec un faux client API (aucun appel réseau) -------------------------

class FakeClient:
    def __init__(self, payload=None, stop_reason="end_turn"):
        self.payload, self.stop_reason, self.calls = payload, stop_reason, []
        self.beta = SimpleNamespace(messages=SimpleNamespace(create=self._create))

    def _create(self, **kw):
        self.calls.append(kw)
        import json
        block = SimpleNamespace(type="text", text=json.dumps(self.payload))
        return SimpleNamespace(stop_reason=self.stop_reason, content=[block])


def _payload(reply, **fields):
    base = {k: "" for k in ("type_travaux", "surface_m2", "surface_existante_m2", "code_postal",
                            "delai", "budget", "financement", "photos")}
    return {"reply": reply, "fields": {**base, **fields}, "done": False, "wants_human": False,
            "asked_price": False}


def test_claude_qualifier_appel_et_champs(env):
    lead = env.engine.new_lead("c1", TEL, "Julie")
    client = FakeClient(_payload("Dans quelle commune ?", surface_m2="30"))
    turn = ClaudeQualifier(client=client).next_turn(COMPANY, lead, [("in", "30 m²")])
    assert turn.fields == {"surface_m2": "30"} and turn.reply == "Dans quelle commune ?"
    kw = client.calls[0]
    assert kw["output_config"]["format"]["type"] == "json_schema"
    assert kw["messages"][-1]["role"] == "user"


def test_claude_qualifier_montant_invente_bloque(env):
    lead = env.engine.new_lead("c1", TEL, "Julie")
    client = FakeClient(_payload("Une extension coûte environ 2 000 €/m²."))
    turn = ClaudeQualifier(client=client).next_turn(COMPANY, lead, [("in", "c'est cher ?")])
    assert "2 000" not in turn.reply


def test_claude_qualifier_refus_passe_a_l_humain(env):
    lead = env.engine.new_lead("c1", TEL, "Julie")
    turn = ClaudeQualifier(client=FakeClient({}, stop_reason="refusal")).next_turn(COMPANY, lead, [("in", "x")])
    assert turn.wants_human
