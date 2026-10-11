# Archibald · Business plan

**Verdict: Not yet**

- ✓ Each mission signée via séquestre (volumes = missions PAR MOIS) earns $314.00 before fixed costs (44% contribution).
- ✗ Year 1 operating LOSS: $21,282.
- ✓ 8 of 20 simulated buyers buy (40%, the bar is 25%).

| key number | |
| --- | ---: |
| Price | $720.00 a mission signée via séquestre (volumes = missions PAR MOIS) |
| Profit margin at plan | 15% per mission signée via séquestre (volumes = missions PAR MOIS) |
| Break-even | 13 mission signée via séquestre (volumes = missions PAR MOIS)s a day |
| Year 1 operating profit | $-21,282 |
| Startup spend | $13,000 |
| Cash needed before it pays for itself | $36,262 |
| Startup money earned back | not in year 1 |
| Buyer panel | 8 buy · 12 pass |

## The idea

- Ce que c'est : une marketplace qui digitalise la mise en relation entre particuliers et architectes en France. Un agent IA conversationnel qualifie le projet du client en 5 minutes (budget, PLU, faisabilité, style) et génère un brief PDF professionnel ; un matching relie le projet à l'architecte selon ses compétences réelles (pas sa taille ni sa notoriété) ; un séquestre financier garantit le paiement des honoraires de conception.
- Pour qui : (1) les particuliers qui ont un projet (construction, extension, rénovation) et qui sont « perdus » (budget irréaliste, réglementation incomprise, manque de confiance) ; (2) les architectes, surtout les jeunes indépendants, qui perdent du temps sur des prospects non qualifiés et subissent des impayés.
- Ce qu'on vend, à quel prix : gratuit pour tous à l'inscription ; commission uniquement à la transaction : 5 % payés par le client et 10 % payés par l'architecte, sur les honoraires de conception.
- Où et comment : en ligne, France. Site en ligne, agent conversationnel fonctionnel, brief PDF généré automatiquement, compte Instagram @monprojetarchi lancé.
- Budget et contraintes : budget, équipe et calendrier non communiqués. Une introduction est en cours vers Charlotte Cadé, cofondatrice de Selency.
- Phrase de positionnement du fondateur : « Pas le plus connu. Le plus compatible avec votre projet. »

## Summary

**Ce que c'est.** Archibald est une marketplace qui met en relation des particuliers et des architectes. Un agent IA qualifie le projet en 5 minutes et produit un brief PDF. Un matching propose les architectes selon leurs compétences, pas leur notoriété. Un séquestre garantit le paiement des honoraires. Le site, l'agent et le brief existent déjà.

**Verdict : Not yet (pas encore)**, calculé par `compile.py`. Il repose sur le modèle recommandé (0 % client, 8 % architecte sur les honoraires séquestrés) :
- chaque mission laisse **314 € (44 %)** ;
- le point mort est à **13 missions par mois** ;
- **l'année 1 perd 21 282 €** ;
- il faut **36 262 €** de trésorerie.

**Le modèle actuel (5 % client + 10 % architecte) est le plus fragile.** Dans le panel, les 5 % côté client font tomber l'adhésion à **1 client sur 20**, contre **14 sur 20** quand le service est gratuit. À volume divisé par 10, l'année 1 perd 44 102 €.

**Ce qui doit changer pour passer au vert :**
1. Supprimer les frais client.
2. Faire porter la commission sur **tous les honoraires qui passent par le séquestre** (conception et suivi), pas sur la seule conception.
3. Atteindre environ 900 € par mission (10 % de 9 000 €, année 1 à -5 622 €) ou 30 missions par mois.

**Où le conseil et les panels s'accordent :**
- le **séquestre est la vraie différence** (aucun concurrent trouvé n'en propose) ;
- **la fuite hors plateforme** est le risque n°1 ;
- **les 15 % cumulés sont trop élevés** ;
- il faut **une seule ville**.

**Où ils divergent :**
- le conseil voulait une garantie pour *justifier* les 5 % client ; les panels disent de les *supprimer* ;
- la lentille Monopole croit à l'effet de réseau, la lentille Produit craint que le brief promette trop (PLU).

**Le plus gros risque : le séquestre.** Encaisser des fonds pour le compte de tiers exige un établissement de paiement agréé. Un avocat et le choix du prestataire sont à régler avant le premier euro. Vient ensuite la déontologie de la commission (avis d'avocat, position du CROA).

**Pour démarrer.** Environ 13 000 € (séquestre via un prestataire, juridique, publicité de lancement) et un test de 10 séquestres réels dans une ville avant l'ouverture publique du 1er février 2027 (`launch.md`).

**Cette semaine :**
- choisir la ville ;
- prendre rendez-vous avec un avocat en droit des paiements et en déontologie des architectes ;
- contacter 2 prestataires de paiement agréés pour marketplaces ;
- trouver une source au chiffre « 80 % » ou le retirer du pitch.

*Les panels sont des acheteurs simulés et les chiffres sont des projections. Pas un conseil financier, juridique ou fiscal.*

## What the board said

**Vote : 3 « FUND IF » sur 3. Score moyen : 4,7/10** (Offre 5 · Monopole 4 · Produit 5). Mémos complets dans `board/`.
À comparer avec la première version de l'idée (sans séquestre ni agent existant) : 4/10. Ce qui a remonté la note : **le produit existe déjà** et la phrase de positionnement tient en une ligne.

### Les risques soulevés par plusieurs membres

1. **La fuite hors plateforme (3/3).** Avec 15 % cumulés (5 % client + 10 % architecte), les deux parties ont une forte raison de finir l'affaire en direct après le premier rendez-vous. Le brief et le matching sont livrés *avant* que la commission soit due.
2. **Aucune preuve à ce jour (3/3).** Le nombre de briefs, de mises en relation et de transactions n'est pas communiqué, et le chiffre « 80 % par bouche-à-oreille » n'a pas de source.
3. **Trois produits en un (Produit, Monopole).** Agent IA, matching et séquestre : un seul est démontré (le brief).
4. **Pas de tête de pont (Offre, Monopole).** « France » et un compte Instagram ne suffisent pas à créer de la liquidité locale.
5. **Réglementation (Monopole, Produit).** Une commission de 10 % sur les honoraires face à la déontologie, et un séquestre qui suppose un prestataire de paiement agréé.

### Désaccords à garder

- La lentille Monopole voit un vrai coin de monopole : la donnée projet par projet et l'effet de réseau local. La lentille Produit craint que le brief promette plus qu'il ne tient (PLU, faisabilité) et casse la confiance des deux côtés à la fois.
- La lentille Offre veut une **garantie client** pour justifier les 5 %. Les deux autres demandent plutôt de **posséder ce qui se passe après le match**.

### Conditions (checklist)

- [ ] **Une tête de pont** : une ville et un type de projet, avec un objectif chiffré de densité. → `/founder-marketing`, `/founder-launch`
- [ ] **Un mécanisme anti-fuite prouvé** : mesurer la part des honoraires réellement passée par le séquestre sur les premières missions. → `/founder-launch`
- [ ] **Une acceptation des commissions des deux côtés.** → `/founder-consumer` (fait : voir `panel/` et `panel-clients/`)
- [ ] **La conformité** : déontologie de la commission architecte, et séquestre via un établissement agréé. → `/founder-ops`
- [ ] **Une distribution chiffrée** : un coût d'acquisition inférieur à la commission moyenne. → `/founder-cfo`
- [ ] **Un brief validé par de vrais architectes**, et un agent qui dit ce qu'il ne sait pas. → `/founder-ops`
- [ ] **Un entonnoir instrumenté** : brief → mise en relation → contrat → paiement en séquestre. → `/founder-launch`
- [ ] **La chose unique**, en une phrase. → `/founder-offer`

### La version la plus forte que le conseil voit

Le brief IA comme **porte d'entrée gratuite** pour le client, et le **séquestre comme raison de rester sur la plateforme** pour les deux parties. L'architecte est payé, le client paie au fil des étapes validées. Le tout dans une ville, sur un type de projet (par exemple l'extension de maison), avec un brief relu et validé par des architectes. La commission n'est prélevée qu'à travers le séquestre : elle n'existe que si l'argent passe par Archibald, et c'est ce qui la rend défendable.

## The competition

Mise à jour du 11/10/2026, à partir de la recherche de la v1 (`_v1-archimatch/competitors.md`) complétée sur le séquestre et le nom. **Limite :** les sites des concurrents, Trustpilot et architectes.org étaient injoignables depuis mon environnement. Les faits viennent de la presse et des extraits de moteur de recherche, souvent anciens : revérifiez chaque prix avant de décider.

### 1. Le tableau

| Concurrent | Type | Prix | Ce qu'il fait | Séquestre ? | Source |
|---|---|---|---|---|---|
| **Archidvisor** | Direct | 7 % des honoraires HT + 35 €/mois, payés par l'architecte ; gratuit pour le client | le client compare les candidatures et rencontre « les 3 agences les plus pertinentes » parmi environ 1 250 ; partenaire de l'Ordre ; plus de 10 000 projets en 2020 | non trouvé | [Gust](https://gust.com/companies/archidvisor), [JDE](https://www.lejournaldesentreprises.com/breve/le-bordelais-archidvisor-leve-12-million-deuros-127993), [MySweetImmo](https://www.mysweetimmo.com/2021/02/10/travaux-et-crise-sanitaire-archidvisor-et-ses-architectes-ont-accompagne-plus-de-10-000-projets-en-2020/) |
| **Archibien** | Direct | non publié | une équipe humaine évalue faisabilité et budget, puis organise un mini-concours entre 3 architectes (sur environ 350) | non trouvé | [Europe 1](https://www.europe1.fr/node/710449), [LCL](https://www.lcl.fr/banque-privee/actualites/autres-horizons/la-preuve-par-trois-archibien) |
| **Trouver mon Architecte** | Direct | gratuit pour le client | mise en relation, architectes inscrits à l'Ordre ; actif en 2026 | non trouvé | [Solutions Numériques](https://www.solutions-numeriques.com/?p=63941), [Trustpilot](https://de.trustpilot.com/review/trouver-mon-architecte.fr) |
| **Architectes pour tous** (Ordre) | Direct | gratuit pour tous | annuaire géolocalisé d'environ 4 000 agences | non | [Monimmeuble](https://monimmeuble.com/actualite/architectes-pour-tous-le-service-internet-pour-trouver-son-architecte) |
| **Archionline** | Direct | non publié | architecte + artisans | non trouvé ; plainte d'un architecte payé en retard par la plateforme | [FrenchWeb](https://www.frenchweb.fr/archionline-leve-12-million-deuros-pour-provoquer-le-coup-de-foudre-avec-larchitecte/256980), [Custplace](https://fr.custplace.com/archionline) |
| **Houzz**, **Habitatpresto** | Indirects | Houzz Pro dès 399 € ; Habitatpresto gratuit pour le client | annuaires, devis travaux | non | [JDN](https://www.journaldunet.com/retail/1168330-houzz-strategie-france-adi-tatarko/), [Habitatpresto](https://www.habitatpresto.com/devis-travaux/devis-architecte) |
| **Bouche-à-oreille**, constructeurs, dessinateurs | Substituts | gratuit à forfait | recommandation ; plans sans architecte sous 150 m² | — | [Que Choisir](https://www.quechoisir.org/enquete-architectes-trouver-le-bon-plan-n7715/), [Construires](https://www.construires.fr/architecte/) |

### 2. Fourchette de prix (côté architecte)

0 % (Ordre) · **7 % + abonnement** (Archidvisor) · 5 à 10 % pour les plateformes selon le CNOA ([document 2023](https://www.architectes.org/sites/cnoa/files/2023-09/field_media_document/988-cdp-63-web2.pdf)). **Aucun concurrent trouvé ne fait payer le client.** Archibald, avec 5 % côté client et 10 % côté architecte, serait le plus cher du marché des deux côtés.

### 3. Ce que dit le marché sur le bouche-à-oreille

[Que Choisir](https://www.quechoisir.org/enquete-architectes-trouver-le-bon-plan-n7715/) écrit que le choix d'un architecte se fait « le plus souvent » par recommandation, mais **sans chiffre**. **Je n'ai trouvé aucune source pour « 80 % ».** Citez une source, ou dites « la plupart » ; un investisseur demandera d'où vient ce chiffre.

### 4. Carte de positionnement

Axes : **ce que la plateforme sécurise** (rien → paiement) × **la façon dont elle choisit les architectes** (notoriété ou annuaire → compétences).

```
                 sécurise le paiement (séquestre)
                              |
                              |   • Archibald (visé)
                              |
  annuaire / notoriété ------ + ------ matching par compétences
                              |
  Ordre • Houzz • Trouver mon |  • Archidvisor (3 agences)
  Architecte • Habitatpresto  |  • Archibien (sélection humaine)
                    ne sécurise rien
```

### 5. Les plaintes (toutes minces)

1. Qualité ou qualification du prestataire (Archionline, Archidvisor).
2. Pas de réponse ni de suivi après la mise en relation (Archidvisor).
3. **Un architecte payé en retard par une plateforme** (Archionline) : c'est exactement le risque qu'un séquestre doit éviter, et la preuve qu'il doit être tenu par un tiers agréé.

### 6. Le vide

- **Le séquestre des honoraires.** Je n'ai trouvé aucun concurrent qui sécurise le paiement de l'architecte : c'est la seule vraie différence d'Archibald. Dans les panels, c'est l'élément qui fait adhérer les architectes qui ont déjà eu des impayés, et qui rassure les clients échaudés par un artisan.
- **Le matching par compétences** (« le junior passionné d'ossature bois ») : Archidvisor et Archibien sélectionnent déjà 3 agences, mais sans le revendiquer sur les compétences. C'est une différence de discours, à prouver par le résultat.
- **Le brief IA** : différenciant aujourd'hui, mais copiable en quelques semaines.

### 7. La menace

Archidvisor (trafic, base d'architectes, partenariat avec l'Ordre) peut ajouter un séquestre via Stripe Connect ou Mangopay et un brief IA. Votre avance doit venir de la densité locale et de la confiance (les premiers séquestres réussis), pas de la technologie.

## The buyer panel

**8 buy · 12 pass** (40% buy) out of 20 simulated buyers. Seed 1101, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

### By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Architecte d'une agence plus grosse, orientée marchés publics et promoteurs | 2 | 50%  (thin) |
| Gérant d'une petite agence (2 à 10 personnes) | 5 | 40%  (thin) |
| Architecte libéral seul, installé depuis longtemps | 5 | 40%  (thin) |
| Architecte libéral seul, jeune installé (moins de 5 ans) | 8 | 38% |

### By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Fait ses comptes au centime | 3 | 100%  (thin) |
| Carnet vide, cherche du travail | 4 | 100%  (thin) |
| Déjà inscrit sur des plateformes | 3 | 33%  (thin) |
| Vit du bouche-à-oreille | 5 | 0%  (thin) |
| Sélectif sur les projets | 3 | 0%  (thin) |
| Attaché à la déontologie | 2 | 0%  (thin) |

### By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| under $38,000 | 6 | 50%  (thin) |
| $60,000 and up | 7 | 43%  (thin) |
| $38,000 to $60,000 | 7 | 29%  (thin) |

### Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| habit | 4 | "Mes clients viennent du bouche-à-oreille, j'ai déjà mes soirées remplies de permis de construire et je n'ai jamais payé pour un client. Je n'ai pas besoin d'une plateforme qui me prend 10 % pour des particuliers qui vont me mettre en concurrence avec deux autres agences." (P002) · "Mes clients viennent tous de recommandations, je n'ai jamais payé pour un client et je ne vais pas commencer à lâcher 10 % de mes honoraires de conception à une plateforme. Le séquestre me parle vraiment après mon projet reporté, mais pas au point de changer ma façon de trouver du travail." (P005) |
| price | 3 | "Je gagne déjà à peine ma vie et mes honoraires sont tirés vers le bas ; en céder 10 % à une plateforme, c'est rogner sur des missions déjà serrées. Et des particuliers qui arrivent via une appli, j'ai peur que ce soient justement les petits projets mal payés que je refuse." (P004) · "J'ai déjà assez de demandes, dont la moitié ne mène à rien, et céder 10 % de mes honoraires de conception à une plateforme, c'est trop pour mes marges de libérale seule. Je m'inscrirais peut-être parce que c'est gratuit, mais je ne compterais pas dessus et je refuserais sans doute une mission à ce prix." (P010) |
| values | 2 | "Mon agence vit des marchés publics et des promoteurs, pas des extensions de particuliers ; et une plateforme qui prend 10 % sur mes honoraires pour m'amener un client, ça ressemble furieusement à un apporteur d'affaires, ce que l'Ordre regarde de très près." (P011) · "Reverser 10 % de mes honoraires à une plateforme qui m'amène un client, ça ressemble exactement à un apporteur d'affaires rémunéré, et je ne signe rien de ce genre sans savoir ce qu'en pense l'Ordre. En plus, les particuliers des plateformes veulent surtout un plan gratuit et disparaissent." (P019) |
| trust | 2 | "Je travaille depuis longtemps avec du bouche-à-oreille et des clients que je choisis ; une plateforme inconnue qui garde mes honoraires sur un séquestre et prend 10 % au passage, ce n'est pas pour moi. Et les particuliers qui passent par une marketplace, j'ai peur que ce soient surtout des petits projets à budget irréaliste." (P013) · "Mes clients viennent par recommandation et je n'ai jamais payé pour en avoir un ; je veux bien plus de projets, mais je ne vais pas laisser une plateforme inconnue garder mes honoraires sur un séquestre et m'en prendre 10 % au passage." (P015) |
| quality | 1 | "Je suis installée depuis longtemps, mes clients viennent du bouche-à-oreille et je refuse déjà les petits projets mal payés. Une plateforme de particuliers, c'est surtout des extensions à budget irréaliste, et en plus je devrais lâcher 10 % de mes honoraires." (P008) |

### Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 8 | "Je suis installé depuis peu et j'ai besoin de clients ; l'inscription est gratuite et le séquestre règle mon problème d'impayés, donc je m'inscris pour voir. Mais je prendrai une mission seulement si le brief montre un vrai budget, et je vais vite décrocher si ce sont des curieux." (P001) · "Mon carnet est vide depuis des mois et l'inscription est gratuite, sans abonnement : je ne paie que si je signe une mission, donc je m'inscris et je teste. Le séquestre contre les impayés, c'est un vrai plus pour une petite agence comme la mienne." (P003) |

### What would flip a no

- Une garantie écrite qu'il n'y a pas de mise en concurrence ni d'esquisse gratuite : un client qui a déjà validé son budget et qui me choisit moi seul, avec une commission plus basse, autour de 5 %.
- Une commission plafonnée autour de 5 % et la garantie que les projets proposés ont un budget vérifié et sérieux, pas des petites demandes d'extension à prix cassé.
- Que le client me soit proposé en exclusivité, sans mise en concurrence ni esquisse gratuite, avec un budget vérifié (financement obtenu) avant que je le rencontre.
- Une commission autour de 5 % et des retours concrets d'architectes de mon groupe WhatsApp qui ont réellement signé des missions sérieuses via Archibald.
- Des collègues de mon groupe WhatsApp qui me disent avoir signé via Archibald des missions sérieuses avec des budgets réalistes et des honoraires effectivement versés au séquestre.
- Une commission autour de 5 % et la preuve que les clients sont vraiment qualifiés (budget réaliste, projet faisable), avec un déblocage des fonds automatique si le client ne réagit pas sous quelques jours.
- Un avis écrit du Conseil national de l'Ordre validant le modèle de commission, plus des projets de taille suffisante pour une agence comme la mienne.
- Un séquestre tenu par un établissement reconnu (banque ou CARPA-type) avec des règles de déblocage claires, plus la preuve que les projets proposés ont des budgets sérieux, et une commission plus basse autour de 5 %.
- Que des confrères de mon groupe WhatsApp me disent qu'ils ont signé de vraies missions rentables via Archibald, avec des clients sérieux qu'ils n'auraient pas eus autrement.
- Un séquestre tenu par un tiers régulé (banque ou notaire) avec des règles de déblocage écrites, et un confrère que je connais qui me dise qu'il a eu de vrais projets payés par là.
- Une commission autour de 5 %, et la preuve que le séquestre est versé avant que je travaille, donc que le client a réellement l'argent.
- Un avis écrit du Conseil de l'Ordre des architectes confirmant que le modèle est conforme, et des confrères de mon groupe WhatsApp qui ont réellement signé des missions payées via la plateforme.

Buyers say they would buy **1.0 times** in the first month on average.

20 buyers gave all four price answers. Run founder-pricing's van_westendorp.py on the answers folder.

## Pricing

> Note : l'outil affiche « $ » ; ici, ce sont des **pourcentages de commission sur les honoraires**. Panels simulés de 20 personnes : ils servent à choisir quoi tester, pas à prouver.

### Ce que disent les panels

| | architectes (`panel/`) | clients, modèle fondateur (`panel-clients/`) | clients, offre retravaillée (`panel-clients-v2/`) |
|---|---|---|---|
| Prix pitché | 10 % | **5 % en plus des honoraires** | **0 %** |
| Adhésion | **40 %** (8 sur 20) | **5 %** (1 sur 20) | **70 %** (14 sur 20) |
| Fourchette acceptable | **2 à 10 %** | **1 à 4 %** | 0,5 à 3 % (s'il fallait payer) |
| Médianes | trop bas 2, bonne affaire 4, cher 7, trop cher 10 | 0,5 / 1 / 3 / 5 | 0,5 / 1 / 2 / 4 |

**Constat principal : les 5 % côté client tuent la demande.** Les clients disent « je paie deux fois » (ils pensent que la commission de l'architecte se retrouve aussi dans sa facture) et « un architecte recommandé par un proche ne me coûte rien ». Avec un service gratuit pour le client, l'adhésion passe de 5 % à 70 %.

**Côté architectes, 10 % est pile à la limite.** Pour 7 architectes sur 20, c'est le seuil « je n'achète pas ». Le séquestre est l'argument qui fait adhérer : 5 des 8 architectes qui adhèrent le citent.

### Concurrents

Personne ne fait payer le client. Archidvisor prend 7 % plus un abonnement côté architecte.

### Ce dont l'entreprise a besoin (`cfo.md`)

Coût variable par mission signée : 406 € (dont 240 € d'acquisition). La base de calcul de la commission décide de tout :

| base et taux | commission par mission | marge au plan (20 missions/mois) | point mort | année 1 |
|---|---:|---:|---:|---:|
| 8 % de 6 000 € (conception seule) | 480 € | -22 % | 42 missions/mois | -40 161 € |
| 6 % de 9 000 € (toute la mission) | 540 € | -13 % | 31/mois | -36 942 € |
| **8 % de 9 000 € (toute la mission)** | **720 €** | **15 %** | **13/mois** | **-21 282 €** |
| 10 % de 9 000 € | 900 € | 32 % | 9/mois | -5 622 € |
| *Modèle du fondateur : 15 % de 6 000 €, volume divisé par 10* | 900 € | -168 % | — | -44 102 € |

### 1. Le prix recommandé

- **Client : 0 %.** Gratuit, avec la garantie « honoraires identiques à ceux pratiqués en direct ».
- **Architecte : 8 % des honoraires qui passent par le séquestre**, sur toute la mission (conception, puis suivi de chantier si l'architecte le fait), prélevés à chaque versement.

Pourquoi :
- 8 % est dans la fourchette acceptable (2 à 10 %), à peine au-dessus d'Archidvisor (7 %) mais **sans abonnement et avec le séquestre en plus**.
- Élargir la base (toute la mission plutôt que la seule conception) rapporte plus qu'augmenter le taux, et pousse à faire passer tous les honoraires par Archibald.
- **La commission n'existe que si l'argent passe par le séquestre.** Elle est donc défendable : elle paie un service visible.

### 2. L'échelle

| palier | prix | pour qui |
|---|---|---|
| **Standard** | 8 % des honoraires séquestrés | tous les architectes |
| **Fondateur** (50 premiers de la ville) | 5 % sur leurs 3 premières missions | amorçage |
| *(plus tard)* **Séquestre seul** | 2 à 3 % pour un architecte qui amène son propre client | utiliser le séquestre comme produit autonome, sans mise en relation |

Le dernier palier est une piste à tester. Les architectes refusent de payer pour des clients, mais ils ont un vrai problème d'impayés : un séquestre utilisable avec leurs propres clients pourrait devenir un produit à part entière.

### 3. L'offre d'ouverture

Le statut fondateur (5 % sur 3 missions) est réservé aux 50 premiers architectes de la ville de lancement, jusqu'à la date d'ouverture publique (`launch.md`).

### 4. Ce qu'il faut tester avec de vrais utilisateurs

1. **Architectes : 8 % contre 10 %** sur les honoraires séquestrés : deux pages d'inscription, en mesurant l'acceptation des conditions générales.
2. **Clients : 0 % contre 2 %** de « frais de séquestre » côté client (la limite haute acceptable). À ne garder que si l'adhésion ne baisse pas de plus de 10 points.
3. **Honoraires moyens réellement séquestrés** sur les 10 premières missions : l'hypothèse des 9 000 € est la plus fragile du modèle.

### 5. Les objections de prix, mot pour mot

- Client : « payer 5 % en plus des honoraires quand l'architecte paie déjà une commission, c'est payer deux fois. » (`panel-clients/`)
- Architecte : « 10 % de mes honoraires de conception, déjà serrés, c'est ma marge. » (`panel/`)
- Architecte : « Je n'aime pas qu'un tiers garde mon argent et décide quand une étape est validée. » (`panel/`)

## The offer

Ce document part du pitch du fondateur (`pitch-clients-v1.md`, `pitch-architectes.md`) et des panels (`panel/`, `panel-clients/`, `panel-clients-v2/`), avec la méthode de la lentille Offre.

### 1. Les obstacles, dans les mots des panels

**Côté clients**
1. « Payer 5 % en plus, c'est payer deux fois. »
2. « Un architecte recommandé par un proche ne me coûte rien. »
3. « L'algorithme me propose ceux qui paient, pas les meilleurs. »
4. « Je préfère parler à un humain qu'à une IA. »
5. « Mon banquier veut des devis. »
6. « Ai-je vraiment besoin d'un architecte ? »
7. « Je vais être harcelé de coups de fil. »
8. « Je ne sais pas ce que coûte un architecte. »
9. « Qui tient l'argent du séquestre ? »
10. « Le séquestre ne couvre pas le chantier, là où je me suis fait avoir. »

**Côté architectes**

11. « 10 %, c'est ma marge. »
12. « Je n'ai jamais payé pour un client. »
13. « Le budget du client sera irréaliste. »
14. « Je ferai une esquisse gratuite contre deux confrères. »
15. « Un tiers garde mon argent et décide si l'étape est validée. »
16. « Est-ce compatible avec la déontologie ? »
17. « Le PLU lu par une IA sera faux. »

### 2. Ce qu'on garde, ce qu'on retire

| décision | répond à |
|---|---|
| **Supprimer les 5 % côté client** (client : 5 % → 70 % d'adhésion) | 1, 2 |
| **« Honoraires garantis identiques à ceux pratiqués en direct »**, écrit dans le contrat architecte | 1, 3 |
| **Critères de matching publiés, aucun architecte ne paie pour être proposé** | 3 |
| **Un humain rappelle sous 48 h**, mais **seulement si le client le demande** (un client du panel a relevé la contradiction avec « personne ne vous appelle ») | 4, 7 |
| **Diagnostic « Ai-je besoin d'un architecte ? » honnête**, y compris quand la réponse est non | 6 |
| **Fourchette d'honoraires affichée avant tout rendez-vous** | 8 |
| **Séquestre tenu par un établissement de paiement agréé, nommé** ; règles de déblocage écrites ; validation tacite après 7 jours ; médiation en cas de désaccord | 9, 15 |
| **Séquestre étendu au suivi de chantier** (honoraires de l'architecte, pas les travaux) | 10, et élargit la base de commission |
| **8 % plutôt que 10 %, sans abonnement ; 5 % sur les 3 premières missions des fondateurs** | 11 |
| **Pas d'esquisse gratuite**, inscrit dans les CGU | 14 |
| **Brief relu par un architecte référent pendant les 3 premiers mois** ; l'agent dit « je ne sais pas » sur le PLU quand la source manque | 13, 17 |
| Avis juridique + démarche auprès de l'Ordre (`ops.md`) | 16 |
| *Écarté :* le séquestre sur les travaux des entreprises | autre métier, autre agrément |

### 3. La pile

- **La chose unique (demandée par la lentille Produit) : « Votre architecte est payé, votre projet est protégé. »** C'est le séquestre qui distingue Archibald. Le brief IA est la porte d'entrée gratuite, et le matching est le moyen.
- **Côté client, gratuitement :**
  - le diagnostic honnête (« Ai-je besoin d'un architecte ? ») ;
  - un brief PDF à montrer à la banque ;
  - 3 architectes compatibles, avec réalisations comparables et fourchette d'honoraires ;
  - le séquestre étape par étape, avec médiation ;
  - un rappel humain sur demande.
- **Côté architecte :**
  - des clients au brief cadré ;
  - le paiement garanti par le séquestre ;
  - zéro esquisse gratuite ;
  - 8 % seulement sur ce qui passe par le séquestre, sans abonnement.
- **Garantie client :** si l'architecte ne livre pas l'étape validée au contrat, les fonds de cette étape sont rendus, après médiation. Elle ne coûte rien à Archibald, puisque les fonds sont séquestrés.
- **Garantie architecte :** une étape livrée et non contestée sous 7 jours est payée automatiquement.
- **Urgence réelle :** le statut fondateur pour les 50 premiers architectes de la ville, jusqu'à l'ouverture publique.

### 4. Équation de valeur, avant et après (1 à 10)

| | client avant | client après | architecte avant | architecte après |
|---|---:|---:|---:|---:|
| Résultat rêvé | 7 | 7 | 6 | 7 |
| Probabilité perçue | 3 | 6 | 4 | 5 |
| Délai | 6 | 6 | 5 | 5 |
| Effort et sacrifice | 4 (5 % en plus) | 8 (gratuit) | 4 | 5 |

### 5. Le re-test

- **Clients** (même graine 1102, 20 personnes) : **5 % → 70 %**.
  - Par segment (peu de données) : 80 % pour la maison neuve, 75 % pour l'extension, 57 % pour la rénovation.
  - L'objection qui reste : « l'algorithme propose ceux qui paient ». Elle est **atténuée, pas levée** : seuls les premiers avis vérifiés la feront tomber.
- **Architectes : pas de re-test de l'offre Archibald.** Dans la v1 (`_v1-archimatch/panel-v2/`), une offre comparable (5 % plafonné, zéro esquisse, garantie) avait fait passer l'adhésion de 30 % à 55 %. **À re-tester à 8 %** avant d'engager quoi que ce soit.

## The numbers

> Les rapports de l'outil affichent « $ » et « a day » : lire **euros HT** et **par mois** (une unité = une mission signée dont les honoraires passent par le séquestre). Toutes les hypothèses sont des ESTIMATIONS, détaillées dans `cfo-sources.md`. Ce n'est pas un conseil financier, fiscal ou juridique : un expert-comptable doit valider le modèle, notamment le traitement de la TVA sur les commissions et les flux du séquestre.

- **La marge.** Avec 8 % de 9 000 € d'honoraires séquestrés, chaque mission rapporte **720 €** et laisse **314 € (44 %)** après ses coûts directs. Au plan de 20 missions par mois, la marge est de **15 %**.
- **Le point mort : 13 missions par mois**, soit environ 52 briefs par mois.
- **L'année 1 perd 21 282 €.** Il faut **36 262 €** de trésorerie, dont 13 000 € de démarrage : le site et l'agent existent déjà, ce qui réduit fortement l'investissement de départ.
- **La ligne à surveiller : la base de la commission.**
  - Sur la seule conception (6 000 € à 8 %, soit 480 €), chaque mission ne laisse que 74 €, le point mort monte à 42 missions par mois et l'année 1 perd 40 161 €.
  - **Le modèle du fondateur, à 15 %**, rapporte 900 € par mission. Mais avec un volume divisé par 10 (le panel client passe de 70 % à 5 %), l'année 1 perd **44 102 €**.
- **Trois leviers, chiffrés avec l'outil :**
  1. **10 % des honoraires séquestrés (900 €)** : l'année 1 passe à **-5 622 €** et le point mort à 9 missions par mois. C'est à tester face à 8 %.
  2. **Volume ×1,5** (30 missions par mois au plan) : l'année 1 passe à -7 623 €.
  3. **Le coût d'acquisition (240 € par mission)** est le premier poste. Avec des coûts unitaires +15 %, l'année 1 passe à -26 580 €. Instagram organique et des partenariats avec des courtiers peuvent le faire baisser.
- **Trésorerie.** La commission prélevée à chaque déblocage du séquestre arrive au rythme des étapes, sur 3 à 18 mois. Le besoin de trésorerie réel sera donc **plus élevé** que ce que calcule l'outil.
- **Conditions du conseil** : la commission moyenne doit être supérieure au coût d'acquisition. C'est le cas (720 € contre 240 €), mais l'année 1 reste négative : la condition n'est remplie qu'à moitié.


Every number below comes from the input file. Nothing is looked up or guessed.

### One mission signée via séquestre (volumes = missions PAR MOIS)

| line | per mission signée via séquestre (volumes = missions PAR MOIS) |
| --- | ---: |
| Price | $720.00 |
| Acquisition clients : 4 briefs x 60 EUR par mission signée (ESTIMATION) | -$240.00 |
| Acquisition / activation architectes, part par mission (ESTIMATION) | -$50.00 |
| Rappel humain sous 48 h : 4 briefs x 20 min (ESTIMATION) | -$40.00 |
| IA (agent + brief PDF), 4 briefs (ESTIMATION) | -$8.00 |
| Frais du prestataire de paiement sur 9 000 EUR séquestrés, ~0,75 % (ESTIMATION) | -$68.00 |
| **Contribution** (what each mission signée via séquestre (volumes = missions PAR MOIS) leaves to pay the fixed costs) | **$314.00** (44%) |

### The margin that matters

Fixed costs: $4,050 a month (Rémunération fondateur (minimum, ESTIMATION) $2,500, Contenu Instagram / SEO (ESTIMATION) $800, Outils, hébergement, abonnement prestataire de paiement (ESTIMATION) $400, Expert-comptable + banque (ESTIMATION) $250, Assurance RC pro (ESTIMATION) $100).

- **Break-even: 13 mission signée via séquestre (volumes = missions PAR MOIS)s a day.** Below that you lose money every month.
- **Profit margin at your plan** (20 a day): **15%** of every sale, after every cost.

### Year 1, month by month

| month | mission signée via séquestre (volumes = missions PAR MOIS)s a day | revenue | profit | cumulative (after $13,000 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$4,050 | -$17,050 |
| 2 | 1 | $720 | -$3,736 | -$20,786 |
| 3 | 2 | $1,440 | -$3,422 | -$24,208 |
| 4 | 3 | $2,160 | -$3,108 | -$27,316 |
| 5 | 4 | $2,880 | -$2,794 | -$30,110 |
| 6 | 5 | $3,600 | -$2,480 | -$32,590 |
| 7 | 7 | $5,040 | -$1,852 | -$34,442 |
| 8 | 9 | $6,480 | -$1,224 | -$35,666 |
| 9 | 11 | $7,920 | -$596 | -$36,262 |
| 10 | 13 | $9,360 | $32 | -$36,230 |
| 11 | 15 | $10,800 | $660 | -$35,570 |
| 12 | 17 | $12,240 | $1,288 | -$34,282 |

- **Year 1 operating profit: -$21,282** on $62,640 of revenue.
- After the $13,000 startup spend: -$34,282.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$36,262**.

### What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 15% | 13 | -$21,282 |
| Price -10% | 6% | 17 | -$27,546 |
| Volume -20% | 8% | 13 | -$26,746 |
| Unit costs +15% | 7% | 17 | -$26,580 |

### Red flags

- Year 1 loses money on operations (-$21,282).
- The startup spend is not earned back within year 1.

## Marketing

Il s'appuie sur les panels (`panel/`, `panel-clients-v2/`), les concurrents, l'offre et les chiffres. Les citations des panels servent à la recherche et ne doivent **jamais** être utilisées comme témoignages.

### 1. Positionnement

**Recommandé (client) :**
> Pour les particuliers qui veulent un architecte mais ne savent pas par où commencer, Archibald est le seul service qui vous dit d'abord si vous en avez besoin, vous présente les architectes les plus compatibles avec votre projet et protège chaque euro d'honoraires par un séquestre. Les annuaires, eux, vous laissent seul face au plus connu.

La signature du fondateur reste : **« Pas le plus connu. Le plus compatible avec votre projet. »**

Dans le panel v2, les clients « perdus » et ceux qui « comparent en ligne » adhèrent à 100 % (peu de données). Le séquestre est cité par les clients échaudés par un artisan.

**Côté architecte (recrutement) :** « Vos honoraires sont dans le séquestre avant que vous commenciez. Votre talent compte plus que la taille de votre agence. »

**Angle banque :** « Votre banquier veut un dossier ? Brief PDF en 5 minutes. » C'est le déclencheur cité par 6 clients sur 14 qui adhèrent. Attention : plusieurs disent « le banquier veut des devis, pas un brief ». Le brief doit donc contenir une estimation des honoraires et du coût des travaux.

### 2. Canaux

**Clients**

| canal | pourquoi | coût | succès si |
|---|---|---|---|
| **Instagram @monprojetarchi** (déjà lancé) : avant/après de projets, « 1 minute pour comprendre le PLU », portraits d'architectes compatibles | Le format qui sert le « junior passionné d'ossature bois » ; montre des visages, pas un algorithme | temps + 300 €/mois de sponsorisation | 30 briefs/mois issus d'Instagram |
| **Publicité Google sur les recherches locales** (« architecte extension [ville] », « faut-il un architecte 150 m² ») | Intention au moment du besoin | 1 500 €/mois | ≤ 60 € par brief |
| **Courtiers en crédit et agents immobiliers** | « Mon banquier veut un dossier » | temps | 5 partenaires, 10 briefs/mois |

**Architectes**

| canal | pourquoi | succès si |
|---|---|---|
| **Écoles d'architecture (ENSA) et réseaux de jeunes diplômés** | La cible « jeunes indépendants » ; ceux dont le carnet est vide adhèrent à 100 % | 30 inscrits en 6 semaines |
| **Démarchage direct** (annuaire de l'Ordre de la ville) | Densité locale | 50 fondateurs |
| **Groupes WhatsApp locaux, via les fondateurs** | Le déclic n°1 des refus : « des confrères qui ont été payés via le séquestre » | 3 recommandations par fondateur |

**Ce qu'on ne fait pas :** de lancement national, de TikTok, ni d'annuaires payants.

**Charlotte Cadé (Selency)** : sollicitez son conseil sur la **confiance dans une marketplace entre particuliers** et sur le **paiement sécurisé entre tiers**, des sujets que Selency a dû traiter. Ne la présentez pas comme une partenaire tant que rien n'est convenu.

### 3. Campagne de 30 jours (ouverture publique le lundi 1er février 2027, voir `launch.md`)

| date | canal | action |
|---|---|---|
| lun. 18 janv. | Architectes | Relance des fondateurs : « Ouverture le 1er février ; vos 3 premières missions à 5 % » |
| mar. 19 janv. | Instagram | Série « Avez-vous besoin d'un architecte ? » 1/5 (accroche 1) |
| mer. 20 janv. | Courtiers | Kit partenaire : brief type + lien suivi |
| jeu. 21 janv. | Instagram | Portrait d'architecte fondateur n°1 : sa spécialité, pas sa taille (accroche 6) |
| ven. 22 janv. | LinkedIn du fondateur | Pourquoi un séquestre pour les architectes, avec les chiffres réels du test |
| lun. 25 janv. | ENSA / réseaux | Présentation aux jeunes diplômés |
| mar. 26 janv. | Instagram | « Le PLU en 60 secondes » (accroche 3) |
| jeu. 28 janv. | Instagram | Comment marche le séquestre, en schéma (accroche 4) |
| ven. 29 janv. | Tous | Répétition générale du parcours avec 5 proches |
| **lun. 1er févr.** | Google Ads + Instagram + site | **Ouverture** : 3 annonces (accroches 2, 5, 7), 50 €/jour |
| mer. 3 févr. | Instagram | Portrait d'architecte n°2 |
| ven. 5 févr. | Revue | Coût par brief, part des briefs avec 3 architectes en 72 h |
| lun. 8 févr. | Instagram | Coulisses : un brief anonymisé avant/après |
| mer. 10 févr. | Google Ads | Coupure de l'annonce la plus chère |
| ven. 12 févr. | Revue | Revue J+14 |
| lun. 15 févr. | Courtiers | Deuxième vague de partenaires |
| mer. 17 févr. | Instagram | « Combien coûte un architecte pour une extension ? » (accroche 8) |

### 4. Dix accroches

1. « Avez-vous vraiment besoin d'un architecte ? Réponse honnête en 5 minutes. » *(« ai-je besoin d'un architecte ? »)*
2. « Pas le plus connu. Le plus compatible avec votre projet. » *(signature du fondateur)*
3. « Ce que votre PLU vous autorise, expliqué en 60 secondes. » *(« réglementation incomprise »)*
4. « Vos honoraires sont séquestrés. Vous payez l'étape quand vous la validez. » *(« pas de confiance »)*
5. « Gratuit pour vous. Même prix qu'en direct. C'est écrit. » *(« payer deux fois »)*
6. « Il a 27 ans et construit en bois. Il est peut-être votre architecte. » *(matching par compétences)*
7. « Votre banquier veut un dossier ? Le brief en 5 minutes. » *(déclencheur banque)*
8. « Extension : combien coûte vraiment un architecte ? » *(« je ne sais pas ce que coûte un architecte »)*
9. *Architectes :* « Vos honoraires sont dans le séquestre avant que vous commenciez. » *(impayés)*
10. *Architectes :* « Zéro esquisse gratuite. 0 € tant que vous ne signez pas. » *(esquisse gratuite, commission)*

### 5. Budget et indicateurs

- **Budget mensuel :** 1 500 € de Google Ads + 300 € de sponsorisation Instagram (inclus dans les 60 € par brief), et 800 € de contenu (dans les coûts fixes).
- **Le plafond à ne pas dépasser :** 720 € de commission moins 166 € d'autres coûts variables (architectes 50 €, rappel humain 40 €, IA 8 €, prestataire de paiement 68 €) = **554 € par mission**. Rapporté à 4 briefs par mission, c'est **138 € par brief au maximum**. Le plan repose sur 60 €.
- **Les trois chiffres de la semaine :**
  1. **Coût par brief** : on change de canal au-delà de 90 €.
  2. **Part des briefs avec au moins 2 architectes intéressés en 72 h** : on recrute des architectes en dessous de 80 %.
  3. **Part des missions signées dont les honoraires passent vraiment par le séquestre** : c'est l'indicateur anti-fuite demandé par le conseil. En dessous de 70 %, on revoit l'offre.

## Brand

Il s'appuie sur la signature du fondateur, le positionnement (`marketing.md`) et les concurrents.

### 1. Le nom

**Archibald est un bon nom : il est gardé.**
- **Ce qu'il dit :** « archi », avec un prénom rassurant, presque un personnage. Il incarne la confiance et la compagnie plutôt que la plateforme.
- **À l'oral :** facile à dire et à retenir.
- **En icône :** un « A » ou un monogramme.
- **Le risque principal :** la famille de noms en « Archi- » des concurrents (Archidvisor, Archibien, Archionline). Archibald s'en distingue parce que c'est un prénom.
- **Ma recherche :** je n'ai trouvé aucune plateforme d'architecture nommée « Archibald », mais je n'ai pu faire que des recherches publiques. Le nom est courant ailleurs (marques, commerces), donc **la vérification dans les bonnes classes est indispensable**.
- **Incohérence à régler :** le compte Instagram s'appelle **@monprojetarchi**, pas Archibald. Choisissez : renommez-le en @archibald.archi (ou un équivalent libre), ou gardez « Mon projet archi, par Archibald » comme série de contenus.

**Alternatives** si la marque n'est pas disponible : **Archibalde**, **Maison Archibald**, **Archibald Studio**. Le mieux est de garder « Archibald » associé à un mot distinctif déposable.

#### Vérifications à faire vous-même (je n'ai pas pu accéder aux registres)

- **Marque :** [INPI](https://data.inpi.fr/) et [EUIPO eSearch](https://euipo.europa.eu/eSearch/), dans les classes **42** (services d'architecture), **35** (mise en relation, publicité), **36** (services financiers : **important à cause du séquestre**) et **9** (logiciel).
- **Domaines :** archibald.fr et archibald.archi via l'[AFNIC](https://www.afnic.fr/) ; à défaut, archibald-architectes.fr.
- **Comptes :** Instagram, LinkedIn, TikTok, YouTube.
- Un conseil en propriété industrielle valide le choix. **Rien n'est protégé tant que le dépôt n'est pas fait.**

### 2. Promesse et voix

- **La promesse :** *« Le bon architecte pour votre projet, et chaque euro protégé. »*
- **Signatures :**
  1. « Pas le plus connu. Le plus compatible. » (celle du fondateur, à garder en tête)
  2. « Votre projet mérite le bon architecte. »
  3. « Payé. Protégé. Compatible. »
- **La voix :**
  - **Complice** (Archibald est un personnage) : faire « Archibald a lu votre PLU : voici ce qui est possible » ; ne pas faire « Notre algorithme propriétaire a analysé vos données ».
  - **Honnête** : faire « Pour 12 m², vous n'avez pas besoin d'architecte. Voici à qui vous adresser » ; ne pas faire « Le meilleur architecte garanti à 100 % ».
  - **Respectueuse du métier** : faire « Votre talent compte plus que la taille de votre agence » ; ne pas faire « Boostez vos leads ».
- **Avant / après (ligne du pitch) :**
  - Avant : « Un matching connecte le bon projet au bon architecte selon ses vraies compétences. »
  - Après : « Archibald vous présente les architectes qui ont déjà fait des projets comme le vôtre, qu'ils aient 27 ans ou 30 ans de métier. »

### 3. L'identité visuelle (brief)

- **Couleurs** (contrastes calculés au rapport WCAG) :
  - **Encre** `#1F2A2E` sur **Papier** `#F6F3EE` : 13,3:1 (AAA).
  - **Bois** `#A84A25` pour l'accent : 5,17:1 sur Papier (AA), et texte blanc sur Bois lisible (AA).
  - Ces couleurs évoquent le calque, l'encre et le bois, dans l'esprit du « junior passionné d'ossature bois ».
- **Typographie :** Fraunces (titres) et Inter (texte), toutes deux gratuites sous licence SIL OFL sur [Google Fonts](https://fonts.google.com/).
- **Brief du logo :** un « A » construit comme un trait d'architecte (un faîte, un compas stylisé discret), avec en option un nœud papillon ou des lunettes pour incarner le personnage d'Archibald. Il doit fonctionner en 32 px, sur le brief PDF et sur un avatar Instagram. À éviter : maison clipart, loupe, cœur.
- **Les 5 premiers points de contact :**
  1. L'accueil, avec « Avez-vous besoin d'un architecte ? ».
  2. **Le brief PDF : le vrai produit visible**, à soigner comme un rendu d'architecte.
  3. L'email de dépôt au séquestre (« Vos honoraires sont protégés »).
  4. Le premier portrait d'architecte sur Instagram.
  5. La réponse à la première plainte, sous 24 h, signée par le fondateur.

## Operations

### 1. Le cycle (★ = vu par le client ou l'architecte)

1. ★ **Le diagnostic et le brief IA** (5 min). Le PDF contient le budget, le PLU (avec sa **source** : le document d'urbanisme consulté, ou « non trouvé »), la faisabilité, le style et une **estimation des honoraires**.
2. ★ **Le rappel humain sous 48 h, si le client le demande** : relecture du brief, et une réponse honnête si un architecte n'est pas nécessaire.
3. **Le matching.** Les critères publiés sont la zone, le type de projet, la technique (bois, rénovation énergétique, etc.), les réalisations comparables et la disponibilité. Aucun critère payant. Pendant les 3 premiers mois, **un architecte référent relit le brief**.
4. ★ **Les architectes** reçoivent le brief anonymisé et ont 72 h pour se dire intéressés. Le client reçoit au plus 3 profils, avec fourchette d'honoraires. Les coordonnées ne sont échangées qu'avec ceux qu'il choisit.
5. ★ **Le contrat d'architecte** est signé hors plateforme (contrat type de l'Ordre recommandé). L'échéancier des honoraires est saisi dans Archibald.
6. ★ **Le dépôt au séquestre** des honoraires de la première étape, voire de toute la conception, chez le **prestataire de paiement agréé**.
7. ★ **L'étape livrée** (esquisse, APS, APD, PC…) : le client valide sous 7 jours, sinon c'est validé automatiquement. Le prestataire débloque les fonds, moins la commission de 8 %, vers l'architecte.
8. ★ **En cas de désaccord** : gel des fonds de l'étape, puis médiation (procédure B).
9. **Le suivi anti-fuite** : la part des honoraires du contrat réellement passée par le séquestre, avec relance aux étapes non déposées.

### 2. Prestataires (à comparer, prix à demander)

| besoin | options | point clé |
|---|---|---|
| **Séquestre / paiements de marketplace** | prestataires de paiement pour marketplaces agréés en Europe (par ex. [Stripe Connect](https://stripe.com/fr/resources/more/payment-solutions-marketplace-france), Mangopay, Lemonway) | **les fonds doivent rester chez l'établissement agréé, jamais sur le compte d'Archibald** ; vérifier son statut auprès de l'ACPR ; KYC des architectes |
| Agent IA + PDF | déjà en place | ajouter la source du PLU et la mention « indicatif » |
| Signature électronique | outil du marché | contrat et échéancier |
| Comptabilité | expert-comptable | TVA sur les commissions, flux en séquestre |
| Assurance | RC professionnelle d'intermédiaire de plateforme | à faire chiffrer par 2 courtiers |
| Juridique | avocat en droit du numérique et des paiements + droit de la construction et déontologie des architectes | **le poste le plus critique** |

### 3. L'équipe

- **Les 3 premiers mois :** le fondateur fait les rappels (20 min par brief), le recrutement d'architectes et le contenu Instagram. Un **architecte référent** relit les briefs (rémunéré à l'acte ou en parts à discuter : ce coût n'est pas dans `numbers.json`).
- **Au plan (20 missions/mois, environ 80 briefs) :** environ 27 h par mois de rappels, ce qui reste faisable seul. **Au-delà de 40 missions par mois**, il faudra un temps partiel « succès client » : relancez `/founder-cfo` à ce moment.

### 4. Les procédures clés

**A. La qualité d'un brief (avant l'envoi aux architectes)**
1. Vérifier la surface avant et après travaux, et le seuil des 150 m².
2. Vérifier que la source du PLU est présente.
3. Comparer le budget au coût au m² : si l'écart dépasse 30 %, rappeler le client.
4. Vérifier que le financement est déclaré.
5. Si un architecte n'est pas nécessaire, le dire au client et orienter vers une autre solution.

**B. Un litige sur une étape**
1. Geler les fonds de l'étape.
2. Recueillir les positions écrites des deux parties sous 72 h.
3. Proposer un médiateur (médiation de la consommation pour le client particulier).
4. Appliquer la décision.
5. Noter le cas et ajuster les CGU si besoin.

**C. Le dépôt au séquestre**
1. Le contrat est signé.
2. L'échéancier est saisi.
3. Un appel de fonds est envoyé au client.
4. Le dépôt est confirmé aux deux parties (« Vos honoraires sont protégés »).

**D. La revue du lundi**
- Coût par brief.
- Briefs avec 2 ou 3 architectes intéressés en 72 h.
- Part des honoraires passée par le séquestre.
- Litiges ouverts.

### 5. Règles, agréments, assurances (à confirmer par un professionnel ; pas un conseil juridique)

- [ ] **Le séquestre : condition bloquante.** Encaisser des fonds pour le compte de tiers relève des services de paiement. Archibald doit passer par un **établissement de paiement ou de monnaie électronique agréé**, en être agent, ou relever d'une exemption ([JDN sur l'ACPR et les marketplaces](https://www.journaldunet.com/retail/1146067-les-marketplaces-francaises-mises-en-peril-par-les-autorites-bancaires/), [FrenchWeb](https://www.frenchweb.fr/places-de-marche-ce-quil-faut-savoir-sur-la-reglementation-des-paiements/275851) ; articles de 2015-2017, **à faire confirmer par un avocat en droit des paiements**). Ne jamais faire transiter l'argent par le compte d'Archibald.
- [ ] **La déontologie des architectes : une commission de 8 à 10 % sur les honoraires.** Obtenir un avis d'avocat et solliciter la position du CROA ou du CNOA ([code de déontologie](https://architectes.org/sites/cnoa/files/2024-05/code_de_deontologie.pdf)). 2 architectes sur 20 refusent pour cette raison dans le panel, et 6 sur 50 dans la v1.
- [ ] **Les obligations des plateformes** : transparence des critères de classement et de la rémunération versée par les professionnels (Code de la consommation, art. L111-7 et suivants, [Légifrance](https://www.legifrance.gouv.fr/)). Cela rejoint « aucun critère payant ».
- [ ] **Le titre d'architecte** : vérifier l'inscription à l'Ordre de chaque architecte ([DGCCRF](https://www.economie.gouv.fr/dgccrf/qualification-darchitecte-sur-internet)).
- [ ] **Le RGPD** : consentement au partage des coordonnées, durée de conservation des briefs ([CNIL](https://www.cnil.fr/)).
- [ ] **L'IA et le PLU** : mention « estimation indicative, non opposable », source citée, renvoi vers le service urbanisme de la commune.
- [ ] **La médiation de la consommation** ([economie.gouv.fr](https://www.economie.gouv.fr/mediation-conso)).
- [ ] **Les CGU clients et les CGV architectes** : pas d'esquisse gratuite, honoraires identiques au direct, règles de déblocage, validation tacite à 7 jours, médiation.
- [ ] **La RC professionnelle.**

### 6. Registre des risques

| # | risque | probabilité | gravité | plan |
|---|---|---|---|---|
| 1 | Le séquestre est mis en place sans agrément | moyenne | **fatale** | prestataire agréé dès le premier euro, avis d'avocat |
| 2 | Fuite : les honoraires ne passent pas par le séquestre | élevée | forte | séquestre utile aux deux parties, indicateur hebdo, commission basse, garantie client liée au séquestre |
| 3 | L'Ordre juge la commission non conforme | moyenne | forte | plan B : abonnement architecte, ou « séquestre seul » à 2-3 % présenté comme un service de paiement |
| 4 | Le brief IA se trompe sur le PLU ou la faisabilité | moyenne | forte | source citée, mention « indicatif », relecture par l'architecte référent |
| 5 | Litige client-architecte sur une étape | moyenne | moyenne | procédure B, validation tacite, médiation |
| 6 | Pas assez d'architectes réactifs dans la ville | moyenne | forte | 50 fondateurs avant l'ouverture, ENSA, une seule ville |
| 7 | Coût par brief > 90 € | moyenne | forte | Instagram organique, courtiers, coupure des annonces |
| 8 | Honoraires séquestrés moyens < 9 000 € | moyenne | forte | séquestre étendu au suivi de chantier, mesure dès les 10 premières missions |
| 9 | Archidvisor ajoute un séquestre | moyenne | moyenne | densité locale, marque « personnage », relation directe avec les jeunes architectes |
| 10 | Fondateur seul débordé (rappels, litiges) | moyenne | moyenne | procédures écrites, rappel sur demande seulement, architecte référent |

## Launch plan

Le site, l'agent et le brief existent déjà : **le test porte sur la transaction, pas sur le produit.** Tout se joue dans **une seule ville** (celle où vous avez du réseau ; évitez Bordeaux, siège d'Archidvisor). L'ouverture publique est fixée au **lundi 1er février 2027**.

### 1. Tester avant de dépenser : « les 10 premiers séquestres » (12 oct. 2026 → 31 janv. 2027)

Le test se fait en version semi-manuelle : le séquestre passe par le prestataire agréé en mode simple, les rappels et le matching sont faits à la main, sans publicité nationale.

**Les lignes de succès, écrites avant de commencer :**

| mesure | seuil | ce que dit le panel |
|---|---|---|
| Architectes qui acceptent les CGV à 8 % (sur 150 contactés) | **≥ 30** | 40 % adhèrent à 10 % (borne haute) |
| Briefs générés dans la ville | **≥ 60**, à **≤ 60 € par brief** | 70 % des clients du panel l'utiliseraient |
| Briefs avec au moins 2 architectes intéressés en 72 h | **≥ 80 %** | — |
| Missions signées | **≥ 10** | plan : 1 sur 4 briefs |
| **Part des honoraires passée par le séquestre** | **≥ 70 %** | la condition anti-fuite du conseil |
| Honoraires moyens séquestrés | **≥ 7 000 €** | hypothèse : 9 000 € |
| Avis juridique sur le séquestre et la commission | **favorable** | condition bloquante |

**Si les vrais chiffres sont nettement en dessous, ils l'emportent sur les panels.**
- Si les architectes refusent : retour à `/founder-pricing` (essayer « séquestre seul »).
- Si les clients ne déposent pas au séquestre : retour à `/founder-offer`.

### 2. Le compte à rebours (★ = chemin critique)

| semaine | tâches | échéance |
|---|---|---|
| 12 oct. | ★ Choisir la ville. ★ Rendez-vous avec un avocat (paiements + déontologie). Démarrer les échanges avec 2 prestataires de paiement agréés. | 16 oct. |
| 19 oct. | Ajouter au brief : source du PLU, estimation des honoraires, diagnostic « besoin d'un architecte ? ». Recruter l'architecte référent. | 23 oct. |
| 26 oct. | Démarchage : 150 architectes (annuaire de l'Ordre + ENSA), 20 par jour. ★ Courrier au CROA. | 13 nov. |
| 2 nov. | ★ Choisir le prestataire de paiement. Contrat type + échéancier. CGU/CGV. | 13 nov. |
| 16 nov. | **Début du test** : Instagram @monprojetarchi recentré sur la ville, Google Ads à 30 €/jour, 5 courtiers. | 20 nov. |
| 23 nov. → 22 janv. | Briefs, rappels, matching, premiers dépôts au séquestre. Revue chaque lundi. | continu |
| 14 déc. | ★ Avis juridique reçu. Point d'étape (briefs, architectes, premiers dépôts). | 18 déc. |
| 18 janv. | Campagne J-14 (`marketing.md`). Marque : vérification INPI faite, Instagram renommé ou série « Mon projet archi par Archibald ». | 22 janv. |
| 25 janv. | **Bilan du test face aux seuils : décision go / no-go / pivot.** Répétition du parcours. | 29 janv. |
| **1er févr.** | **Ouverture publique dans la ville** (seulement si go) | |

### 3. Le jour d'ouverture (lundi 1er février 2027)

| heure | quoi |
|---|---|
| 8 h | Parcours testé de bout en bout : brief → matching → dépôt test chez le prestataire |
| 8 h 30 | Google Ads (50 €/jour) + post Instagram « C'est ouvert à [ville] » |
| 9 h | Email aux architectes fondateurs : règles (72 h, zéro esquisse, séquestre) |
| 10 h | Appels aux courtiers partenaires |
| 12 h | Point : briefs reçus, erreurs de l'agent (PLU non trouvé ?), temps de rappel |
| 14 h → 17 h | Relecture des briefs, matching, rappels demandés |
| 18 h | Bilan de la journée |
| **Si ça casse** | Agent en panne : formulaire de secours + rappel. Prestataire de paiement en panne : report du dépôt, jamais d'encaissement sur le compte d'Archibald. Coût par brief > 90 € à J+3 : couper l'annonce la plus chère. |

### 4. Les 30 premiers jours

| indicateur hebdomadaire | alerte | action |
|---|---|---|
| Briefs générés | < 15/sem. | renforcer Instagram et les courtiers |
| Coût par brief | > 90 € | couper ou réécrire les annonces |
| Briefs avec au moins 2 architectes en 72 h | < 80 % | recruter par type de projet |
| Part des honoraires séquestrés | < 70 % | revoir l'offre (garantie, commission) |
| Missions signées vs point mort (13/mois) | < 9 au mois 4 | revoir prix et ciblage |

**Revues :**
- **J+7 (8 févr.)** : les briefs sont-ils justes (PLU, budget) ?
- **J+14 (15 févr.)** : quel canal amène les clients qui signent ?
- **J+30 (3 mars)** : remettre les vrais chiffres dans `numbers.json` et relancer `/founder-cfo`.

_The panel is simulated buyers and the numbers are projections from your inputs. Confirm demand with real customers and costs with real quotes before you spend. Not financial, legal or tax advice._
