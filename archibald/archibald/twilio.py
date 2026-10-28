"""Connexion à Twilio : vrais SMS, vrais appels, et vérification des webhooks.

Pas de SDK : deux appels REST et la signature des webhooks suffisent.
Variables d'environnement : TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM (le numéro
Twilio, format +33…), PUBLIC_URL (adresse publique du serveur, pour que Twilio le joigne).
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from xml.sax.saxutils import escape, quoteattr

API = "https://api.twilio.com/2010-04-01/Accounts/{sid}/{path}"


@dataclass
class TwilioConfig:
    account_sid: str
    auth_token: str
    from_number: str
    public_url: str
    voice: str = "Polly.Lea"

    @classmethod
    def from_env(cls) -> "TwilioConfig | None":
        keys = ("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "TWILIO_FROM", "PUBLIC_URL")
        if not all(os.environ.get(k) for k in keys):
            return None
        return cls(*(os.environ[k] for k in keys[:3]), os.environ["PUBLIC_URL"].rstrip("/"),
                   os.environ.get("ARCHIBALD_VOICE", "Polly.Lea"))


@dataclass
class _Client:
    cfg: TwilioConfig
    errors: list[str] = field(default_factory=list)

    def _post(self, path: str, data: dict) -> dict | None:
        url = API.format(sid=self.cfg.account_sid, path=path)
        auth = base64.b64encode(f"{self.cfg.account_sid}:{self.cfg.auth_token}".encode()).decode()
        req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(),
                                     headers={"Authorization": f"Basic {auth}"})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            try:
                detail = json.load(exc).get("message", "")
            except Exception:  # réponse illisible : on garde le code HTTP
                detail = ""
            self.errors.append(f"Twilio {exc.code} : {detail}".strip())
        except urllib.error.URLError as exc:
            self.errors.append(f"Twilio injoignable : {exc.reason}")
        print(f"[twilio] {self.errors[-1]}", file=sys.stderr)
        return None


class TwilioSms(_Client):
    def send(self, to: str, text: str) -> None:
        self._post("Messages.json", {"From": self.cfg.from_number, "To": to, "Body": text})


class TwilioVoice(_Client):
    live = True  # le moteur attend que le client décroche au lieu de simuler l'appel

    def start_call(self, to: str, lead_id: str) -> None:
        q = urllib.parse.urlencode({"lead": lead_id})
        self._post("Calls.json", {
            "From": self.cfg.from_number, "To": to,
            "Url": f"{self.cfg.public_url}/twilio/voice/answer?{q}", "Method": "POST",
            "StatusCallback": f"{self.cfg.public_url}/twilio/voice/status?{q}", "StatusCallbackMethod": "POST",
        })


def valid_signature(auth_token: str, url: str, params: dict[str, str], signature: str) -> bool:
    """Signature X-Twilio-Signature : HMAC-SHA1 de l'URL suivie des paramètres triés."""
    payload = url + "".join(k + params[k] for k in sorted(params))
    digest = hmac.new(auth_token.encode(), payload.encode(), hashlib.sha1).digest()
    return hmac.compare_digest(base64.b64encode(digest).decode(), signature or "")


def _says(texts: list[str], voice: str) -> str:
    return "".join(f'<Say language="fr-FR" voice={quoteattr(voice)}>{escape(t)}</Say>' for t in texts if t)


def twiml_gather(texts: list[str], action: str, voice: str) -> str:
    """Dire les répliques puis écouter la réponse (reconnaissance vocale en français)."""
    return ('<?xml version="1.0" encoding="UTF-8"?><Response>'
            f'<Gather input="speech" language="fr-FR" speechTimeout="auto" actionOnEmptyResult="true" '
            f'method="POST" action={quoteattr(action)}>{_says(texts, voice)}</Gather></Response>')


def twiml_hangup(texts: list[str], voice: str) -> str:
    return f'<?xml version="1.0" encoding="UTF-8"?><Response>{_says(texts, voice)}<Hangup/></Response>'


EMPTY = '<?xml version="1.0" encoding="UTF-8"?><Response></Response>'
