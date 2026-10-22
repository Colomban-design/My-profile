"""Fiche projet envoyée à l'entreprise : texte lisible sur téléphone + export JSON
pour le logiciel de devis ou le CRM (import générique ; connecteurs Obat/Tolteck à brancher)."""

from __future__ import annotations

import json

from .models import Company, Fiche, Lead
from .scoring import besoin_architecte, classify

LABELS = {
    "type_travaux": "Travaux",
    "surface_m2": "Surface des travaux (m²)",
    "surface_existante_m2": "Surface actuelle (m²)",
    "code_postal": "Commune / CP",
    "delai": "Début souhaité",
    "budget": "Budget annoncé",
    "financement": "Financement",
    "photos": "Photos possibles",
}


def build_fiche(company: Company, lead: Lead) -> Fiche:
    classement, raisons = classify(company, lead.fields)
    archi = besoin_architecte(lead.fields)
    resume = ", ".join(f"{LABELS.get(k, k)} : {v}" for k, v in lead.fields.items() if v)
    return Fiche(lead.id, classement, raisons, archi, resume, dict(lead.fields))


def render_text(company: Company, lead: Lead, fiche: Fiche) -> str:
    lines = [
        f"FICHE PROJET — {fiche.classement.value.upper()}",
        f"Client : {lead.prenom or '(prénom non donné)'} — {lead.telephone} — source : {lead.source}",
        f"Pourquoi : {'; '.join(fiche.raisons)}",
        f"Architecte : {fiche.besoin_architecte}",
        "",
    ]
    for key, label in LABELS.items():
        if fiche.champs.get(key):
            lines.append(f"- {label} : {fiche.champs[key]}")
    if lead.creneau_prefere:
        lines.append(f"- Créneau préféré pour le rappel : {lead.creneau_prefere}")
    lines += ["", "Rappel : aucun prix n'a été annoncé au client. Le classement ne refuse personne."]
    return "\n".join(lines)


def export_json(lead: Lead, fiche: Fiche) -> str:
    return json.dumps(
        {
            "lead_id": lead.id,
            "telephone": lead.telephone,
            "prenom": lead.prenom,
            "source": lead.source,
            "classement": fiche.classement.value,
            "raisons": fiche.raisons,
            "besoin_architecte": fiche.besoin_architecte,
            "champs": fiche.champs,
        },
        ensure_ascii=False,
        indent=2,
    )
