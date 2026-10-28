"""Serveur HTTP (bibliothèque standard) : démo, webhooks Twilio et API JSON.

Démo (une page) :
    GET  /                              la page « essayez Archibald sur votre téléphone »
    GET  /api/demo/config               mode (twilio / simulation), nom de l'entreprise, code requis ?
    POST /api/demo/lead                 {"prenom", "telephone", "projet", "code"} → lance le vrai SMS
    GET  /api/demo/lead/<id>            fil de la conversation + fiche, lu par la page toutes les 1,5 s
    POST /api/demo/lead/<id>/reply      {"text"} : répondre à la place du client (mode simulation seulement)
    GET  /console                       l'ancienne console détaillée (scénarios simulés)

Twilio (signature vérifiée) :
    POST /twilio/sms                    SMS reçu du client
    POST /twilio/voice/answer?lead=…    le client décroche
    POST /twilio/voice/turn?lead=…      ce que le client vient de dire
    POST /twilio/voice/status?lead=…    fin d'appel (raccroché, pas de réponse…)

API JSON (intégrations) : POST /leads, /sms/inbound, /quotes, /quotes/<id>/status, /tick ;
GET /report?company_id=…
"""

from __future__ import annotations

import json
import os
import secrets
import threading
import time
from collections import defaultdict, deque
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlparse

from . import twilio
from .engine import Engine
from .models import QuoteStatus
from .phones import is_mobile_fr, pretty, to_e164

DEMO_DIR = Path(__file__).resolve().parent.parent / "demo"
SKELETON = (
    '<!doctype html><html lang="fr"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    "<style>[hidden]{display:none!important}body{margin:0}</style></head><body>{page}</body></html>"
)
PROJETS = {
    "extension": "Extension de la maison",
    "surelevation": "Surélévation",
    "renovation": "Rénovation complète",
    "autre": "Autres travaux",
}


@dataclass
class DemoGuard:
    """Garde-fous de la démo publique : code d'accès, mobiles français, plafonds d'envoi."""

    code: str = ""
    per_number_per_day: int = 3
    per_day: int = 50
    _by_number: dict[str, deque] = field(default_factory=lambda: defaultdict(deque))
    _all: deque = field(default_factory=deque)

    def check(self, telephone: str, code: str, now: float | None = None) -> str | None:
        now = now or time.time()
        if self.code and not secrets.compare_digest(code.strip(), self.code):
            return "Code de démo incorrect."
        if not is_mobile_fr(telephone):
            return "Entrez un numéro de mobile français (06 ou 07)."
        for q in (self._all, self._by_number[telephone]):
            while q and now - q[0] > 86400:
                q.popleft()
        if len(self._all) >= self.per_day:
            return "La démo a atteint son plafond d'envois pour aujourd'hui."
        if len(self._by_number[telephone]) >= self.per_number_per_day:
            return "Ce numéro a déjà fait plusieurs essais aujourd'hui."
        self._all.append(now)
        self._by_number[telephone].append(now)
        return None


@dataclass
class App:
    engine: Engine
    company_id: str = "demo"
    twilio_cfg: twilio.TwilioConfig | None = None
    guard: DemoGuard = field(default_factory=DemoGuard)
    lock: threading.Lock = field(default_factory=threading.Lock)
    silences: dict[str, int] = field(default_factory=lambda: defaultdict(int))

    @property
    def live(self) -> bool:
        return self.twilio_cfg is not None

    def provider_errors(self) -> list[str]:
        errs = []
        for p in (self.engine.sms, self.engine.voice):
            errs += getattr(p, "errors", [])
        return errs

    def lead_view(self, lead_id: str) -> dict:
        lead = self.engine.store.get_lead(lead_id)
        msgs = [{"dir": r["direction"], "text": r["texte"], "at": r["at"][11:16]} for r in self.engine.store.history(lead_id)]
        return {
            "id": lead.id, "prenom": lead.prenom, "telephone": pretty(lead.telephone), "state": lead.state.value,
            "canal": lead.canal, "en_appel": lead_id in self.engine._calls, "messages": msgs,
            "fiche": self.engine.store.get_fiche(lead_id), "mode": "twilio" if self.live else "simulation",
            "erreurs": self.provider_errors()[-3:],
        }


def make_handler(app: App):
    engine = app.engine

    class Handler(BaseHTTPRequestHandler):
        # ---------------------------------------------------------------- outils
        def _send(self, code: int, body: bytes, ctype: str) -> None:
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, code: int, payload) -> None:
            self._send(code, json.dumps(payload, ensure_ascii=False).encode(), "application/json; charset=utf-8")

        def _xml(self, xml: str) -> None:
            self._send(200, xml.encode(), "text/xml; charset=utf-8")

        def _raw(self) -> bytes:
            return self.rfile.read(int(self.headers.get("Content-Length") or 0))

        def _twilio_params(self) -> dict[str, str] | None:
            """Paramètres d'un webhook Twilio, ou None si la signature est fausse."""
            params = {k: v[0] for k, v in parse_qs(self._raw().decode(), keep_blank_values=True).items()}
            cfg = app.twilio_cfg
            if cfg is None:
                return params  # mode simulation : pas de signature à vérifier
            url = cfg.public_url + self.path
            if not twilio.valid_signature(cfg.auth_token, url, params, self.headers.get("X-Twilio-Signature", "")):
                return None
            return params

        # ------------------------------------------------------------------- GET
        def do_GET(self):  # noqa: N802
            url = urlparse(self.path)
            path = url.path.rstrip("/") or "/"
            if path in ("/", "/console"):
                page = DEMO_DIR / ("index.html" if path == "/" else "console.html")
                html = SKELETON.replace("{page}", page.read_text(encoding="utf-8"))
                return self._send(200, html.encode(), "text/html; charset=utf-8")
            if path == "/api/demo/config":
                c = engine.store.get_company(app.company_id)
                return self._json(200, {"mode": "twilio" if app.live else "simulation", "entreprise": c.nom,
                                        "dirigeant": c.dirigeant, "code_requis": bool(app.guard.code)})
            if path.startswith("/api/demo/lead/"):
                with app.lock:
                    try:
                        return self._json(200, app.lead_view(path.split("/")[4]))
                    except KeyError:
                        return self._json(404, {"error": "demande inconnue"})
            if path == "/report":
                company_id = parse_qs(url.query).get("company_id", [app.company_id])[0]
                with app.lock:
                    return self._json(200, engine.dashboard(company_id))
            return self._json(404, {"error": "route inconnue"})

        # ------------------------------------------------------------------ POST
        def do_POST(self):  # noqa: N802
            url = urlparse(self.path)
            path = url.path.rstrip("/")
            if path.startswith("/twilio/"):
                return self._twilio(path, parse_qs(url.query).get("lead", [""])[0])
            try:
                data = json.loads(self._raw() or b"{}")
                with app.lock:
                    return self._api(path, data)
            except (KeyError, ValueError, json.JSONDecodeError) as exc:
                return self._json(400, {"error": str(exc)})

        def _api(self, path: str, data: dict):
            if path == "/api/demo/lead":
                tel = to_e164(str(data.get("telephone", "")))
                prenom = str(data.get("prenom", "")).strip()[:40]
                if not prenom:
                    return self._json(400, {"error": "Indiquez un prénom."})
                refus = app.guard.check(tel, str(data.get("code", "")))
                if refus:
                    return self._json(400, {"error": refus})
                projet = PROJETS.get(str(data.get("projet", "")), PROJETS["autre"])
                lead = engine.new_lead(app.company_id, tel, prenom, "démo", projet)
                return self._json(201, app.lead_view(lead.id))
            if path.startswith("/api/demo/lead/") and path.endswith("/reply"):
                if app.live:
                    return self._json(403, {"error": "En mode réel, répondez depuis votre téléphone."})
                lead = engine.store.get_lead(path.split("/")[4])
                engine.inbound_sms(lead.telephone, str(data["text"])[:500])
                return self._json(200, app.lead_view(lead.id))
            if path == "/leads":
                lead = engine.new_lead(data["company_id"], data["telephone"], data.get("prenom", ""),
                                       data.get("source", "site"), data.get("message", ""), bool(data.get("recommande")))
                return self._json(201, {"lead_id": lead.id, "state": lead.state.value})
            if path == "/sms/inbound":
                engine.inbound_sms(data["from"], data["text"])
                return self._json(200, {"ok": True})
            if path == "/quotes":
                return self._json(201, {"quote_id": engine.quote_sent(data["lead_id"], data.get("montant"), data.get("quote_id"))})
            if path.startswith("/quotes/") and path.endswith("/status"):
                engine.quote_status(path.split("/")[2], QuoteStatus(data["status"]))
                return self._json(200, {"ok": True})
            if path == "/tick":
                return self._json(200, {"relances_envoyees": engine.tick()})
            return self._json(404, {"error": "route inconnue"})

        def _twilio(self, path: str, lead_id: str):
            params = self._twilio_params()
            if params is None:
                return self._send(403, b"signature invalide", "text/plain")
            voice = app.twilio_cfg.voice if app.twilio_cfg else "Polly.Lea"
            turn_url = f"{app.twilio_cfg.public_url if app.twilio_cfg else ''}/twilio/voice/turn?{urlencode({'lead': lead_id})}"
            with app.lock:
                try:
                    if path == "/twilio/sms":
                        engine.inbound_sms(params.get("From", ""), params.get("Body", ""))
                        return self._xml(twilio.EMPTY)
                    if path == "/twilio/voice/answer":
                        said = engine.call_answered(lead_id)
                        if lead_id not in engine._calls:
                            return self._xml(twilio.twiml_hangup(said, voice))
                        return self._xml(twilio.twiml_gather(said, turn_url, voice))
                    if path == "/twilio/voice/turn":
                        speech = params.get("SpeechResult", "").strip()
                        if not speech:
                            app.silences[lead_id] += 1
                            if app.silences[lead_id] >= 2:
                                engine.call_ended(lead_id, "silence")
                                return self._xml(twilio.twiml_hangup(
                                    ["Je vous entends mal. Je vous écris par SMS pour continuer. Au revoir."], voice))
                            last = [r["texte"] for r in engine.store.history(lead_id) if r["direction"] == "out"][-1:]
                            return self._xml(twilio.twiml_gather(["Pardon, je n'ai pas bien entendu."] + last, turn_url, voice))
                        app.silences[lead_id] = 0
                        said, ended = engine.call_speech(lead_id, speech)
                        if ended:
                            return self._xml(twilio.twiml_hangup(said + ["Au revoir."], voice))
                        return self._xml(twilio.twiml_gather(said, turn_url, voice))
                    if path == "/twilio/voice/status":
                        if params.get("CallStatus") in ("completed", "busy", "no-answer", "failed", "canceled"):
                            engine.call_ended(lead_id, params.get("CallStatus", ""))
                        return self._xml(twilio.EMPTY)
                except KeyError:
                    return self._xml(twilio.twiml_hangup([], voice) if "voice" in path else twilio.EMPTY)
            return self._send(404, b"", "text/plain")

        def log_message(self, fmt, *args):  # journal HTTP silencieux
            pass

    return Handler


def serve(app: App, host: str = "127.0.0.1", port: int = 8000) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), make_handler(app))


def guard_from_env() -> DemoGuard:
    return DemoGuard(
        code=os.environ.get("DEMO_CODE", ""),
        per_number_per_day=int(os.environ.get("DEMO_MAX_PAR_NUMERO", "3")),
        per_day=int(os.environ.get("DEMO_MAX_PAR_JOUR", "50")),
    )
