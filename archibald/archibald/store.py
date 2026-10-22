"""Stockage SQLite : leads, preuves de consentement, messages, fiches, devis, relances."""

from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict
from datetime import datetime

from .models import Company, Fiche, Lead, LeadState, QuoteStatus

SCHEMA = """
CREATE TABLE IF NOT EXISTS companies (id TEXT PRIMARY KEY, data TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS leads (
    id TEXT PRIMARY KEY, company_id TEXT NOT NULL, telephone TEXT NOT NULL, data TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS leads_phone ON leads (telephone);
-- Preuve de consentement : à conserver 3 ans (réforme du démarchage, 11/08/2026).
CREATE TABLE IF NOT EXISTS consents (
    id INTEGER PRIMARY KEY AUTOINCREMENT, lead_id TEXT NOT NULL, telephone TEXT NOT NULL,
    event TEXT NOT NULL,            -- demande_envoyee | accord_appel | accord_ecrit | plus_tard | stop
    texte TEXT NOT NULL, at TEXT NOT NULL, conserver_jusqu_au TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS optouts (telephone TEXT PRIMARY KEY, at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT, lead_id TEXT NOT NULL,
    direction TEXT NOT NULL,        -- in | out
    texte TEXT NOT NULL, at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS fiches (lead_id TEXT PRIMARY KEY, data TEXT NOT NULL, at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS quotes (
    id TEXT PRIMARY KEY, lead_id TEXT NOT NULL, montant INTEGER, envoye_le TEXT NOT NULL,
    status TEXT NOT NULL, raison_hesitation TEXT DEFAULT ''
);
CREATE TABLE IF NOT EXISTS followups (
    id INTEGER PRIMARY KEY AUTOINCREMENT, quote_id TEXT NOT NULL, due_at TEXT NOT NULL,
    rang INTEGER NOT NULL, status TEXT NOT NULL   -- a_envoyer | envoye | annule
);
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT, lead_id TEXT, kind TEXT NOT NULL, detail TEXT, at TEXT NOT NULL
);
"""


class Store:
    def __init__(self, path: str = ":memory:"):
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)

    # --- entreprises -------------------------------------------------------
    def save_company(self, c: Company) -> None:
        data = asdict(c)
        data["heures_contact"] = [t.isoformat() for t in c.heures_contact]
        self.db.execute("INSERT OR REPLACE INTO companies VALUES (?, ?)", (c.id, json.dumps(data)))
        self.db.commit()

    def get_company(self, company_id: str) -> Company:
        row = self.db.execute("SELECT data FROM companies WHERE id = ?", (company_id,)).fetchone()
        if row is None:
            raise KeyError(f"entreprise inconnue : {company_id}")
        data = json.loads(row["data"])
        from datetime import time

        data["heures_contact"] = tuple(time.fromisoformat(t) for t in data["heures_contact"])
        return Company(**data)

    # --- leads ---------------------------------------------------------------
    def save_lead(self, lead: Lead) -> None:
        data = asdict(lead)
        data["state"] = lead.state.value
        self.db.execute(
            "INSERT OR REPLACE INTO leads VALUES (?, ?, ?, ?)",
            (lead.id, lead.company_id, lead.telephone, json.dumps(data, ensure_ascii=False)),
        )
        self.db.commit()

    def get_lead(self, lead_id: str) -> Lead:
        row = self.db.execute("SELECT data FROM leads WHERE id = ?", (lead_id,)).fetchone()
        if row is None:
            raise KeyError(f"lead inconnu : {lead_id}")
        return self._lead(row["data"])

    def latest_lead_for_phone(self, telephone: str) -> Lead | None:
        row = self.db.execute(
            "SELECT data FROM leads WHERE telephone = ? ORDER BY rowid DESC LIMIT 1", (telephone,)
        ).fetchone()
        return self._lead(row["data"]) if row else None

    def leads_for_company(self, company_id: str) -> list[Lead]:
        rows = self.db.execute("SELECT data FROM leads WHERE company_id = ?", (company_id,)).fetchall()
        return [self._lead(r["data"]) for r in rows]

    @staticmethod
    def _lead(raw: str) -> Lead:
        data = json.loads(raw)
        data["state"] = LeadState(data["state"])
        return Lead(**data)

    # --- consentement -------------------------------------------------------
    def record_consent(self, lead: Lead, event: str, texte: str, now: datetime) -> None:
        keep_until = now.replace(year=now.year + 3)
        self.db.execute(
            "INSERT INTO consents (lead_id, telephone, event, texte, at, conserver_jusqu_au) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (lead.id, lead.telephone, event, texte, now.isoformat(), keep_until.isoformat()),
        )
        self.db.commit()

    def consents(self, lead_id: str) -> list[sqlite3.Row]:
        return self.db.execute(
            "SELECT * FROM consents WHERE lead_id = ? ORDER BY id", (lead_id,)
        ).fetchall()

    def opt_out(self, telephone: str, now: datetime) -> None:
        self.db.execute("INSERT OR REPLACE INTO optouts VALUES (?, ?)", (telephone, now.isoformat()))
        self.db.commit()

    def is_opted_out(self, telephone: str) -> bool:
        return self.db.execute("SELECT 1 FROM optouts WHERE telephone = ?", (telephone,)).fetchone() is not None

    # --- messages -----------------------------------------------------------
    def log_message(self, lead_id: str, direction: str, texte: str, now: datetime) -> None:
        self.db.execute(
            "INSERT INTO messages (lead_id, direction, texte, at) VALUES (?, ?, ?, ?)",
            (lead_id, direction, texte, now.isoformat()),
        )
        self.db.commit()

    def history(self, lead_id: str) -> list[sqlite3.Row]:
        return self.db.execute(
            "SELECT direction, texte, at FROM messages WHERE lead_id = ? ORDER BY id", (lead_id,)
        ).fetchall()

    # --- fiches -------------------------------------------------------------
    def save_fiche(self, fiche: Fiche, now: datetime) -> None:
        data = asdict(fiche)
        data["classement"] = fiche.classement.value
        self.db.execute(
            "INSERT OR REPLACE INTO fiches VALUES (?, ?, ?)",
            (fiche.lead_id, json.dumps(data, ensure_ascii=False), now.isoformat()),
        )
        self.db.commit()

    def get_fiche(self, lead_id: str) -> dict | None:
        row = self.db.execute("SELECT data FROM fiches WHERE lead_id = ?", (lead_id,)).fetchone()
        return json.loads(row["data"]) if row else None

    # --- devis et relances --------------------------------------------------
    def save_quote(self, quote_id: str, lead_id: str, montant: int | None, envoye_le: datetime) -> None:
        self.db.execute(
            "INSERT OR REPLACE INTO quotes (id, lead_id, montant, envoye_le, status) VALUES (?, ?, ?, ?, ?)",
            (quote_id, lead_id, montant, envoye_le.isoformat(), QuoteStatus.ENVOYE.value),
        )
        self.db.commit()

    def get_quote(self, quote_id: str) -> sqlite3.Row:
        row = self.db.execute("SELECT * FROM quotes WHERE id = ?", (quote_id,)).fetchone()
        if row is None:
            raise KeyError(f"devis inconnu : {quote_id}")
        return row

    def open_quote_for_lead(self, lead_id: str) -> sqlite3.Row | None:
        return self.db.execute(
            "SELECT * FROM quotes WHERE lead_id = ? AND status = ? ORDER BY rowid DESC LIMIT 1",
            (lead_id, QuoteStatus.ENVOYE.value),
        ).fetchone()

    def set_quote_status(self, quote_id: str, status: QuoteStatus) -> None:
        self.db.execute("UPDATE quotes SET status = ? WHERE id = ?", (status.value, quote_id))
        if status is not QuoteStatus.ENVOYE:
            self.cancel_followups(quote_id)
        self.db.commit()

    def set_hesitation(self, quote_id: str, raison: str) -> None:
        self.db.execute("UPDATE quotes SET raison_hesitation = ? WHERE id = ?", (raison, quote_id))
        self.db.commit()

    def add_followup(self, quote_id: str, due_at: datetime, rang: int) -> None:
        self.db.execute(
            "INSERT INTO followups (quote_id, due_at, rang, status) VALUES (?, ?, ?, 'a_envoyer')",
            (quote_id, due_at.isoformat(), rang),
        )
        self.db.commit()

    def due_followups(self, now: datetime) -> list[sqlite3.Row]:
        return self.db.execute(
            "SELECT * FROM followups WHERE status = 'a_envoyer' AND due_at <= ? ORDER BY due_at",
            (now.isoformat(),),
        ).fetchall()

    def mark_followup(self, followup_id: int, status: str) -> None:
        self.db.execute("UPDATE followups SET status = ? WHERE id = ?", (status, followup_id))
        self.db.commit()

    def cancel_followups(self, quote_id: str) -> None:
        self.db.execute(
            "UPDATE followups SET status = 'annule' WHERE quote_id = ? AND status = 'a_envoyer'", (quote_id,)
        )
        self.db.commit()

    def cancel_followups_for_phone(self, telephone: str) -> None:
        self.db.execute(
            "UPDATE followups SET status = 'annule' WHERE status = 'a_envoyer' AND quote_id IN "
            "(SELECT q.id FROM quotes q JOIN leads l ON l.id = q.lead_id WHERE l.telephone = ?)",
            (telephone,),
        )
        self.db.commit()

    # --- journal ------------------------------------------------------------
    def log_event(self, lead_id: str | None, kind: str, detail: str, now: datetime) -> None:
        self.db.execute(
            "INSERT INTO events (lead_id, kind, detail, at) VALUES (?, ?, ?, ?)",
            (lead_id, kind, detail, now.isoformat()),
        )
        self.db.commit()

    def events(self, kind: str | None = None) -> list[sqlite3.Row]:
        if kind:
            return self.db.execute("SELECT * FROM events WHERE kind = ? ORDER BY id", (kind,)).fetchall()
        return self.db.execute("SELECT * FROM events ORDER BY id").fetchall()
