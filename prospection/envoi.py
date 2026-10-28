"""Envoi des e-mails depuis ta propre boîte (SMTP) et lecture des réponses (IMAP).

Réglages par variables d'environnement :
  SMTP_HOST, SMTP_PORT (587), SMTP_USER, SMTP_PASSWORD, SMTP_FROM (« Prénom Nom <toi@domaine.fr> »)
  IMAP_HOST (facultatif, même identifiants) pour repérer automatiquement les réponses et les « stop ».

Avec Gmail ou Google Workspace : smtp.gmail.com / imap.gmail.com et un « mot de passe
d'application ». Utilise de préférence un domaine secondaire (ex. archibald-renov.fr) pour
ne pas abîmer la réputation de ton domaine principal.
"""

from __future__ import annotations

import email
import email.utils
import imaplib
import os
import re
import smtplib
from dataclasses import dataclass
from datetime import datetime
from email.message import EmailMessage

STOP_RE = re.compile(r"^\s*(stop|desinscri|désinscri|ne plus|retirez|pas intéress|pas interess)", re.I)


@dataclass
class SmtpConfig:
    host: str
    port: int
    user: str
    password: str
    sender: str

    @classmethod
    def from_env(cls) -> "SmtpConfig | None":
        e = os.environ
        if not all(e.get(k) for k in ("SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD")):
            return None
        return cls(e["SMTP_HOST"], int(e.get("SMTP_PORT", "587")), e["SMTP_USER"], e["SMTP_PASSWORD"],
                   e.get("SMTP_FROM", e["SMTP_USER"]))


def heure_ok(now: datetime) -> bool:
    """Du lundi au vendredi, 7 h - 19 h : les e-mails arrivent quand un dirigeant les lit."""
    return now.weekday() < 5 and 7 <= now.hour < 19


def construire(cfg: SmtpConfig, to: str, sujet: str, corps: str) -> EmailMessage:
    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = cfg.sender, to, sujet
    msg["Date"] = email.utils.formatdate(localtime=True)
    msg["Message-ID"] = email.utils.make_msgid(domain=cfg.sender.split("@")[-1].strip(">"))
    addr = email.utils.parseaddr(cfg.sender)[1]
    msg["List-Unsubscribe"] = f"<mailto:{addr}?subject=stop>"
    msg.set_content(corps)  # texte brut : passe mieux les filtres et ressemble à un vrai e-mail
    return msg


class Expediteur:
    def __init__(self, cfg: SmtpConfig):
        self.cfg = cfg
        self.smtp: smtplib.SMTP | None = None

    def __enter__(self):
        self.smtp = smtplib.SMTP(self.cfg.host, self.cfg.port, timeout=30)
        self.smtp.starttls()
        self.smtp.login(self.cfg.user, self.cfg.password)
        return self

    def envoyer(self, to: str, sujet: str, corps: str) -> None:
        self.smtp.send_message(construire(self.cfg, to, sujet, corps))

    def __exit__(self, *exc):
        if self.smtp:
            self.smtp.quit()


def classer_reponse(texte: str) -> str:
    """« stop » si la personne refuse, sinon « repondu »."""
    premiere = next((l for l in texte.splitlines() if l.strip() and not l.startswith(">")), "")
    return "stop" if STOP_RE.search(premiere) else "repondu"


def corps_texte(msg: email.message.Message) -> str:
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8", "replace")
        return ""
    return msg.get_payload(decode=True).decode(msg.get_content_charset() or "utf-8", "replace")


def reponses(cfg: SmtpConfig, imap_host: str, adresses: set[str], jours: int = 30) -> dict[str, str]:
    """{adresse du prospect : 'repondu' | 'stop'} pour les e-mails reçus récemment de prospects."""
    found: dict[str, str] = {}
    since = (datetime.now().date().toordinal() - jours)
    since_str = datetime.fromordinal(since).strftime("%d-%b-%Y")
    with imaplib.IMAP4_SSL(imap_host) as m:
        m.login(cfg.user, cfg.password)
        m.select("INBOX", readonly=True)
        _, ids = m.search(None, f'(SINCE "{since_str}")')
        for i in ids[0].split()[-500:]:
            _, data = m.fetch(i, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])
            sender = email.utils.parseaddr(msg.get("From", ""))[1].lower()
            if sender in adresses:
                verdict = classer_reponse(corps_texte(msg))
                if found.get(sender) != "stop":
                    found[sender] = verdict
    return found
