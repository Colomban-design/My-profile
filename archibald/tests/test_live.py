"""Mode réel : numéros, signature Twilio, appel vocal, page de démo et ses garde-fous."""

import base64
import hashlib
import hmac
import json
import threading
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, time

import pytest

from archibald.cli import FakeClock
from archibald.engine import Engine
from archibald.models import Company, LeadState
from archibald.phones import is_mobile_fr, to_e164
from archibald.providers import ConsoleMailer, ConsoleSms
from archibald.qualifier import ScriptedQualifier
from archibald.server import App, DemoGuard, serve
from archibald.store import Store
from archibald.twilio import TwilioConfig, twiml_gather, valid_signature

TEL = "+33611111111"
COMPANY = Company(id="demo", nom="Durand Rénovation", dirigeant="Marc", tel_dirigeant="+33600000001",
                  email_fiches="m@example.fr", metiers=["extension"], departements=[], budget_min=15000,
                  heures_contact=(time(8), time(21)))


@dataclass
class LiveVoice:
    live = True
    calls: list = field(default_factory=list)

    def start_call(self, to, lead_id):
        self.calls.append((to, lead_id))


def make_engine(voice=None):
    store = Store()
    store.save_company(COMPANY)
    clock = FakeClock(datetime(2026, 10, 27, 11, 0))
    return Engine(store, ScriptedQualifier(), ConsoleSms(), voice or LiveVoice(), ConsoleMailer(), clock)


def test_numeros():
    assert to_e164("06 12 34 56 78") == "+33612345678"
    assert to_e164("0033 7 12 34 56 78") == "+33712345678"
    assert to_e164("+33 6 12.34.56.78") == "+33612345678"
    assert is_mobile_fr("+33612345678") and not is_mobile_fr("+33112345678") and not is_mobile_fr("+14155550100")


def test_signature_twilio():
    url, params, token = "https://demo.example.fr/twilio/sms", {"From": TEL, "Body": "3"}, "secret"
    sig = base64.b64encode(hmac.new(token.encode(), (url + "Body3From" + TEL).encode(), hashlib.sha1).digest()).decode()
    assert valid_signature(token, url, params, sig)
    assert not valid_signature(token, url, {**params, "Body": "1"}, sig)
    assert not valid_signature("autre", url, params, sig)


def test_twiml_echappe_le_texte():
    xml = twiml_gather(["Surface < 150 m² & budget ?"], "https://x/turn?lead=a&b=c", "Polly.Lea")
    assert "&lt; 150 m² &amp; budget" in xml and 'action="https://x/turn?lead=a&amp;b=c"' in xml


def test_appel_reel_de_bout_en_bout():
    eng = make_engine()
    lead = eng.new_lead("demo", "06 11 11 11 11", "Julie", "démo", "Extension")
    assert lead.telephone == TEL
    eng.inbound_sms("06 11 11 11 11", "1")
    assert eng.voice.calls == [(TEL, lead.id)]
    assert eng.sms.sent[-1][1] == "Parfait, je vous appelle tout de suite."
    n_sms = len(eng.sms.sent)

    said = eng.call_answered(lead.id)
    assert "assistant IA" in said[0] and said[1].startswith("Quelle surface")
    ended = False
    for answer in ("30 mètres carrés, la maison fait 110", "69005", "dans 3 mois", "60 000 euros", "prêt accordé"):
        said, ended = eng.call_speech(lead.id, answer)
    assert ended and "c'est complet" in said[-1]
    assert len(eng.sms.sent) - n_sms == 1  # seule l'alerte « à visiter » au patron part en SMS
    assert eng.sms.sent[-1][0] == COMPANY.tel_dirigeant
    assert eng.store.get_lead(lead.id).state is LeadState.QUALIFIED
    assert eng.store.get_fiche(lead.id)["champs"]["code_postal"] == "69005"


def test_raccroche_en_cours_continue_par_sms():
    eng = make_engine()
    lead = eng.new_lead("demo", TEL, "Julie", "démo", "Extension")
    eng.inbound_sms(TEL, "1")
    eng.call_answered(lead.id)
    eng.call_speech(lead.id, "30 m²")
    eng.call_ended(lead.id, "completed")
    texts = [t for to, t in eng.sms.sent if to == TEL]
    assert "continuer par écrit" in texts[-2] and texts[-1].startswith("Dans quelle commune")
    eng.inbound_sms(TEL, "69005")
    assert eng.sms.sent[-1][1].startswith("Quand aimeriez-vous")


def test_stop_au_telephone():
    eng = make_engine()
    lead = eng.new_lead("demo", TEL, "Julie", "démo", "Extension")
    eng.inbound_sms(TEL, "1")
    eng.call_answered(lead.id)
    said, ended = eng.call_speech(lead.id, "stop")
    assert ended and "ne vous recontactera plus" in said[0]
    assert eng.store.is_opted_out(TEL)


def test_garde_fous_demo():
    g = DemoGuard(code="atelier", per_number_per_day=2, per_day=3)
    assert g.check(TEL, "mauvais") == "Code de démo incorrect."
    assert "mobile" in g.check("+33112345678", "atelier")
    assert g.check(TEL, "atelier") is None and g.check(TEL, "atelier") is None
    assert "plusieurs essais" in g.check(TEL, "atelier")
    assert g.check("+33622222222", "atelier") is None
    assert "plafond" in g.check("+33633333333", "atelier")


# --- serveur HTTP réel, sur un port libre ---------------------------------------

@pytest.fixture
def server():
    def start(cfg=None, guard=None):
        app = App(make_engine(), twilio_cfg=cfg, guard=guard or DemoGuard())
        srv = serve(app, port=0)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        started.append(srv)
        return app, f"http://127.0.0.1:{srv.server_address[1]}"
    started = []
    yield start
    for s in started:
        s.shutdown()


def call(url, body=None, form=None, headers=None):
    data = json.dumps(body).encode() if body is not None else urllib.parse.urlencode(form).encode() if form else None
    req = urllib.request.Request(url, data=data, headers=headers or {})
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def test_page_et_parcours_simulation(server):
    app, base = server()
    status, html = call(base + "/")
    assert status == 200 and "Essayez-le sur votre téléphone" in html
    status, cfg = call(base + "/api/demo/config")
    assert json.loads(cfg)["mode"] == "simulation"
    status, body = call(base + "/api/demo/lead", {"prenom": "Julie", "telephone": "06 11 11 11 11", "projet": "extension"})
    lead = json.loads(body)
    assert status == 201 and lead["state"] == "attente_accord" and "assistant IA" in lead["messages"][0]["text"]
    for text in ("3", "30 m², maison de 110 m²", "69005", "dans 3 mois", "60 000 €", "prêt accordé"):
        status, body = call(f"{base}/api/demo/lead/{lead['id']}/reply", {"text": text})
    view = json.loads(body)
    assert view["state"] == "qualifie" and view["fiche"]["classement"] == "à visiter"
    status, body = call(base + "/api/demo/lead", {"prenom": "X", "telephone": "01 23 45 67 89"})
    assert status == 400 and "mobile" in json.loads(body)["error"]


def test_webhook_twilio_refuse_une_fausse_signature(server):
    cfg = TwilioConfig("AC123", "secret", "+33900000000", "https://demo.example.fr")
    app, base = server(cfg)
    app.engine.new_lead("demo", TEL, "Julie", "démo", "Extension")
    status, _ = call(base + "/twilio/sms", form={"From": TEL, "Body": "3"}, headers={"X-Twilio-Signature": "faux"})
    assert status == 403
    url = cfg.public_url + "/twilio/sms"
    sig = base64.b64encode(hmac.new(b"secret", (url + "Body3From" + TEL).encode(), hashlib.sha1).digest()).decode()
    status, xml = call(base + "/twilio/sms", form={"From": TEL, "Body": "3"}, headers={"X-Twilio-Signature": sig})
    assert status == 200 and "<Response>" in xml
    assert app.engine.store.latest_lead_for_phone(TEL).state is LeadState.QUALIFYING
    status, _ = call(base + "/api/demo/lead/x/reply", {"text": "3"})
    assert status in (403, 400)


def test_webhooks_voix(server):
    app, base = server()  # sans config : pas de signature à vérifier
    eng = app.engine
    lead = eng.new_lead("demo", TEL, "Julie", "démo", "Extension")
    eng.inbound_sms(TEL, "1")
    status, xml = call(f"{base}/twilio/voice/answer?lead={lead.id}", form={"CallSid": "CA1"})
    assert "<Gather" in xml and "assistant IA" in xml and 'language="fr-FR"' in xml
    status, xml = call(f"{base}/twilio/voice/turn?lead={lead.id}", form={"SpeechResult": ""})
    assert "pas bien entendu" in xml
    status, xml = call(f"{base}/twilio/voice/turn?lead={lead.id}", form={"SpeechResult": "Je veux parler au patron"})
    assert "<Hangup/>" in xml
    assert eng.store.get_lead(lead.id).state is LeadState.HANDED_OFF
