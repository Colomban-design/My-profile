"""Données métier : entreprise cliente, lead, fiche projet, devis."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import time
from enum import Enum


class LeadState(str, Enum):
    AWAITING_CONSENT = "attente_accord"   # SMS d'accord envoyé, pas encore de réponse
    LATER = "plus_tard"                   # le client a demandé un autre moment
    QUALIFYING = "qualification"          # conversation en cours
    QUALIFIED = "qualifie"                # fiche envoyée à l'entreprise
    HANDED_OFF = "transfere_humain"       # le client a demandé à parler à quelqu'un
    OPTED_OUT = "stop"                    # le client a répondu STOP


class Classement(str, Enum):
    A_VISITER = "à visiter"
    A_RAPPELER = "à rappeler"
    A_SURVEILLER = "à surveiller"


class QuoteStatus(str, Enum):
    ENVOYE = "envoyé"
    SIGNE = "signé"
    PERDU = "perdu"


# Champs de qualification, dans l'ordre où le script de secours les demande.
QUALIF_FIELDS = (
    "type_travaux",
    "surface_m2",
    "code_postal",
    "delai",
    "budget",
    "financement",
)


@dataclass
class Company:
    """Profil de l'entreprise cliente, paramétré à l'installation."""

    id: str
    nom: str
    dirigeant: str
    tel_dirigeant: str
    email_fiches: str
    metiers: list[str]                       # ex. ["extension", "surélévation", "rénovation globale"]
    departements: list[str]                  # ex. ["69", "01", "38"]
    budget_min: int = 15000                  # en dessous : projet « à surveiller »
    heures_contact: tuple[time, time] = (time(9, 0), time(20, 0))
    jamais_contacter_recommandes: bool = True


@dataclass
class Lead:
    id: str
    company_id: str
    telephone: str
    prenom: str = ""
    source: str = "site"                     # site, google, appel_manque (plateformes : après avis juridique)
    message_initial: str = ""
    recommande: bool = False                 # contact recommandé : pas d'appel IA si l'entreprise l'a choisi
    state: LeadState = LeadState.AWAITING_CONSENT
    canal: str = ""                          # "appel" ou "ecrit" une fois l'accord donné
    creneau_prefere: str = ""
    fields: dict[str, str] = field(default_factory=dict)
    created_at: str = ""


@dataclass
class Fiche:
    lead_id: str
    classement: Classement
    raisons: list[str]
    besoin_architecte: str
    resume: str
    champs: dict[str, str]
