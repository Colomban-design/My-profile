"""Le fichier de suivi : un CSV qu'on ouvre dans Excel ou Google Sheets, et que l'outil met à jour.

Statuts : a_contacter → email_1 → email_2 → email_3 → sans_reponse
          à tout moment : repondu, demo, pilote, client, pas_interesse, stop (désinscription)
"""

from __future__ import annotations

import csv
from datetime import date, datetime, timedelta
from pathlib import Path

from .sources import NAF

COLUMNS = [
    "score", "statut", "entreprise", "dirigeant", "prenom_dirigeant", "qualite", "commune", "code_postal",
    "activite", "effectif", "telephone", "email", "site", "note_google", "avis_google",
    "dernier_contact", "prochaine_action", "notes", "siren", "naf", "adresse", "creation", "source",
]
# Séquence : e-mail n° rang envoyé après N jours ouvrés sans réponse depuis le précédent.
SEQUENCE = {1: 0, 2: 4, 3: 10}
ACTIFS = {"a_contacter", "email_1", "email_2"}       # la séquence continue
FINAUX = {"repondu", "demo", "pilote", "client", "pas_interesse", "stop", "sans_reponse"}


def load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as f:
        return [{c: (r.get(c) or "") for c in COLUMNS} | {k: v for k, v in r.items() if k not in COLUMNS} for r in csv.DictReader(f)]


def save(path: Path, rows: list[dict]) -> None:
    rows = sorted(rows, key=lambda r: (-int(r.get("score") or 0), r.get("entreprise", "")))
    extra = sorted({k for r in rows for k in r} - set(COLUMNS))
    tmp = path.with_suffix(".tmp")
    with tmp.open("w", newline="", encoding="utf-8-sig") as f:  # utf-8-sig : Excel lit les accents
        w = csv.DictWriter(f, fieldnames=COLUMNS + extra)
        w.writeheader()
        w.writerows(rows)
    tmp.replace(path)


def merge(existing: list[dict], new: list[dict]) -> tuple[list[dict], int]:
    """Ajoute les nouveaux SIREN sans jamais écraser ce que tu as rempli à la main."""
    by_siren = {r["siren"]: r for r in existing}
    added = 0
    for row in new:
        if row["siren"] in by_siren:
            cur = by_siren[row["siren"]]
            for k, v in row.items():
                if v and not cur.get(k):
                    cur[k] = v
        else:
            by_siren[row["siren"]] = {c: "" for c in COLUMNS} | row | {"statut": "a_contacter"}
            added += 1
    rows = list(by_siren.values())
    for r in rows:
        r["score"] = str(score(r))
    return rows, added


def score(r: dict) -> int:
    """Sur 100 : plus c'est haut, plus l'entreprise reçoit probablement des demandes de devis
    qu'elle n'a pas le temps de rappeler. Règles simples, à ajuster après les premières démos."""
    s = 10 * NAF.get(r.get("naf", ""), ("", 0))[1]                 # métier : jusqu'à 30
    s += {"6-9": 25, "10-19": 25, "20-49": 15, "3-5": 15, "1-2": 5}.get(r.get("effectif", ""), 0)
    if r.get("creation"):
        try:
            years = (date.today() - date.fromisoformat(r["creation"][:10])).days / 365
            s += 10 if years >= 3 else 0                              # installée : a déjà un flux de demandes
        except ValueError:
            pass
    if r.get("site"):
        s += 10                                                       # un site = un formulaire de devis
    if r.get("telephone"):
        s += 5
    if r.get("email"):
        s += 5
    try:
        s += min(15, int(r.get("avis_google") or 0) // 4)             # beaucoup d'avis = beaucoup de clients
    except ValueError:
        pass
    return min(100, s)


def jours_ouvres(depuis: date, jusqua: date) -> int:
    n, d = 0, depuis
    while d < jusqua:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


def prochain_email(r: dict, today: date) -> int | None:
    """Numéro de l'e-mail à envoyer aujourd'hui (1, 2 ou 3), ou None."""
    if r.get("statut") not in ACTIFS or not r.get("email"):
        return None
    rang = 1 if r["statut"] == "a_contacter" else int(r["statut"][-1]) + 1
    if rang == 1:
        return 1
    try:
        last = datetime.fromisoformat(r["dernier_contact"]).date()
    except ValueError:
        return rang
    return rang if jours_ouvres(last, today) >= SEQUENCE[rang] - SEQUENCE[rang - 1] else None


def fermer_sequences(rows: list[dict], today: date) -> int:
    """Après le 3e e-mail sans réponse depuis 7 jours ouvrés : sans_reponse (reste à appeler)."""
    n = 0
    for r in rows:
        if r.get("statut") == "email_3" and r.get("dernier_contact"):
            if jours_ouvres(datetime.fromisoformat(r["dernier_contact"]).date(), today) >= 7:
                r["statut"], r["prochaine_action"] = "sans_reponse", "appeler"
                n += 1
    return n
