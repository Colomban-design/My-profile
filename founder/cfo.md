# Note du CFO : Archibald Rénov

> L'outil affiche « $ » et « a day » : lisez **euros HT** et **par mois**. Une unité = une entreprise cliente active pendant un mois. Toutes les hypothèses sont des ESTIMATIONS (détail dans `cfo-sources.md`). Ce n'est pas un conseil financier, fiscal ou juridique : faites valider par un expert-comptable.

- **La marge.** À 149 € par mois, il reste **68,55 € par client (46 %)**. C'est après la voix IA, les SMS de consentement, le support, l'encaissement, l'acquisition amortie (600 € sur 24 mois) et la garantie chantier (5 % du chiffre d'affaires).
- **Le point mort : 58 clients.**
- **L'année 1 est presque à l'équilibre : +2 984 €**, avec une rampe de 5 à 140 clients et le fondateur payé au minimum. La trésorerie nécessaire est de **28 760 €**. Les 15 000 € de démarrage ne sont pas remboursés en année 1.
- **Les lignes à surveiller :**
  1. **Les minutes de voix** (18 € par client). Si un client traite 3 fois plus de leads, la marge fond. C'est pourquoi l'option volume existe (`pricing.md`).
  2. **L'acquisition** (600 € par client). Elle n'est pas mesurée. Le canal « têtes de réseau » peut la diviser par 3 à 5.
  3. **Les 20 pilotes à 99 €** (non modélisés) coûtent environ 50 € par mois de marge chacun pendant un an, soit environ 12 000 € de manque à gagner. C'est le prix de la preuve.
- **Leviers chiffrés avec l'outil :**

| scénario | point mort | année 1 |
|---|---:|---:|
| **Base, 149 €** | **58 clients** | **+2 984 €** |
| Prix 119 € | 103 clients | -19 066 € |
| Prix 199 € | 34 clients | +39 734 € |
| Volume ×0,6 (rampe à 84 clients au mois 12) | 58 clients | -17 169 € (trésorerie 35 332 €) |

- **Ce qu'il ne faut pas faire : descendre sous 149 €** pour l'offre Commercial. À 119 €, il faut presque deux fois plus de clients.
- **Ce qui rend la thèse grande.** À 149 € (ou 119 € via les réseaux), 2 000 clients font environ 3,5 M€ de revenu annuel récurrent, et 10 000 clients environ 18 M€. La suite naturelle : d'autres métiers à leads chers (pompes à chaleur et photovoltaïque, piscines, cuisines, menuiseries), puis la donnée « quel lead signe » vendue sous forme de conseil d'achat de leads.

# Unit economics: Archibald Rénov : commercial IA des entreprises de rénovation (rappel < 60 s, pré-qualification, relance des devis)

Every number below comes from the input file. Nothing is looked up or guessed.

## One client-mois (volumes = entreprises clientes actives PAR MOIS)

| line | per client-mois (volumes = entreprises clientes actives PAR MOIS) |
| --- | ---: |
| Price | $149.00 |
| Minutes de voix IA : ~60 leads x 3 min x 0,10 EUR (ESTIMATION) | -$18.00 |
| IA texte, SMS et e-mails de relance (ESTIMATION) | -$8.00 |
| SMS de consentement et preuve conservée 3 ans (ESTIMATION) | -$3.00 |
| Hébergement France, enregistrements, intégrations CRM (ESTIMATION) | -$4.00 |
| Support et paramétrage : ~30 min/mois x 25 EUR/h (ESTIMATION) | -$12.00 |
| Frais d'encaissement ~2 % (ESTIMATION) | -$3.00 |
| Acquisition amortie : 600 EUR par client / 24 mois (ESTIMATION) | -$25.00 |
| Garantie chantier : 5 % du CA remboursé (ESTIMATION) | -$7.45 |
| **Contribution** (what each client-mois (volumes = entreprises clientes actives PAR MOIS) leaves to pay the fixed costs) | **$68.55** (46%) |

## The margin that matters

Fixed costs: $3,950 a month (Rémunération fondateur (minimum, ESTIMATION) $2,500, Salons, démos, contenu (ESTIMATION) $600, Outils, monitoring, téléphonie de base (ESTIMATION) $400, Expert-comptable, banque, RC pro, DPO (ESTIMATION) $450).

- **Break-even: 58 client-mois (volumes = entreprises clientes actives PAR MOIS)s a day.** Below that you lose money every month.
- **Profit margin at your plan** (150 a day): **28%** of every sale, after every cost.

## Year 1, month by month

| month | client-mois (volumes = entreprises clientes actives PAR MOIS)s a day | revenue | profit | cumulative (after $15,000 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 5 | $745 | -$3,607 | -$18,607 |
| 2 | 10 | $1,490 | -$3,264 | -$21,872 |
| 3 | 18 | $2,682 | -$2,716 | -$24,588 |
| 4 | 27 | $4,023 | -$2,099 | -$26,687 |
| 5 | 37 | $5,513 | -$1,414 | -$28,101 |
| 6 | 48 | $7,152 | -$660 | -$28,760 |
| 7 | 60 | $8,940 | $163 | -$28,597 |
| 8 | 75 | $11,175 | $1,191 | -$27,406 |
| 9 | 90 | $13,410 | $2,220 | -$25,186 |
| 10 | 105 | $15,645 | $3,248 | -$21,939 |
| 11 | 120 | $17,880 | $4,276 | -$17,663 |
| 12 | 140 | $20,860 | $5,647 | -$12,016 |

- **Year 1 operating profit: $2,984** on $109,515 of revenue.
- After the $15,000 startup spend: -$12,016.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$28,760**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 28% | 58 | $2,984 |
| Price -10% | 20% | 74 | -$7,967 |
| Volume -20% | 24% | 58 | -$7,093 |
| Unit costs +15% | 20% | 70 | -$5,885 |

## Red flags

- The startup spend is not earned back within year 1.
