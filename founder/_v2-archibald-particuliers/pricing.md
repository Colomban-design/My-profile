# Prix : Archibald

> Note : l'outil affiche « $ » ; ici, ce sont des **pourcentages de commission sur les honoraires**. Panels simulés de 20 personnes : ils servent à choisir quoi tester, pas à prouver.

## Ce que disent les panels

| | architectes (`panel/`) | clients, modèle fondateur (`panel-clients/`) | clients, offre retravaillée (`panel-clients-v2/`) |
|---|---|---|---|
| Prix pitché | 10 % | **5 % en plus des honoraires** | **0 %** |
| Adhésion | **40 %** (8 sur 20) | **5 %** (1 sur 20) | **70 %** (14 sur 20) |
| Fourchette acceptable | **2 à 10 %** | **1 à 4 %** | 0,5 à 3 % (s'il fallait payer) |
| Médianes | trop bas 2, bonne affaire 4, cher 7, trop cher 10 | 0,5 / 1 / 3 / 5 | 0,5 / 1 / 2 / 4 |

**Constat principal : les 5 % côté client tuent la demande.** Les clients disent « je paie deux fois » (ils pensent que la commission de l'architecte se retrouve aussi dans sa facture) et « un architecte recommandé par un proche ne me coûte rien ». Avec un service gratuit pour le client, l'adhésion passe de 5 % à 70 %.

**Côté architectes, 10 % est pile à la limite.** Pour 7 architectes sur 20, c'est le seuil « je n'achète pas ». Le séquestre est l'argument qui fait adhérer : 5 des 8 architectes qui adhèrent le citent.

## Concurrents

Personne ne fait payer le client. Archidvisor prend 7 % plus un abonnement côté architecte.

## Ce dont l'entreprise a besoin (`cfo.md`)

Coût variable par mission signée : 406 € (dont 240 € d'acquisition). La base de calcul de la commission décide de tout :

| base et taux | commission par mission | marge au plan (20 missions/mois) | point mort | année 1 |
|---|---:|---:|---:|---:|
| 8 % de 6 000 € (conception seule) | 480 € | -22 % | 42 missions/mois | -40 161 € |
| 6 % de 9 000 € (toute la mission) | 540 € | -13 % | 31/mois | -36 942 € |
| **8 % de 9 000 € (toute la mission)** | **720 €** | **15 %** | **13/mois** | **-21 282 €** |
| 10 % de 9 000 € | 900 € | 32 % | 9/mois | -5 622 € |
| *Modèle du fondateur : 15 % de 6 000 €, volume divisé par 10* | 900 € | -168 % | — | -44 102 € |

## 1. Le prix recommandé

- **Client : 0 %.** Gratuit, avec la garantie « honoraires identiques à ceux pratiqués en direct ».
- **Architecte : 8 % des honoraires qui passent par le séquestre**, sur toute la mission (conception, puis suivi de chantier si l'architecte le fait), prélevés à chaque versement.

Pourquoi :
- 8 % est dans la fourchette acceptable (2 à 10 %), à peine au-dessus d'Archidvisor (7 %) mais **sans abonnement et avec le séquestre en plus**.
- Élargir la base (toute la mission plutôt que la seule conception) rapporte plus qu'augmenter le taux, et pousse à faire passer tous les honoraires par Archibald.
- **La commission n'existe que si l'argent passe par le séquestre.** Elle est donc défendable : elle paie un service visible.

## 2. L'échelle

| palier | prix | pour qui |
|---|---|---|
| **Standard** | 8 % des honoraires séquestrés | tous les architectes |
| **Fondateur** (50 premiers de la ville) | 5 % sur leurs 3 premières missions | amorçage |
| *(plus tard)* **Séquestre seul** | 2 à 3 % pour un architecte qui amène son propre client | utiliser le séquestre comme produit autonome, sans mise en relation |

Le dernier palier est une piste à tester. Les architectes refusent de payer pour des clients, mais ils ont un vrai problème d'impayés : un séquestre utilisable avec leurs propres clients pourrait devenir un produit à part entière.

## 3. L'offre d'ouverture

Le statut fondateur (5 % sur 3 missions) est réservé aux 50 premiers architectes de la ville de lancement, jusqu'à la date d'ouverture publique (`launch.md`).

## 4. Ce qu'il faut tester avec de vrais utilisateurs

1. **Architectes : 8 % contre 10 %** sur les honoraires séquestrés : deux pages d'inscription, en mesurant l'acceptation des conditions générales.
2. **Clients : 0 % contre 2 %** de « frais de séquestre » côté client (la limite haute acceptable). À ne garder que si l'adhésion ne baisse pas de plus de 10 points.
3. **Honoraires moyens réellement séquestrés** sur les 10 premières missions : l'hypothèse des 9 000 € est la plus fragile du modèle.

## 5. Les objections de prix, mot pour mot

- Client : « payer 5 % en plus des honoraires quand l'architecte paie déjà une commission, c'est payer deux fois. » (`panel-clients/`)
- Architecte : « 10 % de mes honoraires de conception, déjà serrés, c'est ma marge. » (`panel/`)
- Architecte : « Je n'aime pas qu'un tiers garde mon argent et décide quand une étape est validée. » (`panel/`)
