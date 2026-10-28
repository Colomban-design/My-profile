"""Tests de l'outil de prospection, sans réseau. Les entreprises ci-dessous sont fictives."""

from datetime import date, datetime

import pytest

import prospection.__main__ as cli
from prospection import crm, envoi, messages, sources

# Forme d'un résultat de l'annuaire (recherche-entreprises.api.gouv.fr), réduite aux champs lus.
ANNUAIRE_RESULT = {
    "siren": "900000001", "nom_complet": "MAISONS EXEMPLE (MAISONS EXEMPLE)", "nom_raison_sociale": "MAISONS EXEMPLE",
    "date_creation": "2015-03-01",
    "siege": {"activite_principale": "41.20A", "tranche_effectif_salarie": "11", "adresse": "1 RUE DE TEST 69005 LYON",
              "code_postal": "69005", "libelle_commune": "LYON"},
    "dirigeants": [{"nom": "EXEMPLE", "prenoms": "JEAN PIERRE", "qualite": "Gérant", "type_dirigeant": "personne physique"}],
}


def test_lecture_annuaire():
    r = sources.parse_annuaire(ANNUAIRE_RESULT)
    assert r["entreprise"] == "Maisons Exemple" and r["prenom_dirigeant"] == "Jean" and r["dirigeant"] == "Jean Exemple"
    assert r["effectif"] == "10-19" and r["activite"] == "Construction de maisons individuelles" and r["commune"] == "Lyon"


def test_lecture_annuaire_champs_absents():
    r = sources.parse_annuaire({"siren": "900000002"})
    assert r["siren"] == "900000002" and r["entreprise"] == "" and r["dirigeant"] == ""


def test_lecture_google():
    p = sources.parse_place({"nationalPhoneNumber": "04 00 00 00 00", "websiteUri": "https://exemple.fr", "rating": 4.7,
                             "userRatingCount": 52})
    assert p == {"telephone": "04 00 00 00 00", "site": "https://exemple.fr", "note_google": "4.7", "avis_google": "52"}


def test_fusion_ne_perd_jamais_le_travail_manuel():
    a = sources.parse_annuaire(ANNUAIRE_RESULT)
    rows, added = crm.merge([], [a])
    assert added == 1 and rows[0]["statut"] == "a_contacter"
    rows[0]["email"], rows[0]["notes"], rows[0]["statut"] = "contact@exemple.fr", "rappeler lundi", "email_1"
    rows, added = crm.merge(rows, [a | {"commune": "Autre"}])
    assert added == 0 and rows[0]["email"] == "contact@exemple.fr" and rows[0]["statut"] == "email_1"
    assert rows[0]["notes"] == "rappeler lundi" and rows[0]["commune"] == "Lyon"


def test_score():
    base = sources.parse_annuaire(ANNUAIRE_RESULT)
    s0 = crm.score(base)
    assert s0 == 30 + 25 + 10
    assert crm.score(base | {"site": "x", "telephone": "x", "email": "x", "avis_google": "80"}) == min(100, s0 + 20 + 15)
    assert crm.score(base | {"naf": "43.91B", "effectif": "1-2"}) < s0


def test_sequence_jours_ouvres():
    r = {"statut": "a_contacter", "email": "a@b.fr", "dernier_contact": ""}
    assert crm.prochain_email(r, date(2026, 11, 2)) == 1
    r |= {"statut": "email_1", "dernier_contact": "2026-11-02T09:00:00"}   # lundi
    assert crm.prochain_email(r, date(2026, 11, 5)) is None                # jeudi : 3 jours ouvrés
    assert crm.prochain_email(r, date(2026, 11, 6)) == 2                   # vendredi : 4
    r |= {"statut": "email_2", "dernier_contact": "2026-11-06T09:00:00"}
    assert crm.prochain_email(r, date(2026, 11, 13)) is None               # 5 ouvrés
    assert crm.prochain_email(r, date(2026, 11, 16)) == 3                  # 6 ouvrés
    assert crm.prochain_email(r | {"statut": "repondu"}, date(2026, 12, 1)) is None
    assert crm.prochain_email(r | {"email": ""}, date(2026, 12, 1)) is None


def test_fin_de_sequence():
    rows = [{"statut": "email_3", "dernier_contact": "2026-11-02T09:00:00", "prochaine_action": ""}]
    assert crm.fermer_sequences(rows, date(2026, 11, 10)) == 0
    assert crm.fermer_sequences(rows, date(2026, 11, 11)) == 1 and rows[0]["statut"] == "sans_reponse"


@pytest.mark.parametrize("texte,attendu", [
    ("Stop merci", "stop"), ("STOP", "stop"), ("Pas intéressé, bonne journée", "stop"),
    ("Oui, appelez-moi jeudi", "repondu"), ("Bonjour, c'est quoi le prix ?\n\n> Stop pour ne plus recevoir", "repondu"),
])
def test_classement_des_reponses(texte, attendu):
    assert envoi.classer_reponse(texte) == attendu


def test_messages_complets():
    r = crm.merge([], [sources.parse_annuaire(ANNUAIRE_RESULT)])[0][0]
    cfg = {"expediteur": "Camille", "lien_demo": "https://demo.example.fr", "code_demo": "atelier", "zone": "dans le Rhône"}
    for rang in (1, 2, 3):
        sujet, corps = messages.email(rang, r, cfg)
        assert "$" not in sujet + corps and "Bonjour Jean" in corps and "stop" in corps
    assert "https://demo.example.fr (code : atelier)" in messages.email(1, r, cfg)[1]
    assert "Maisons Exemple" in messages.fiche_appel(r, cfg)
    sans_prenom = messages.email(1, r | {"prenom_dirigeant": ""}, cfg)[1]
    assert sans_prenom.startswith("Bonjour Madame, Monsieur")


def test_heures_d_envoi():
    assert envoi.heure_ok(datetime(2026, 11, 3, 8, 30))
    assert not envoi.heure_ok(datetime(2026, 11, 3, 20, 0))
    assert not envoi.heure_ok(datetime(2026, 11, 7, 10, 0))  # samedi


def test_email_construit():
    cfg = envoi.SmtpConfig("smtp.x", 587, "u", "p", "Camille <camille@archibald.example>")
    msg = envoi.construire(cfg, "a@b.fr", "Objet", "Corps")
    assert msg["List-Unsubscribe"] == "<mailto:camille@archibald.example?subject=stop>" and msg["To"] == "a@b.fr"


def test_journee_complete(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "DATA", tmp_path)
    monkeypatch.setattr(cli, "PROSPECTS", tmp_path / "prospects.csv")
    monkeypatch.setattr(cli, "ENVOIS", tmp_path / "envois.csv")
    monkeypatch.setattr(cli, "MAX_PAR_JOUR", 2)
    rows, _ = crm.merge([], [
        sources.parse_annuaire(ANNUAIRE_RESULT) | {"email": "a@exemple.fr", "telephone": "04 00 00 00 01"},
        sources.parse_annuaire(ANNUAIRE_RESULT | {"siren": "900000003"}) | {"email": "b@exemple.fr"},
        sources.parse_annuaire(ANNUAIRE_RESULT | {"siren": "900000004"}) | {"email": "c@exemple.fr"},
        sources.parse_annuaire(ANNUAIRE_RESULT | {"siren": "900000005"}) | {"telephone": "04 00 00 00 05"},
    ])
    crm.save(cli.PROSPECTS, rows)

    cli.main(["jour"])  # essai : rien ne part, rien ne change
    assert all(r["statut"] == "a_contacter" for r in crm.load(cli.PROSPECTS))

    sent = []

    class FakeSender:
        def __init__(self, cfg): pass
        def __enter__(self): return self
        def __exit__(self, *e): pass
        def envoyer(self, to, sujet, corps): sent.append(to)

    monkeypatch.setattr(envoi, "Expediteur", FakeSender)
    monkeypatch.setattr(envoi, "heure_ok", lambda now: True)
    monkeypatch.setattr(envoi.SmtpConfig, "from_env", classmethod(lambda c: envoi.SmtpConfig("h", 587, "u", "p", "x@y.fr")))
    cli.main(["jour", "--vraiment", "--pause", "0"])
    assert len(sent) == 2  # plafond respecté
    cli.main(["jour", "--vraiment", "--pause", "0"])
    assert len(sent) == 2  # plafond du jour déjà atteint : rien de plus
    after = {r["siren"]: r for r in crm.load(cli.PROSPECTS)}
    assert sum(r["statut"] == "email_1" for r in after.values()) == 2
    assert after["900000005"]["statut"] == "a_contacter"  # pas d'e-mail : il est dans les appels
    calls = list(tmp_path.glob("appels-*.md"))
    assert calls and "900000005" not in calls[0].read_text() and "Maisons Exemple" in calls[0].read_text()

    cli.main(["marquer", "900000003", "demo", "RDV jeudi 8h"])
    assert crm.load(cli.PROSPECTS)[0]  # fichier toujours lisible
    r = {x["siren"]: x for x in crm.load(cli.PROSPECTS)}["900000003"]
    assert r["statut"] == "demo" and "RDV jeudi 8h" in r["notes"]
