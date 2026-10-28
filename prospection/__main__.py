"""Prospection Archibald, en ligne de commande (depuis la racine du dépôt) :

  python -m prospection trouver --departements 69,01,38      # 1. la liste (annuaire officiel)
  python -m prospection enrichir                             # 2. téléphone, site, avis (Google, facultatif)
  python -m prospection importer mes_contacts.csv            #    ou ajouter une liste à toi
  python -m prospection jour                                 # 3. CHAQUE MATIN : réponses, e-mails, fiches d'appel
  python -m prospection jour --vraiment                      #    … en envoyant vraiment
  python -m prospection marquer 812345678 demo "RDV jeudi"   # 4. noter ce qui s'est passé
  python -m prospection statut                               #    où on en est
  python -m prospection apercu 812345678                     #    voir les 3 e-mails d'un prospect

Fichiers (non versionnés, données personnelles) : prospection/donnees/prospects.csv (ouvrable dans
Excel ou Google Sheets), envois.csv (journal), appels-AAAA-MM-JJ.md (fiches du jour).
"""

from __future__ import annotations

import argparse
import csv
import os
import random
import sys
import time
from collections import Counter
from datetime import date, datetime
from pathlib import Path

from . import crm, envoi, messages, sources

DATA = Path(os.environ.get("PROSPECTION_DONNEES", Path(__file__).resolve().parent / "donnees"))
PROSPECTS = DATA / "prospects.csv"
ENVOIS = DATA / "envois.csv"
MAX_PAR_JOUR = int(os.environ.get("PROSPECTION_MAX_PAR_JOUR", "30"))


def _rows() -> list[dict]:
    rows = crm.load(PROSPECTS)
    if not rows:
        sys.exit(f"Aucun prospect dans {PROSPECTS}. Lance d'abord : python -m prospection trouver --departements 69")
    return rows


def _log_envoi(r: dict, rang: int, sujet: str, mode: str) -> None:
    new = not ENVOIS.exists()
    with ENVOIS.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["date", "mode", "siren", "entreprise", "email", "rang", "sujet"])
        w.writerow([datetime.now().isoformat(timespec="seconds"), mode, r["siren"], r["entreprise"], r["email"], rang, sujet])


def _envoyes_aujourdhui() -> int:
    if not ENVOIS.exists():
        return 0
    today = date.today().isoformat()
    with ENVOIS.open(encoding="utf-8") as f:
        return sum(1 for r in csv.DictReader(f) if r["date"].startswith(today) and r["mode"] == "reel")


def cmd_trouver(a) -> None:
    deps = [d.strip() for d in a.departements.split(",") if d.strip()]
    print(f"Recherche dans l'annuaire officiel : départements {', '.join(deps)}…")
    new = sources.annuaire(deps, maximum=a.max)
    rows, added = crm.merge(crm.load(PROSPECTS), new)
    DATA.mkdir(parents=True, exist_ok=True)
    crm.save(PROSPECTS, rows)
    print(f"{len(new)} entreprises trouvées, {added} nouvelles. Total : {len(rows)} → {PROSPECTS}")
    print("Étape suivante : python -m prospection enrichir (téléphone et site), puis ajoute les e-mails trouvés sur les sites.")


def cmd_enrichir(a) -> None:
    key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not key:
        sys.exit("Il faut une clé Google (GOOGLE_MAPS_API_KEY, API « Places API (New) » activée). "
                 "Sans clé : complète téléphone et site à la main dans le CSV pour les 30 premiers.")
    rows = _rows()
    todo = [r for r in rows if not r.get("telephone") and not r.get("enrichi")][: a.max]
    ok = 0
    for i, r in enumerate(todo, 1):
        try:
            found = sources.places(r["entreprise"], r["commune"] or r["code_postal"], key)
        except sources.SourceError as e:
            print(f"  arrêt : {e}")
            break
        r["enrichi"] = date.today().isoformat()
        if found:
            for k, v in found.items():
                if v and not r.get(k):
                    r[k] = v
            ok += 1
        if i % 20 == 0:
            print(f"  {i}/{len(todo)}…")
    for r in rows:
        r["score"] = str(crm.score(r))
    crm.save(PROSPECTS, rows)
    print(f"{ok}/{len(todo)} fiches Google trouvées. Scores recalculés.")


def cmd_importer(a) -> None:
    """Ajoute un CSV à toi (export d'un salon, d'une CAPEB, d'un tableur). Colonnes reconnues : celles de prospects.csv."""
    with open(a.fichier, newline="", encoding="utf-8-sig") as f:
        new = []
        for i, r in enumerate(csv.DictReader(f)):
            r = {k.strip().lower(): (v or "").strip() for k, v in r.items() if k}
            r.setdefault("siren", r.get("siret", "")[:9] or f"import-{Path(a.fichier).stem}-{i}")
            r["source"] = r.get("source") or f"import {Path(a.fichier).name}"
            new.append(r)
    rows, added = crm.merge(crm.load(PROSPECTS), new)
    DATA.mkdir(parents=True, exist_ok=True)
    crm.save(PROSPECTS, rows)
    print(f"{added} prospects ajoutés depuis {a.fichier}. Total : {len(rows)}")


def cmd_jour(a) -> None:
    rows = _rows()
    today, now = date.today(), datetime.now()
    smtp = envoi.SmtpConfig.from_env()

    # 1. Les réponses d'abord : on n'écrit jamais à quelqu'un qui a répondu ou dit stop.
    imap_host = os.environ.get("IMAP_HOST")
    if smtp and imap_host:
        by_mail = {r["email"].lower(): r for r in rows if r.get("email")}
        for addr, verdict in envoi.reponses(smtp, imap_host, set(by_mail)).items():
            r = by_mail[addr]
            if r["statut"] in crm.ACTIFS or r["statut"].startswith("email_") or r["statut"] == "sans_reponse":
                r["statut"] = verdict
                r["prochaine_action"] = "rappeler aujourd'hui" if verdict == "repondu" else ""
                print(f"  ✉ {r['entreprise']} : {'a répondu → à rappeler' if verdict == 'repondu' else 'stop, retiré'}")
    else:
        print("  (réponses non vérifiées automatiquement : IMAP_HOST non réglé. Marque-les avec « marquer ».)")
    n_fermes = crm.fermer_sequences(rows, today)

    # 2. Les e-mails du jour, dans les plafonds.
    dus = [(r, rang) for r in rows if (rang := crm.prochain_email(r, today))]
    dus.sort(key=lambda x: (-x[1], -int(x[0]["score"] or 0)))  # relances d'abord, puis les meilleurs scores
    reste = max(0, MAX_PAR_JOUR - _envoyes_aujourdhui())
    if a.vraiment and not smtp:
        sys.exit("Pour envoyer, règle SMTP_HOST, SMTP_USER, SMTP_PASSWORD (voir prospection/README.md).")
    if a.vraiment and not envoi.heure_ok(now):
        print("  Pas d'envoi maintenant (on écrit du lundi au vendredi, 7 h - 19 h).")
        dus = []
    a_envoyer = dus[: min(reste, a.max)]
    mode = "reel" if a.vraiment else "essai"
    if a_envoyer:
        print(f"\n{'Envoi' if a.vraiment else 'Essai (rien ne part, ajoute --vraiment)'} : {len(a_envoyer)} e-mail(s) "
              f"sur {len(dus)} dus, plafond {MAX_PAR_JOUR}/jour.")

    def traiter(r, rang, sender=None):
        sujet, corps = messages.email(rang, r)
        if sender:
            sender.envoyer(r["email"], sujet, corps)
        _log_envoi(r, rang, sujet, mode)
        if a.vraiment:
            r["statut"], r["dernier_contact"] = f"email_{rang}", now.isoformat(timespec="seconds")
            r["prochaine_action"] = "appeler" if rang == 3 else f"e-mail {rang + 1}"
        print(f"  {'→' if a.vraiment else '·'} e-mail {rang} à {r['entreprise']} <{r['email']}> : {sujet}")

    if a.vraiment and a_envoyer:
        with envoi.Expediteur(smtp) as sender:
            for i, (r, rang) in enumerate(a_envoyer):
                traiter(r, rang, sender)
                crm.save(PROSPECTS, rows)  # sauvegarde après chaque envoi : rien n'est envoyé deux fois
                if i < len(a_envoyer) - 1:
                    time.sleep(random.uniform(a.pause * 0.6, a.pause * 1.4))  # rythme humain, meilleure délivrabilité
    else:
        for r, rang in a_envoyer:
            traiter(r, rang)

    # 3. Les appels du jour : ceux qui ont répondu, puis les meilleurs scores avec téléphone.
    appels = [r for r in rows if r["statut"] == "repondu"]
    appels += [r for r in rows if r["statut"] in ("sans_reponse", "email_2", "email_3") and r.get("telephone")]
    appels += [r for r in rows if r["statut"] == "a_contacter" and r.get("telephone") and not r.get("email")]
    vus, liste = set(), []
    for r in appels:
        if r["siren"] not in vus:
            vus.add(r["siren"])
            liste.append(r)
    liste = liste[: a.appels]
    if liste:
        path = DATA / f"appels-{today.isoformat()}.md"
        path.write_text(f"# Appels du {today.strftime('%d/%m/%Y')} ({len(liste)})\n\nMeilleurs créneaux pour joindre un "
                        "dirigeant du bâtiment : tôt le matin ou en fin de journée, pas en pleine journée de chantier.\n\n"
                        + "\n---\n\n".join(messages.fiche_appel(r) for r in liste), encoding="utf-8")
        print(f"\n{len(liste)} appel(s) à passer : {path}")
    crm.save(PROSPECTS, rows)
    if n_fermes:
        print(f"{n_fermes} séquence(s) terminée(s) sans réponse : à appeler.")
    _statut(rows)


def cmd_marquer(a) -> None:
    rows = _rows()
    r = next((x for x in rows if x["siren"] == a.siren or x["entreprise"].lower() == a.siren.lower()), None)
    if not r:
        sys.exit(f"Introuvable : {a.siren}")
    valides = crm.ACTIFS | crm.FINAUX | {"email_3"}
    if a.statut not in valides:
        sys.exit(f"Statut inconnu. Choisis parmi : {', '.join(sorted(valides))}")
    r["statut"] = a.statut
    if a.note:
        r["notes"] = (r["notes"] + " | " if r["notes"] else "") + f"{date.today():%d/%m} {a.note}"
    r["dernier_contact"] = datetime.now().isoformat(timespec="seconds")
    crm.save(PROSPECTS, rows)
    print(f"{r['entreprise']} → {a.statut}")


def _statut(rows: list[dict]) -> None:
    c = Counter(r["statut"] for r in rows)
    ordre = ["a_contacter", "email_1", "email_2", "email_3", "sans_reponse", "repondu", "demo", "pilote", "client",
             "pas_interesse", "stop"]
    print("\nEntonnoir : " + " · ".join(f"{s} {c[s]}" for s in ordre if c[s]))
    contactes = sum(c[s] for s in ordre[1:])
    if contactes:
        print(f"Taux de réponse : {sum(c[s] for s in ('repondu', 'demo', 'pilote', 'client', 'pas_interesse')) / contactes:.0%} "
              f"· démos : {c['demo'] + c['pilote'] + c['client']} · pilotes : {c['pilote'] + c['client']}")
    manque = sum(1 for r in rows if r["statut"] == "a_contacter" and not r.get("email"))
    if manque:
        print(f"{manque} prospect(s) sans e-mail : complète la colonne « email » (page contact de leur site) "
              "ou appelle-les directement.")


def cmd_statut(a) -> None:
    _statut(_rows())


def cmd_apercu(a) -> None:
    r = next((x for x in _rows() if x["siren"] == a.siren), None)
    if not r:
        sys.exit(f"Introuvable : {a.siren}")
    for rang in (1, 2, 3):
        sujet, corps = messages.email(rang, r)
        print(f"===== E-mail {rang} (J+{crm.SEQUENCE[rang]} ouvrés) =====\nObjet : {sujet}\n\n{corps}\n")


def main(argv=None) -> None:
    p = argparse.ArgumentParser(prog="python -m prospection", description="Prospection Archibald")
    sub = p.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("trouver")
    t.add_argument("--departements", required=True, help="ex. 69,01,38")
    t.add_argument("--max", type=int, default=300)
    e = sub.add_parser("enrichir")
    e.add_argument("--max", type=int, default=100, help="nombre d'appels Google (payants au-delà du crédit gratuit)")
    i = sub.add_parser("importer")
    i.add_argument("fichier")
    j = sub.add_parser("jour")
    j.add_argument("--vraiment", action="store_true", help="envoyer réellement (sinon : essai, rien ne part)")
    j.add_argument("--max", type=int, default=MAX_PAR_JOUR)
    j.add_argument("--appels", type=int, default=10)
    j.add_argument("--pause", type=float, default=60, help="secondes entre deux e-mails")
    m = sub.add_parser("marquer")
    m.add_argument("siren")
    m.add_argument("statut")
    m.add_argument("note", nargs="?", default="")
    sub.add_parser("statut")
    ap = sub.add_parser("apercu")
    ap.add_argument("siren")
    a = p.parse_args(argv)
    try:
        {"trouver": cmd_trouver, "enrichir": cmd_enrichir, "importer": cmd_importer, "jour": cmd_jour,
         "marquer": cmd_marquer, "statut": cmd_statut, "apercu": cmd_apercu}[a.cmd](a)
    except sources.SourceError as exc:
        sys.exit(f"Erreur : {exc}")


if __name__ == "__main__":
    main()
