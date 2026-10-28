"""Les messages. Courts, au vouvoiement, écrits pour un dirigeant d'entreprise de rénovation qui
lit ses e-mails sur son téléphone, le soir. Chaque e-mail : une idée, une question, une sortie."""

from __future__ import annotations

import os
from string import Template

SIGNATURE = Template("""$expediteur
$expediteur_titre, Archibald
$expediteur_tel

Vos coordonnées professionnelles viennent de sources publiques (annuaire des entreprises, votre site).
Vous ne souhaitez plus recevoir de message de ma part ? Répondez simplement « stop ».""")

EMAILS = {
    1: ("$entreprise : les demandes de devis du soir",
        """Bonjour $salutation,

Quand un particulier demande un devis sur votre site à 19 h, combien de temps avant que quelqu'un le rappelle ?

Archibald répond à votre place dans la minute : il demande au client s'il accepte d'être rappelé, lui pose les questions que vous poseriez (surface, budget, financement, délai), et vous envoie une fiche prête. Il relance aussi vos devis à J+3, J+10 et J+20. Il ne donne jamais de prix et vous passe la main dès que le client le demande.

Le plus simple est d'essayer sur votre propre téléphone, en 30 secondes :
$lien_demo$code_demo

Je cherche $nb_pilotes entreprises $zone pour un essai gratuit cet hiver. Ça vous parle ?

$signature"""),
    2: ("Re : $entreprise : les demandes de devis du soir",
        """Bonjour $salutation,

Je me permets de revenir vers vous. Une seule question : aujourd'hui, qui relance vos devis envoyés et restés sans réponse ?

Si c'est vous, le soir, Archibald peut le faire à votre place, avec votre nom, et vous dire pourquoi le client hésite (prix, délai, financement).

Dix minutes au téléphone cette semaine pour vous montrer ? Répondez avec un créneau, je m'adapte.

$signature"""),
    3: ("Dernier message — $entreprise",
        """Bonjour $salutation,

Dernier message de ma part, promis. Si le sujet ne vous concerne pas, aucun souci.

Si un jour un lead vous échappe parce que personne n'a pu rappeler à temps, la démo reste ouverte :
$lien_demo$code_demo

Bonne fin de semaine,

$signature"""),
}

APPEL = """# Appel : $entreprise ($commune)

**Interlocuteur :** $dirigeant ($qualite) · **Tél :** $telephone · **Site :** $site
**Contexte :** $activite, $effectif salariés · statut $statut · $notes

1. **Ouverture (10 s)** : « Bonjour $salutation, $expediteur, d'Archibald. Je vous appelle au sujet de vos demandes de devis. Vous avez deux minutes, ou je vous rappelle ce soir ? »
2. **Question (30 s)** : « Quand quelqu'un demande un devis sur votre site le soir ou pendant que vous êtes sur un chantier, qui le rappelle, et en combien de temps ? »
3. **Écouter.** Noter la réponse mot pour mot dans la colonne « notes ».
4. **Si c'est un vrai sujet** : « Je peux vous le montrer sur votre téléphone, là, en 30 secondes. » Envoyer le lien de démo par SMS pendant l'appel, uniquement s'il dit oui.
5. **Proposer** : un essai gratuit pendant l'hiver, sans engagement. Fixer la date du rendez-vous d'installation.

**Objections fréquentes**
- *« Mes clients veulent parler à un humain. »* → Il vous passe la main dès qu'ils le demandent, et l'appel ne se fait que s'ils ont dit oui par SMS.
- *« J'ai déjà trop de demandes. »* → Justement : il trie pour vous (à visiter, à rappeler, à surveiller) et vous ne vous déplacez plus pour rien.
- *« Combien ? »* → 149 € par mois après l'essai, et remboursé si aucun chantier signé n'en vient en 90 jours.
- *« Je n'ai pas le temps. »* → L'installation prend une heure, on la fait pour vous.
"""


def contexte(r: dict, cfg: dict | None = None) -> dict:
    cfg = cfg or {}
    env = os.environ.get
    prenom = r.get("prenom_dirigeant", "")
    ctx = {
        **r,
        "salutation": f"{prenom}" if prenom else "Madame, Monsieur",
        "expediteur": cfg.get("expediteur") or env("PROSPECTION_EXPEDITEUR", "[votre prénom]"),
        "expediteur_titre": cfg.get("expediteur_titre") or env("PROSPECTION_TITRE", "Fondateur"),
        "expediteur_tel": cfg.get("expediteur_tel") or env("PROSPECTION_TEL", ""),
        "lien_demo": cfg.get("lien_demo") or env("PROSPECTION_LIEN_DEMO", "[lien de la démo]"),
        "nb_pilotes": cfg.get("nb_pilotes") or env("PROSPECTION_NB_PILOTES", "5"),
        "zone": cfg.get("zone") or env("PROSPECTION_ZONE", "dans votre région"),
    }
    code = cfg.get("code_demo") or env("PROSPECTION_CODE_DEMO", "")
    ctx["code_demo"] = f" (code : {code})" if code else ""
    for k in ("dirigeant", "qualite", "telephone", "site", "notes", "activite", "effectif", "commune"):
        ctx[k] = ctx.get(k) or "—"
    return ctx


def email(rang: int, r: dict, cfg: dict | None = None) -> tuple[str, str]:
    ctx = contexte(r, cfg)
    ctx["signature"] = SIGNATURE.safe_substitute(ctx).strip()
    sujet, corps = EMAILS[rang]
    return Template(sujet).safe_substitute(ctx), Template(corps).safe_substitute(ctx)


def fiche_appel(r: dict, cfg: dict | None = None) -> str:
    return Template(APPEL).safe_substitute(contexte(r, cfg))
