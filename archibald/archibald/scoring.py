"""Classement de la fiche : à visiter, à rappeler, à surveiller, avec les raisons.

Règles simples et lisibles, que le dirigeant peut contester : le classement ne
refuse jamais un client, il dit seulement par où commencer.
"""

from __future__ import annotations

import re

from .models import Classement, Company

SEUIL_ARCHITECTE_M2 = 150  # recours à l'architecte obligatoire au-delà (surface de plancher totale)


def parse_int(value: str) -> int | None:
    """« 45 000 € », « 45k », « environ 30 000 » → entier ; sinon None."""
    if not value:
        return None
    t = value.lower().replace(" ", " ").replace("\xa0", " ")
    m = re.search(r"(\d+(?:[ .]\d{3})*(?:[.,]\d+)?)\s*(?:(k|m)(?:€|e)?\b)?", t)
    if not m:
        return None
    number = float(m.group(1).replace(" ", "").replace(".", "").replace(",", "."))
    if m.group(2) == "k":
        number *= 1000
    elif m.group(2) == "m" and number < 100:
        number *= 1_000_000
    return int(number)


def delai_mois(value: str) -> int | None:
    t = value.lower()
    if not t:
        return None
    if any(w in t for w in ("urgent", "vite", "asap", "tout de suite", "dès que possible", "des que possible")):
        return 1
    n = parse_int(t)
    if n is None:
        return None
    if re.search(r"\ban(s|n[ée]es?)?\b", t):
        return n * 12
    if "semaine" in t:
        return max(1, n // 4)
    return n


def financement_solide(value: str) -> bool | None:
    t = value.lower()
    if not t:
        return None
    if any(w in t for w in ("accord", "accordé", "obtenu", "comptant", "apport", "fonds propres", "épargne", "epargne")):
        return True
    if any(w in t for w in ("en cours", "demande", "pas encore", "aucun", "ne sais", "sais pas")):
        return False
    return None


def besoin_architecte(champs: dict[str, str]) -> str:
    surface = parse_int(champs.get("surface_m2", ""))
    existante = parse_int(champs.get("surface_existante_m2", ""))
    if surface is None:
        return "à vérifier (surface inconnue)"
    total = surface + (existante or 0)
    if existante is not None and total > SEUIL_ARCHITECTE_M2:
        return f"oui : surface totale estimée {total} m² > {SEUIL_ARCHITECTE_M2} m²"
    if existante is None:
        return "à vérifier (surface existante inconnue ; architecte obligatoire si le total dépasse 150 m²)"
    return f"non a priori (total estimé {total} m²)"


def classify(company: Company, champs: dict[str, str]) -> tuple[Classement, list[str]]:
    raisons: list[str] = []
    a_surveiller = False
    manquants = [k for k in ("type_travaux", "budget", "delai", "financement", "code_postal") if not champs.get(k)]

    cp = champs.get("code_postal", "")
    if cp and company.departements and cp[:2] not in company.departements:
        a_surveiller = True
        raisons.append(f"hors zone ({cp[:2]})")

    budget = parse_int(champs.get("budget", ""))
    if budget is not None and budget < company.budget_min:
        a_surveiller = True
        raisons.append(f"budget annoncé {budget} € < seuil de {company.budget_min} €")

    mois = delai_mois(champs.get("delai", ""))
    if mois is not None and mois > 12:
        a_surveiller = True
        raisons.append(f"projet à plus de 12 mois ({champs['delai']})")

    if a_surveiller:
        return Classement.A_SURVEILLER, raisons

    fin = financement_solide(champs.get("financement", ""))
    if not manquants and fin is True and (mois is None or mois <= 6):
        raisons.append("budget, financement et délai renseignés")
        raisons.append(f"financement : {champs['financement']}")
        return Classement.A_VISITER, raisons

    if manquants:
        raisons.append("à compléter : " + ", ".join(manquants))
    if fin is False:
        raisons.append(f"financement pas encore sécurisé ({champs.get('financement')})")
    if mois is not None and mois > 6:
        raisons.append(f"délai {champs['delai']}")
    return Classement.A_RAPPELER, raisons or ["informations à confirmer au téléphone"]
