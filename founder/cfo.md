# Note du CFO : Archibald, l'agent IA pour architectes

> L'outil affiche « $ » et « a day » : lisez **euros HT** et **par mois**. Une unité = un abonné pendant un mois. Toutes les hypothèses sont des ESTIMATIONS, détaillées dans `cfo-sources.md`. Ce n'est pas un conseil financier, fiscal ou juridique : faites valider par un expert-comptable.

- **La marge par abonné.** À 39 € HT par mois, il reste **18 € (46 %)** après l'IA, l'hébergement, le support, l'encaissement et l'acquisition amortie. Sans l'acquisition, la marge brute logicielle est d'environ **72 %** (28 € sur 39 €).
- **Le point mort : 209 abonnés actifs.** C'est environ 0,7 % des 29 500 architectes, ou 2 à 3 % du segment qui reçoit des demandes froides (voir `pricing.md`).
- **L'année 1 perd 19 710 €.** Le fondateur est payé au minimum. Il faut **32 300 € de trésorerie** avant que l'activité ne s'autofinance. L'équilibre mensuel arrive au mois 11, avec 235 abonnés.
- **La ligne à surveiller : l'acquisition (10 € par mois et par abonné).** Elle suppose 250 € par abonné et 25 mois de durée de vie, donc une attrition de 4 % par mois. Si l'attrition monte à 8 %, la durée de vie tombe à 12 mois, l'acquisition passe à 21 €, et la marge par abonné tombe à 7 €. **Le taux de résiliation est le chiffre qui décide de tout.**
- **Leviers chiffrés avec l'outil :**
  1. **Prix à 49 €** : l'année 1 passe à -5 660 € et le point mort tombe à 134 abonnés. Mais 49 € se rapproche du plafond du re-test (50 €).
  2. **Prix à 29 €** : l'année 1 passe à -33 760 € et le point mort monte à 469 abonnés. **Il ne faut pas descendre** sous 39 € pour l'offre agence.
  3. **L'option téléphone (+15 €, environ 3 € de minutes)** : avec 30 % de souscripteurs, le revenu moyen par abonné monte d'environ 3,6 € par mois, ce qui rapproche du scénario à 49 € sans toucher au prix affiché.
  4. **Le réseau comme acquisition** : chaque demande transmise montre Archibald à un confrère. Si le réseau fait baisser le coût d'acquisition de 250 € à 150 €, la marge passe à 22 € par abonné.
- **Pour l'ambition « très grosse entreprise » :** à 39 €, 10 000 abonnés (un tiers des architectes) font 4,7 M€ de revenu récurrent annuel. Le chiffre est sain, mais ce n'est pas une licorne. Le levier est ailleurs (voir `summary.md`).

# Unit economics: Archibald : assistant d'accueil IA pour agences d'architecture, avec réseau de renvoi entre confrères (France)

Every number below comes from the input file. Nothing is looked up or guessed.

## One abonné-mois (volumes = abonnés actifs PAR MOIS)

| line | per abonné-mois (volumes = abonnés actifs PAR MOIS) |
| --- | ---: |
| Price | $39.00 |
| IA (LLM) : ~30 conversations + briefs par mois x 0,10 EUR (ESTIMATION) | -$3.00 |
| Hébergement France/UE, stockage, envoi des PDF (ESTIMATION) | -$2.00 |
| Support et paramétrage : ~10 min par abonné et par mois x 30 EUR/h (ESTIMATION) | -$5.00 |
| Frais d'encaissement ~2,5 % (ESTIMATION) | -$1.00 |
| Acquisition amortie : 250 EUR par abonné / 25 mois de durée de vie (attrition 4 %/mois) (ESTIMATION) | -$10.00 |
| **Contribution** (what each abonné-mois (volumes = abonnés actifs PAR MOIS) leaves to pay the fixed costs) | **$18.00** (46%) |

## The margin that matters

Fixed costs: $3,750 a month (Rémunération fondateur (minimum, ESTIMATION) $2,500, Contenu, Instagram, salons et événements locaux (ESTIMATION) $500, Outils, monitoring, CRM, hébergement de base (ESTIMATION) $300, Expert-comptable + banque (ESTIMATION) $250, Assurance RC pro éditeur + DPO externe mutualisé (ESTIMATION) $200).

- **Break-even: 209 abonné-mois (volumes = abonnés actifs PAR MOIS)s a day.** Below that you lose money every month.
- **Profit margin at your plan** (300 a day): **14%** of every sale, after every cost.

## Year 1, month by month

| month | abonné-mois (volumes = abonnés actifs PAR MOIS)s a day | revenue | profit | cumulative (after $11,000 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 10 | $390 | -$3,570 | -$14,570 |
| 2 | 20 | $780 | -$3,390 | -$17,960 |
| 3 | 35 | $1,365 | -$3,120 | -$21,080 |
| 4 | 50 | $1,950 | -$2,850 | -$23,930 |
| 5 | 70 | $2,730 | -$2,490 | -$26,420 |
| 6 | 90 | $3,510 | -$2,130 | -$28,550 |
| 7 | 115 | $4,485 | -$1,680 | -$30,230 |
| 8 | 140 | $5,460 | -$1,230 | -$31,460 |
| 9 | 170 | $6,630 | -$690 | -$32,150 |
| 10 | 200 | $7,800 | -$150 | -$32,300 |
| 11 | 235 | $9,165 | $480 | -$31,820 |
| 12 | 270 | $10,530 | $1,110 | -$30,710 |

- **Year 1 operating profit: -$19,710** on $54,795 of revenue.
- After the $11,000 startup spend: -$30,710.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$32,300**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 14% | 209 | -$19,710 |
| Price -10% | 5% | 266 | -$25,190 |
| Volume -20% | 6% | 209 | -$24,768 |
| Unit costs +15% | 6% | 253 | -$24,136 |

## Red flags

- Year 1 loses money on operations (-$19,710).
- The startup spend is not earned back within year 1.
