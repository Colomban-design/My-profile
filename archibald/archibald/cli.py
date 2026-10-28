"""Démo de bout en bout et lancement du serveur.

    python -m archibald.cli demo      # un lead complet, en console
    python -m archibald.cli serve     # webhooks sur http://127.0.0.1:8000
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, time, timedelta

from .engine import Engine
from .models import Company, QuoteStatus
from .phones import to_e164
from .providers import ConsoleMailer, ConsoleSms, ConsoleVoice
from .qualifier import ScriptedQualifier
from .store import Store

DEMO_COMPANY = Company(
    id="demo", nom="Maisons Durand Rénovation", dirigeant="Marc", tel_dirigeant="+33600000001",
    email_fiches="marc@example.fr", metiers=["extension", "surélévation", "rénovation globale"],
    departements=["69", "01", "38"], budget_min=30000, heures_contact=(time(9), time(20)),
)


def pick_qualifier():
    if os.environ.get("ANTHROPIC_API_KEY"):
        from .qualifier import ClaudeQualifier

        print("Qualification : Claude (ANTHROPIC_API_KEY trouvée)\n")
        return ClaudeQualifier()
    print("Qualification : script de secours (pas de clé API)\n")
    return ScriptedQualifier()


class FakeClock:
    def __init__(self, start: datetime):
        self.now = start

    def __call__(self) -> datetime:
        return self.now

    def advance(self, **kw) -> None:
        self.now += timedelta(**kw)


def demo(scripted: bool = False) -> None:
    clock = FakeClock(datetime(2026, 10, 20, 18, 42))  # un mardi soir, sur le chantier
    store = Store()
    store.save_company(DEMO_COMPANY)
    engine = Engine(
        store, qualifier=ScriptedQualifier() if scripted else pick_qualifier(),
        sms=ConsoleSms(echo=True), voice=ConsoleVoice(echo=True), mailer=ConsoleMailer(echo=True), clock=clock,
    )

    def client(text: str) -> None:
        clock.advance(minutes=2)
        print(f"  [CLIENT] {text}")
        engine.inbound_sms("+33611111111", text)

    print("== 18:42 — Demande de devis sur le site ==")
    lead = engine.new_lead("demo", "+33611111111", "Julie", "site", "Extension de 30 m² côté jardin")
    print("\n== Le client choisit l'écrit ==")
    client("3")
    for answer in ("30 m², la maison fait 110 m²", "Combien ça coûte à peu près ?", "69005",
                   "Au printemps, d'ici 4 mois", "Environ 60 000 €", "Prêt accordé par la banque + apport"):
        client(answer)
        if engine.store.get_lead(lead.id).state.value != "qualification":
            break

    print("\n== Fiche reçue par l'entreprise ==")
    print(engine.mailer.sent[-1][2] if engine.mailer.sent else "(aucune fiche)")

    print("\n== Devis envoyé, relances automatiques ==")
    envoi = clock.now
    qid = engine.quote_sent(lead.id, 58000)
    for days in (3, 10):
        clock.now = envoi + timedelta(days=days, minutes=5)
        print(f"-- J+{days}, {clock.now:%d/%m %H:%M} --")
        engine.tick()
    client("On hésite, le prix est un peu au-dessus de ce qu'on pensait")
    engine.quote_status(qid, QuoteStatus.SIGNE)

    print("\n== Tableau de bord ==")
    print(json.dumps(engine.dashboard("demo"), ensure_ascii=False, indent=2))


def company_from_env() -> Company:
    """Entreprise de la démo, réglable sans toucher au code."""
    env = os.environ.get
    deps = [d.strip() for d in env("ARCHIBALD_DEPARTEMENTS", "").split(",") if d.strip()]
    return Company(
        id="demo", nom=env("ARCHIBALD_ENTREPRISE", DEMO_COMPANY.nom), dirigeant=env("ARCHIBALD_DIRIGEANT", "Marc"),
        tel_dirigeant=to_e164(env("ARCHIBALD_TEL_DIRIGEANT", "")), email_fiches=env("ARCHIBALD_EMAIL", "fiches@example.fr"),
        metiers=DEMO_COMPANY.metiers, departements=deps, budget_min=int(env("ARCHIBALD_BUDGET_MIN", "15000")),
        heures_contact=(time(int(env("ARCHIBALD_HEURE_DEBUT", "8"))), time(int(env("ARCHIBALD_HEURE_FIN", "21")))),
    )


def build_app(db: str):
    from .server import App, guard_from_env
    from .twilio import TwilioConfig, TwilioSms, TwilioVoice

    store = Store(db)
    store.save_company(company_from_env())
    cfg = TwilioConfig.from_env()
    if cfg:
        sms, voice = TwilioSms(cfg), TwilioVoice(cfg)
        print(f"Mode réel : SMS et appels via Twilio depuis {cfg.from_number}, webhooks sur {cfg.public_url}")
    else:
        sms, voice = ConsoleSms(echo=True), ConsoleVoice(echo=True)
        print("Mode simulation (pas de variables TWILIO_*) : les SMS s'affichent ici et sur la page.")
    engine = Engine(store, qualifier=pick_qualifier(), sms=sms, voice=voice, mailer=ConsoleMailer(echo=True))
    return App(engine, twilio_cfg=cfg, guard=guard_from_env())


def main() -> None:
    parser = argparse.ArgumentParser(prog="archibald")
    sub = parser.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("demo", help="un lead complet, en console")
    d.add_argument("--scripted", action="store_true", help="forcer le script, même avec une clé API")
    s = sub.add_parser("serve", help="la page de démo + les webhooks")
    s.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"))
    s.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8000")))
    s.add_argument("--db", default=os.environ.get("ARCHIBALD_DB", "archibald.db"))
    args = parser.parse_args()
    if args.cmd == "demo":
        demo(args.scripted)
    else:
        from .server import serve

        app = build_app(args.db)
        print(f"Démo : http://{args.host}:{args.port}/")
        serve(app, args.host, args.port).serve_forever()


if __name__ == "__main__":
    main()
