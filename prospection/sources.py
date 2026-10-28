"""D'où viennent les prospects : données publiques et API officielles uniquement.

- Annuaire des entreprises (recherche-entreprises.api.gouv.fr) : gratuit, sans clé. SIREN, nom,
  activité (NAF), effectif, adresse, dirigeants. Pas de téléphone ni d'e-mail.
- Google Places (facultatif, clé payante GOOGLE_MAPS_API_KEY) : téléphone, site web, note et
  nombre d'avis, pour les entreprises déjà trouvées.

Pas de scraping de LinkedIn, de Google Maps ou des Pages Jaunes : c'est interdit par leurs
conditions d'utilisation.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request

ANNUAIRE = "https://recherche-entreprises.api.gouv.fr/search"
PLACES = "https://places.googleapis.com/v1/places:searchText"

# Activités visées : celles qui font extension, surélévation et rénovation globale.
NAF = {
    "41.20A": ("Construction de maisons individuelles", 3),
    "43.99C": ("Maçonnerie générale et gros œuvre", 3),
    "41.20B": ("Construction d'autres bâtiments", 2),
    "43.39Z": ("Autres travaux de finition", 1),
    "43.91B": ("Couverture", 1),
}
# Tranches d'effectif INSEE gardées : de 1 à 49 salariés. Les plus intéressantes vont de 6 à 49.
TRANCHES = {"01": "1-2", "02": "3-5", "03": "6-9", "11": "10-19", "12": "20-49"}


class SourceError(RuntimeError):
    pass


def _get_json(url: str, headers: dict | None = None, body: dict | None = None, timeout: int = 20) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "archibald-prospection", **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise SourceError(f"{url.split('?')[0]} a répondu {e.code} : {e.read()[:300]!r}") from e
    except urllib.error.URLError as e:
        raise SourceError(f"{url.split('?')[0]} injoignable : {e.reason}") from e


def parse_annuaire(result: dict) -> dict:
    """Une entreprise de l'annuaire → une ligne de prospect. Tolère les champs absents."""
    siege = result.get("siege") or {}
    dirigeant = next((d for d in result.get("dirigeants") or [] if d.get("type_dirigeant", "personne physique") == "personne physique"
                      and d.get("prenoms")), None)
    prenom = (dirigeant or {}).get("prenoms", "").split(" ")[0].title()
    nom = (dirigeant or {}).get("nom", "").title()
    naf = siege.get("activite_principale") or result.get("activite_principale") or ""
    return {
        "siren": result.get("siren", ""),
        "entreprise": (result.get("nom_raison_sociale") or result.get("nom_complet") or "").title(),
        "dirigeant": f"{prenom} {nom}".strip(),
        "prenom_dirigeant": prenom,
        "qualite": (dirigeant or {}).get("qualite", ""),
        "naf": naf,
        "activite": NAF.get(naf, ("", 0))[0],
        "effectif": TRANCHES.get(siege.get("tranche_effectif_salarie") or result.get("tranche_effectif_salarie") or "", ""),
        "adresse": siege.get("adresse", ""),
        "code_postal": siege.get("code_postal", ""),
        "commune": (siege.get("libelle_commune") or "").title(),
        "creation": result.get("date_creation", ""),
        "source": "annuaire-entreprises",
    }


def annuaire(departements: list[str], naf: list[str] | None = None, maximum: int = 300, pause: float = 0.25) -> list[dict]:
    """Entreprises actives des départements donnés, pour les activités visées."""
    rows: dict[str, dict] = {}
    for dep in departements:
        for code in naf or list(NAF):
            page = 1
            while len(rows) < maximum:
                params = {"activite_principale": code, "departement": dep, "etat_administratif": "A",
                          "tranche_effectif_salarie": ",".join(TRANCHES), "per_page": 25, "page": page}
                data = _get_json(f"{ANNUAIRE}?{urllib.parse.urlencode(params)}")
                if "results" not in data:
                    raise SourceError(f"Réponse inattendue de l'annuaire (clés : {sorted(data)}). Rien n'a été écrit.")
                for res in data["results"]:
                    row = parse_annuaire(res)
                    if row["siren"]:
                        rows.setdefault(row["siren"], row)
                if page >= int(data.get("total_pages") or 1) or not data["results"]:
                    break
                page += 1
                time.sleep(pause)  # l'API limite le nombre d'appels par seconde
    return list(rows.values())[:maximum]


FIELD_MASK = "places.displayName,places.nationalPhoneNumber,places.websiteUri,places.formattedAddress,places.rating,places.userRatingCount"


def parse_place(place: dict) -> dict:
    return {
        "telephone": place.get("nationalPhoneNumber", ""),
        "site": place.get("websiteUri", ""),
        "note_google": str(place.get("rating", "")),
        "avis_google": str(place.get("userRatingCount", "")),
    }


def places(entreprise: str, commune: str, api_key: str) -> dict | None:
    """Fiche Google de l'entreprise (téléphone, site, avis), ou None si rien de fiable."""
    data = _get_json(PLACES, headers={"Content-Type": "application/json", "X-Goog-Api-Key": api_key,
                                      "X-Goog-FieldMask": FIELD_MASK},
                     body={"textQuery": f"{entreprise} {commune}", "languageCode": "fr", "regionCode": "FR", "pageSize": 1})
    found = (data.get("places") or [None])[0]
    if not found:
        return None
    name = (found.get("displayName") or {}).get("text", "").lower()
    # On garde seulement si le nom trouvé ressemble à l'entreprise cherchée (évite les homonymes).
    words = [w for w in entreprise.lower().replace("-", " ").split() if len(w) > 3 and w not in ("sarl", "sas", "eurl", "sasu")]
    if words and not any(w in name for w in words):
        return None
    return parse_place(found)
