# Prix : ArchiMatch

> Note de lecture : les outils affichent « $ » ; ici, côté architectes les montants sont des **pourcentages de commission**, côté clients des **euros**. Panels simulés : ils servent à choisir quoi tester, pas à prouver.

## Ce que disent les acheteurs simulés

**Architectes (50 réponses, `pricing-curve.md`)**
- Fourchette acceptable : **2 % à 8 %** des honoraires. Point d'indifférence (IPP) : **4 %**. Médianes : trop bas 2 %, bonne affaire 4 %, cher 6 %, trop cher 10 %.
- **Les 8 % pitchés sont pile à la limite haute (PME)** : 13 architectes sur 50 ont mis 8 % comme « je n'achète pas ».

**Déposants (14 réponses exploitables sur 20, `pricing-curve-clients.md`)** — s'il fallait payer le cadrage + 3 architectes :
- Fourchette acceptable : **30 € à 250 €**, IPP **90 €**. Médianes : bonne affaire 50 €, cher 150 €.

## Ce que font les concurrents (`competitors.md`)

0 % (annuaire de l'Ordre) · **7 % + 35 €/mois** (Archidvisor) · 5 à 10 % selon le CNOA. Le client ne paie nulle part.

## Ce dont l'entreprise a besoin (`cfo.md`, outil de l'expert-comptable du pack)

Hypothèse : honoraires moyens de **15 000 € HT** par projet signé (ESTIMATION, projets ciblés ≥ 100 k€ de travaux). Coût variable par projet signé : 310 €.

| commission par projet | ≈ taux sur 15 k€ | marge au plan (20/mois) | point mort | résultat année 1 |
|---|---:|---:|---:|---:|
| 480 € | 3,2 % | -6 % | 24 projets/mois | -32 610 € |
| 600 € | 4 % | 15 % | 14 / mois | -22 170 € |
| **750 €** | **5 %** | **32 %** | **9 / mois** | **-9 120 €** |
| 960 € | 6,4 % | 47 % | 7 / mois | +9 150 € |
| 1 150 € | 7,7 % | 56 % | 5 / mois | +25 680 € |

**La tension centrale :** le taux que les architectes acceptent sans discuter (4 %) ne fait pas vivre l'entreprise ; le taux qui la rend rentable dès l'année 1 (≥ 6,5 %) est celui qu'une majorité refuse.

## 1. Le prix recommandé

**5 % des honoraires HT, plafonné à 1 500 € par projet, facturé en une fois à la signature du contrat d'architecte** (sur la base des honoraires du contrat signé).

Pourquoi :
- 5 % est dans la fourchette acceptable (2-8 %), sous Archidvisor (7 %), et entre le point d'indifférence (4 %) et le seuil « cher » (6 %).
- **Le plafond** répond à l'objection n°1 des architectes établis (« plafonnée ou dégressive sur les gros projets »).
- **Une seule facture à la signature** répond à « usine à gaz administrative » et au contournement (la plateforme ne dépend plus de factures étalées sur 18 mois qu'elle ne voit pas), et règle la trésorerie : sans ça, l'encaissement s'étale sur toute la durée de la mission.
- 0 € si rien n'est signé : pas de paiement à la candidature (le « quand il se positionne » du fondateur est rejeté par le panel : 2 architectes sur 3 paieraient pour rien).

## 2. L'échelle (côté architectes)

| palier | prix | pour qui |
|---|---|---|
| **Essentiel** | 5 % à la signature, plafond 1 500 € | tout architecte inscrit à l'Ordre |
| **Fondateur** (50 premiers d'une ville) | 3 % les 12 premiers mois, plafond 1 000 € | amorçage, en échange d'un retour d'expérience |
| *(plus tard)* **Prioritaire** | abonnement ~49 €/mois + 3 % | agences qui veulent plus de dossiers ; à tester une fois la demande prouvée |

## 3. L'offre d'ouverture

Statut **« Architecte fondateur »** : 3 % plafonnés à 1 000 € pendant 12 mois, réservé aux 50 premiers inscrits de la métropole de lancement, jusqu'au jour d'ouverture publique (date fixée par `/founder-launch`). Vraie limite, vraie date, pas de faux prix barré.

## 4. Ce qu'il faut tester avec de vrais acheteurs

1. **Architectes : 4 % vs 6 %** (plafond 1 500 €) — deux versions de la page d'inscription, envoyées à deux moitiés d'une liste de 200 architectes de la métropole ; mesurer les inscriptions avec acceptation des CGV.
2. **Déposants : gratuit vs « dossier vérifié » à 49 €** — le payant filtre les « touristes » (la plainte n°1 des architectes) et répond à « gratuit = c'est moi qui paie en cachette » ; mesurer dossiers déposés et taux de signature à 60 jours.
3. Vérifier l'hypothèse des **15 000 € d'honoraires moyens** sur les 10 premiers projets signés : c'est la variable la plus fragile du modèle.

## 5. Les objections de prix, mot pour mot (panel architectes)

- « 8 % sur des honoraires déjà serrés, c'est souvent toute ma marge sur une petite mission. » (P010)
- « Sur une extension de maison, mes honoraires couvrent à peine les soirées que je passe sur le permis ; 8 % de ça, c'est ma marge qui part. » (P047)
- « J'ai déjà 3 à 5 demandes par mois sans payer personne ; donner 8 % de mes honoraires, déjà serrés, pour des projets de particuliers dont la moitié n'aboutit pas, ça ne vaut pas le coup. » (P029)

Côté clients, l'objection n'est pas le prix mais la **transparence** : « Gratuit pour moi, ça veut dire que la commission de l'architecte se retrouve dans ses honoraires, donc dans ma facture. » (panel déposants, P001)
