"""Webhooks HTTP (bibliothèque standard uniquement) pour brancher le formulaire du
site, l'opérateur SMS et le logiciel de devis.

    POST /leads                    {"company_id", "telephone", "prenom", "source", "message", "recommande"}
    POST /sms/inbound              {"from", "text"}           (format à adapter à l'opérateur)
    POST /quotes                   {"lead_id", "montant"}
    POST /quotes/<id>/status       {"status": "signé" | "perdu"}
    POST /tick                     envoie les relances dues (à appeler par cron)
    GET  /report?company_id=...    tableau de bord

Prototype : pas d'authentification ni de vérification de signature. À ajouter
avant toute exposition publique (signature de l'opérateur SMS, jeton par entreprise).
"""

from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from .engine import Engine
from .models import QuoteStatus


def make_handler(engine: Engine):
    lock = threading.Lock()  # SQLite + moteur : un événement à la fois

    class Handler(BaseHTTPRequestHandler):
        def _json(self, code: int, payload) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _body(self) -> dict:
            length = int(self.headers.get("Content-Length") or 0)
            return json.loads(self.rfile.read(length) or b"{}")

        def do_POST(self):  # noqa: N802
            path = urlparse(self.path).path.rstrip("/")
            try:
                data = self._body()
                with lock:
                    if path == "/leads":
                        lead = engine.new_lead(
                            data["company_id"], data["telephone"], data.get("prenom", ""),
                            data.get("source", "site"), data.get("message", ""), bool(data.get("recommande")),
                        )
                        return self._json(201, {"lead_id": lead.id, "state": lead.state.value})
                    if path == "/sms/inbound":
                        engine.inbound_sms(data["from"], data["text"])
                        return self._json(200, {"ok": True})
                    if path == "/quotes":
                        qid = engine.quote_sent(data["lead_id"], data.get("montant"), data.get("quote_id"))
                        return self._json(201, {"quote_id": qid})
                    if path.startswith("/quotes/") and path.endswith("/status"):
                        engine.quote_status(path.split("/")[2], QuoteStatus(data["status"]))
                        return self._json(200, {"ok": True})
                    if path == "/tick":
                        return self._json(200, {"relances_envoyees": engine.tick()})
                return self._json(404, {"error": "route inconnue"})
            except (KeyError, ValueError, json.JSONDecodeError) as exc:
                return self._json(400, {"error": str(exc)})

        def do_GET(self):  # noqa: N802
            url = urlparse(self.path)
            if url.path.rstrip("/") == "/report":
                company_id = parse_qs(url.query).get("company_id", [""])[0]
                with lock:
                    return self._json(200, engine.dashboard(company_id))
            return self._json(404, {"error": "route inconnue"})

        def log_message(self, fmt, *args):  # journal HTTP silencieux
            pass

    return Handler


def serve(engine: Engine, host: str = "127.0.0.1", port: int = 8000) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), make_handler(engine))
