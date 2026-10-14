# Prix : Archibald, l'agent IA pour architectes

> L'outil affiche « $ » : lisez **euros HT par mois** (offre de base). Les panels sont simulés : ils servent à choisir quoi tester, pas à prouver.

## Ce que disent les panels

| panel | offre testée | adhésion | fourchette acceptable | point d'indifférence | médianes (trop bas / bonne affaire / cher / trop cher) |
|---|---|---|---|---|---|
| **v1** : 100 architectes (`panel/`) | 79 € + téléphone 30 €, réseau inclus, fourchette d'honoraires montrée au client | **20 %** | 15 à 70 € | 38,8 € | 15 / 29 / 50 / 90 € |
| **v2** : 40 architectes (`panel-v2/`) | **39 €** + téléphone 19 €, mode « prise de brief », réseau optionnel, RGPD, « avis de l'Ordre demandé » | **22 %** | 10 à 50 € | 24,9 € | 9 / 19 / 39 / 60 € |
| Clients finaux : 20 particuliers (`panel-clients/`) | gratuit pour eux | **75 %** l'utiliseraient | — | — | — |

**Ce que ça veut dire :**
- **Diviser le prix par deux n'a presque rien changé (20 % → 22 %).** Le prix n'est pas le frein principal : seulement 2 refus sur 31 portent sur le prix en v2. Les refus viennent du **besoin** (17 : « je n'ai pas de flux de demandes à trier ») et de la **confiance** (12).
- **Le marché se coupe en deux, dans les deux panels :**
  - ceux qui **reçoivent des demandes froides** : technophiles (58 % et 60 %), noyés sous les demandes (17 % puis 43 %), carnets vides qui veulent le réseau (67 % et 50 %) ;
  - ceux qui **vivent du bouche-à-oreille** : 0 % dans les deux panels, quel que soit le prix.
- Les petits libéraux demandent spontanément **un prix à l'usage** (« quelques euros par brief ») ou un forfait à 15-20 €.

## Ce dont l'entreprise a besoin (`cfo.md`)

| prix | marge par abonné | point mort | année 1 |
|---|---:|---:|---:|
| 29 € | 8 € | 469 abonnés | -33 760 € |
| **39 €** | **18 €** | **209 abonnés** | **-19 710 €** |
| 49 € | 28 € | 134 abonnés | -5 660 € |
| 59 € | 38 € | 99 abonnés | +8 390 € |

## 1. Le prix recommandé : une échelle à deux marches

| formule | pour qui | prix | contenu |
|---|---|---|---|
| **À la demande** | les libéraux qui reçoivent peu de demandes, et **les carnets vides qui veulent le réseau** | **0 €/mois + 5 € HT par brief reçu** (plafond 35 €/mois) | l'agent sur le site, le lien, le brief PDF privé, le réseau optionnel |
| **Agence** | les agences et libéraux qui reçoivent des demandes froides chaque semaine | **39 € HT/mois**, briefs illimités | le même contenu, plus le message de refus personnalisé, plus le tableau de bord mensuel « heures économisées » |
| Option téléphone | ceux qui ratent des appels en chantier | **+15 € HT/mois** | prise de message et résumé, sans questionnaire si l'architecte le souhaite |

**Pourquoi cette échelle :**
1. **Elle répond à l'objection n°1 (« je n'ai pas assez de demandes »).** On ne paie que ce qu'on reçoit. Le plafond à 35 € pousse naturellement les gros utilisateurs vers la formule Agence.
2. **Elle résout le démarrage à froid du réseau.** Les architectes au carnet vide (ceux qui **reçoivent** les demandes déclinées) entrent sans frais fixes. Ils sont l'offre du réseau ; les agences débordées (celles qui **envoient**) sont la demande.
3. **39 € reste le prix d'ancrage** : c'est le point d'indifférence du panel v1 (38,8 €), dans la fourchette acceptable du v2 (≤ 50 €), et le minimum vital selon le CFO.
4. **On ne descend pas sous 39 € pour l'offre Agence**, et on ne vend pas « moins cher qu'un standard IA ». On vend « une soirée récupérée par mois ».

## 2. Ce qu'il faut tester en premier

- **Test A (pilote, 30 jours)** : sur 20 agences, comparer l'affichage de « 39 € » à celui de « 49 € avec le téléphone inclus ». Mesurer la conversion de l'essai vers le payant.
- **Test B** : chez les libéraux, mesurer le taux d'activation de la formule à la demande et le nombre moyen de briefs par mois. Si la moyenne dépasse 7 briefs, la formule rapporte plus que 35 €… mais elle est plafonnée, donc on vérifie qu'elle reste rentable (coût d'environ 0,50 € par brief).
- **Ne pas tester** : une commission sur les projets transmis (rejetée pour raisons de déontologie dans trois versions), ni un prix sous 29 €.

## 3. Ce que le prix ne règle pas

Le prix ne règle ni la confiance (« s'il se trompe, c'est moi qui porte la faute »), ni l'Ordre, ni les données. Ces points se traitent dans l'offre (`offer.md`) et les opérations (`ops.md`), pas dans le tarif.
