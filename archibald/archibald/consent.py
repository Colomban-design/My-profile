"""Messages de consentement et lecture des réponses.

Principe (à faire valider par un avocat avant le premier envoi réel) : Archibald
ne démarche jamais. Il répond à une demande de devis que la personne vient de
faire, et lui demande d'abord par écrit comment elle veut être recontactée.
Chaque étape est enregistrée comme preuve, conservée 3 ans.
"""

from __future__ import annotations

import re
import unicodedata

from .models import Company, Lead

STOP_WORDS = {"stop", "arret", "arreter", "desinscrire", "desabonner", "ne plus me contacter"}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", text.strip().lower())


def is_stop(text: str) -> bool:
    t = normalize(text)
    return t in STOP_WORDS or t.startswith("stop")


def consent_request(company: Company, lead: Lead) -> str:
    bonjour = f"Bonjour {lead.prenom}" if lead.prenom else "Bonjour"
    return (
        f"{bonjour}, ici l'assistant IA de {company.nom}, suite à votre demande de devis. "
        "Pour préparer la visite, on peut : 1) vous appeler maintenant, "
        "2) plus tard (indiquez quand), 3) continuer par écrit ici. "
        "Répondez 1, 2 ou 3. STOP pour ne plus être contacté."
    )


def consent_request_recommended(company: Company, lead: Lead) -> str:
    """Contact recommandé : pas d'appel IA, on propose le rappel du dirigeant ou l'écrit."""
    bonjour = f"Bonjour {lead.prenom}" if lead.prenom else "Bonjour"
    return (
        f"{bonjour}, ici l'assistant IA de {company.nom}. Merci pour votre demande. "
        f"{company.dirigeant} vous rappelle personnellement. Pour gagner du temps, "
        "voulez-vous répondre ici à 3 questions sur votre projet ? Répondez 3 pour oui, "
        "2 pour attendre son appel. STOP pour ne plus être contacté."
    )


def parse_choice(text: str) -> str | None:
    """Retourne "appel", "plus_tard", "ecrit" ou None si la réponse n'est pas claire."""
    t = normalize(text)
    if re.fullmatch(r"1\.?|oui|ok|d'accord|daccord|appelez(-| )moi.*|maintenant.*", t):
        return "appel"
    if re.fullmatch(r"2\.?|plus tard.*|demain.*|ce soir.*|.*(lundi|mardi|mercredi|jeudi|vendredi|samedi|dimanche).*", t):
        return "plus_tard"
    if re.fullmatch(r"3\.?|ecrit.*|par ecrit.*|sms.*|ici.*|par message.*", t):
        return "ecrit"
    return None


def confirm_stop(company: Company) -> str:
    return f"C'est noté, {company.nom} ne vous contactera plus par ce biais. Bonne journée."
