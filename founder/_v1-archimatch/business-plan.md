# ArchiMatch (nom de travail, provisoire) · Business plan

**Verdict: Not yet**

- ✓ Each projet signé (volumes = projets signés PAR MOIS) earns $365.00 before fixed costs (49% contribution).
- ✗ Year 1 operating LOSS: $15,645.
- ✓ 15 of 50 simulated buyers buy (30%, the bar is 25%).

| key number | |
| --- | ---: |
| Price | $750.00 a projet signé (volumes = projets signés PAR MOIS) |
| Profit margin at plan | 22% per projet signé (volumes = projets signés PAR MOIS) |
| Break-even | 11 projet signé (volumes = projets signés PAR MOIS)s a day |
| Year 1 operating profit | $-15,645 |
| Startup spend | $23,000 |
| Cash needed before it pays for itself | $43,285 |
| Startup money earned back | not in year 1 |
| Buyer panel | 15 buy · 35 pass |

## The idea

- Ce que c'est : une plateforme de mise en relation qui envoie à des architectes des projets (leads) déposés par des entreprises ou des particuliers ; le déposant cadre son besoin avec une IA, puis un algorithme sélectionne 3 architectes qui correspondent au besoin, et ces architectes postulent.
- Pour qui : deux faces. (1) Les déposants : particuliers et entreprises ayant un projet nécessitant un architecte (construction, extension, rénovation, aménagement). (2) Les architectes, qui reçoivent les leads. Segment précis non encore défini par le fondateur.
- Ce qu'on vend, à quel prix : une commission sur le montant facturé par l'architecte sur le projet. Formulation du fondateur : commission prélevée « quand il se positionne sur un projet ». Taux non fixé. Le moment exact du prélèvement (à la candidature, à la signature, ou au paiement des honoraires) n'est pas tranché.
- Où et comment : en ligne, France (fondateur francophone). Parcours : dépôt du projet guidé par IA -> sélection algorithmique de 3 architectes -> candidatures des architectes -> choix par le déposant.
- Budget et contraintes : non communiqués (budget, équipe, compétences techniques, calendrier inconnus).

## Summary

**Ce que c'est.** Une plateforme où un particulier cadre son projet d'extension ou de rénovation lourde avec une IA, puis reçoit 3 architectes vérifiés qui postulent. L'architecte paie une commission seulement s'il signe. Lancement dans une seule métropole.

**Verdict : Not yet (pas encore)**, calculé par `compile.py`. Ce n'est pas une opinion. Les trois chiffres :
- chaque projet signé laisse **365 € (49 %)** après ses coûts directs ;
- le point mort est de **11 projets signés par mois** ;
- **l'année 1 perd 15 645 €** d'exploitation, et il faut **43 285 €** de trésorerie.

**Ce qui doit changer pour passer au vert :** une commission moyenne d'au moins **960 € par projet** (année 1 à +2 625 €, voir `cfo.md`), obtenue par des projets plus gros ou un taux plus haut, **ou** un coût d'acquisition nettement inférieur à 60 € par dossier grâce aux partenariats. C'est le travail de `/founder-pricing` et `/founder-marketing`, mais seul le test réel peut le prouver.

**Où le conseil et les panels sont d'accord :**
- le contournement et le moment de prélèvement : on facture une seule fois, à la signature ;
- il faut un segment étroit : une ville, des projets de plus de 100 k€ ;
- la déontologie est un risque bloquant ;
- le mécanisme « 3 architectes » n'est pas une différence : Archibien et Archidvisor le font déjà.

**Où ils divergent :**
- le conseil voyait les entreprises comme une piste, mais le panel clients donne **0 % chez les PME et commerçants** ;
- le panel architectes accepte mieux l'offre retravaillée (**30 % puis 55 %**), mais avec une fourchette de prix qui baisse (1 à 6 %).

**Le plus gros risque.** L'Ordre des architectes juge la commission non conforme. Réponse : demander par écrit sa position au CROA et l'avis d'un avocat **avant** d'écrire une ligne de code. Plan B : un abonnement architecte, ou un dossier payé par le déposant (le panel clients accepte de 30 à 250 €).

**Pour démarrer.** Environ 3 000 € et 8 semaines pour le test conciergerie à la main (`launch.md`). Le reste du budget (43 k€ de trésorerie au total) n'est engagé que si le test passe ses seuils : au moins 30 architectes à 5 %, 25 dossiers à 60 € ou moins, et au moins 3 contrats signés.

**Cette semaine.** Choisir la ville, prendre rendez-vous avec un avocat spécialisé en déontologie des architectes, et envoyer le courrier au CROA.

*Les panels sont des acheteurs simulés et les chiffres sont des projections : seuls de vrais clients et de vrais devis les confirment. Pas un conseil financier, juridique ou fiscal.*

## What the board said

**Vote : 3 « FUND IF » (financer sous conditions) sur 3. Score moyen : 4/10.**
Lentille Offre 4 · Lentille Monopole 4 · Lentille Produit 4. Mémos complets dans `board/`.

### Les risques soulevés par plusieurs membres (d'abord)

1. **Le contournement (3/3).** La commission porte sur des honoraires facturés hors plateforme, sur des mois. Une fois l'architecte et le client en contact, rien ne les oblige à repasser par la plateforme. Prélever « quand il se positionne » (à la candidature) fait payer 2 architectes sur 3 pour un projet perdu ; prélever à la signature ou sur les honoraires expose à la fuite.
2. **Pas de segment choisi (3/3).** Particuliers + entreprises × construction, extension, rénovation, aménagement = quatre ou cinq marchés différents. IA de cadrage et algorithme seront moyens partout.
3. **Démarrage à froid et distribution (2/3).** Il faut des projets pour attirer les architectes et inversement ; un particulier fait appel à un architecte une fois dans sa vie, donc chaque client s'acquiert et ne revient pas. Coût d'acquisition inconnu.
4. **Promesse « 100 % » sans preuve (2/3).** Si les 3 architectes ne postulent pas ou ne collent pas, l'expérience échoue dès le premier usage.
5. **Conformité déontologique (2/3).** Une commission sur honoraires d'architecte est-elle compatible avec les règles de la profession ? Non tranché.

### Désaccords à garder

- La lentille Monopole voit un actif durable possible (la donnée de cadrage accumulée, l'effet de réseau) ; la lentille Produit doute que la plateforme possède assez de l'expérience pour que cet actif compte.
- La lentille Offre envisage de faire payer aussi le déposant (cadrage IA premium) ; les deux autres n'en parlent pas.

### Conditions (checklist pour le reste du pack)

- [ ] **Un segment, une zone**, énoncés en une phrase, avec une taille de marché sourcée. → /founder-competitors
- [ ] **Modèle de revenu tranché** : taux et moment de prélèvement que la plateforme contrôle (signature, paiement sécurisé, forfait), avec un mécanisme anti-contournement concret. → /founder-pricing, /founder-offer, /founder-cfo
- [ ] **Conformité** : confirmation écrite (Ordre des architectes / juriste) que la commission retenue est compatible avec la déontologie. → /founder-ops
- [ ] **Acceptation côté architectes** : des architectes acceptent le taux proposé. → /founder-consumer, puis test réel
- [ ] **Preuve de distribution** : un canal testé avec un coût par déposant mesuré. → /founder-marketing, /founder-launch
- [ ] **Unit economics positives** : commission moyenne par projet signé > coût d'acquisition des deux faces. → /founder-cfo
- [ ] **Règle de service mesurable** sur la promesse des 3 architectes (disponibilité vérifiée, délai de réponse, plan B). → /founder-ops
- [ ] **Parcours de bout en bout écrit**, du dépôt au paiement des honoraires, chaque relais avec un responsable. → /founder-ops
- [ ] **Une offre écrite pour chaque face**, avec garantie. → /founder-offer
- [ ] **Test manuel avant de coder** : cadrage et mise en relation faits à la main sur un petit lot de vrais projets. → /founder-launch

### La version la plus forte que le conseil voit

Pas « une plateforme pour tous les projets d'architecte en France », mais un service étroit : les particuliers d'une seule métropole qui ont un projet d'extension ou de rénovation lourde (le type de projet où l'architecte est souvent requis et où le client ne sait pas formuler son besoin), cadrés par l'IA en un dossier propre, présentés à 3 architectes vérifiés et disponibles. L'architecte ne paie rien tant qu'il n'a pas signé ; la plateforme facture au moment qu'elle contrôle (la signature du contrat, via un contrat type ou un paiement passant par elle). C'est plus petit que ce qui a été présenté, et c'est volontaire : une niche à dominer avant d'élargir.

## The competition

Recherche du 11/10/2026, sources publiques uniquement. **Limite importante :** les sites des concurrents, Trustpilot et architectes.org étaient injoignables depuis cet environnement (erreur DNS) ; les faits viennent d'articles de presse et d'extraits de moteur de recherche, souvent anciens (2016-2021). Tout prix doit être revérifié sur le site du concurrent avant décision.

### 1. Le tableau (du plus direct au moins direct)

| Concurrent | Type | Prix comparable | Ce qu'il vend | Source |
|---|---|---|---|---|
| **Archibien** | Direct | non publié | L'équipe évalue faisabilité et budget, puis **sélectionne 3 architectes** parmi ~350 partenaires locaux qui font un mini-concours (esquisse, plan, planning, budget) | [Europe 1](https://www.europe1.fr/node/710449), [LCL](https://www.lcl.fr/banque-privee/actualites/autres-horizons/la-preuve-par-trois-archibien) |
| **Archidvisor** | Direct | **7 % des honoraires HT** de l'architecte + 35 € HT/mois ; gratuit pour le client | Mise en relation : **le client compare les candidatures et rencontre les 3 agences les plus pertinentes** ; ~1 250 agences ; « partenaire de l'Ordre » ; >10 000 projets accompagnés en 2020 ; a levé 1,2 M€ | [Gust](https://gust.com/companies/archidvisor), [Journal des Entreprises](https://www.lejournaldesentreprises.com/breve/le-bordelais-archidvisor-leve-12-million-deuros-127993), [MySweetImmo](https://www.mysweetimmo.com/2021/02/10/travaux-et-crise-sanitaire-archidvisor-et-ses-architectes-ont-accompagne-plus-de-10-000-projets-en-2020/) |
| **Trouver mon Architecte** | Direct | Gratuit pour le client | Mise en relation, architectes inscrits à l'Ordre ; actif en 2026 (réponses Trustpilot juin 2026) ; 364 avis | [Solutions Numériques](https://www.solutions-numeriques.com/?p=63941), [Trustpilot](https://de.trustpilot.com/review/trouver-mon-architecte.fr) |
| **Architectes pour tous** (Ordre) | Direct | **Gratuit pour tous**, y compris l'architecte | Annuaire géolocalisé de ~4 000 agences inscrites | [Monimmeuble](https://monimmeuble.com/actualite/architectes-pour-tous-le-service-internet-pour-trouver-son-architecte), [Batiweb](https://www.batiweb.com/actualites/architecture/l-ordre-national-des-architectes-offre-une-nouvelle-vitrine-a-ses-adherents-30933) |
| **Archionline** | Direct | non publié | Architecte + artisans locaux ; a levé 1,2 M€ | [FrenchWeb](https://www.frenchweb.fr/archionline-leve-12-million-deuros-pour-provoquer-le-coup-de-foudre-avec-larchitecte/256980), [Custplace](https://fr.custplace.com/archionline) |
| **Houzz** | Indirect | Houzz Pro dès 399 € | Annuaire + inspiration, >25 000 pros en France | [JDN](https://www.journaldunet.com/retail/1168330-houzz-strategie-france-adi-tatarko/), [GetApp](https://www.getapp.fr/software/133539/houzz-pro) |
| **Habitatpresto** | Indirect | gratuit client, lead non publié | Devis travaux, dont architectes | [Habitatpresto](https://www.habitatpresto.com/devis-travaux/devis-architecte) |
| Bouche-à-oreille, constructeurs, maîtres d'œuvre, dessinateurs | Substituts | gratuit à forfait | Recommandation ; plans + permis sans architecte sous 150 m² | [Construires](https://www.construires.fr/architecte/), [Codeur](https://www.codeur.com/architecte/tarif) |

Également cités dans la presse, statut actuel inconnu : Mon Maître Carré (concours, 25 €/m² à l'époque), Rencontre un Archi, BAM, La Maison des Architectes ([Cogedim](https://www.cogedim.com/le-neuf-decrypte/l-actu-du-neuf/architectures/start-up-bousculent-le-monde-de-larchitecture.html)).

### 2. Fourchette de prix (côté architecte, pour un projet signé)

- Le CNOA indique que les plateformes facturent en général **5 à 10 % des honoraires** de l'architecte si l'affaire aboutit ([document CNOA 2023, via extrait](https://www.architectes.org/sites/cnoa/files/2023-09/field_media_document/988-cdp-63-web2.pdf)).
- Bas : **0 %** (Architectes pour tous, gratuit). Médian : **7 %** (Archidvisor). Haut : **10 %**.
- Repère : honoraires d'architecte typiquement 8 à 15 % du coût des travaux en mission complète, 3 à 5 % en mission partielle (esquisse + permis) — **une seule source non officielle** ([Construires](https://www.construires.fr/plans-architecte-permis-de-construire/)).
- Le client ne paie nulle part : la gratuité côté déposant est la norme du marché.

### 3. Carte de positionnement (texte)

Axes : **qualité de la sélection** (annuaire brut → sélection humaine de 3) × **coût pour l'architecte** (gratuit → commission).

```
                  sélection forte (3 architectes choisis)
                              |
            Archibien •       |      • ArchiMatch (visé)
                              |
  gratuit ------------------- + ------------------ commission
                              |
 Architectes pour tous •      |  • Archidvisor  • Trouver mon Architecte
         Houzz • Habitatpresto|
                  annuaire / liste de contacts
```

### 4. Les plaintes, classées (toutes **minces** : moins de 3 avis lisibles chacune)

1. **Qualité / qualification du prestataire** (Archionline, Archidvisor) : un prestataire « sans compétence ni qualification » ; reproche sur la qualité d'une architecte. [Custplace](https://fr.custplace.com/archionline), [Trustpilot NL](https://nl.trustpilot.com/review/archidvisor.com)
2. **Absence de réponse / suivi** après mise en relation (Archidvisor). [Trustpilot NL](https://nl.trustpilot.com/review/archidvisor.com)
3. **Paiement de l'architecte par la plateforme** en retard (Archionline : un architecte non payé 6 mois après). [Custplace](https://fr.custplace.com/archionline)
4. Contexte réglementaire : enquête DGCCRF en 2017 sur les 3 principaux sites de mise en relation avec des architectes (usage du titre). [DGCCRF](https://www.economie.gouv.fr/dgccrf/qualification-darchitecte-sur-internet)

Trustpilot n'a pas pu être lu en entier : les thèmes sont des pistes, pas des preuves.

### 5. Le vide

**Dit franchement : le mécanisme proposé (« l'algo sélectionne 3 architectes qui postulent », commission sur honoraires) existe déjà.** Archibien sélectionne 3 architectes ; Archidvisor fait déjà rencontrer « les 3 agences les plus pertinentes » parmi ~1 250 et prend 7 % des honoraires ; l'Ordre offre un annuaire gratuit. Il n'y a pas de vide sur le modèle.

Les vides possibles, à prouver :
- **Le cadrage en amont automatisé.** Archibien fait l'évaluation de faisabilité/budget avec une équipe humaine ; personne (dans les sources trouvées) ne livre au client, en quelques minutes, un dossier structuré (surface, seuil des 150 m², type de mission, budget réaliste, contraintes du PLU). C'est la seule vraie différence de l'idée.
- **Les personnes morales.** Les sociétés, SCI, commerces et associations doivent recourir à un architecte quelle que soit la surface ([Construires](https://www.construires.fr/plans-architecte-permis-de-construire/)). Les concurrents parlent surtout aux particuliers. Un service pour PME/commerçants (local commercial, bureaux, ERP) est un segment moins encombré — à valider.
- **La confiance après la mise en relation** (plaintes 1 à 3) : vérification Ordre + assurance, délai de réponse garanti.

### 6. La menace

- **Archidvisor** peut ajouter un formulaire de cadrage IA en quelques semaines : base d'architectes, trafic et partenariat Ordre déjà là.
- **L'Ordre** peut améliorer Architectes pour tous gratuitement ; il fixe aussi les règles du jeu (déontologie).
- Le cadrage par IA n'est pas une barrière : n'importe qui peut le copier. La seule défense est la niche + la donnée accumulée + la relation avec les architectes.

## The buyer panel

**15 buy · 35 pass** (30% buy) out of 50 simulated buyers. Seed 625958, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

### By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Architecte libéral seul, jeune installé (moins de 5 ans) | 15 | 53% |
| Architecte d'une agence plus grosse, orientée marchés publics et promoteurs | 5 | 40%  (thin) |
| Architecte libéral seul, installé depuis longtemps | 15 | 27% |
| Gérant d'une petite agence (2 à 10 personnes) | 15 | 7% |

### By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Carnet vide, cherche du travail | 10 | 100% |
| Déjà inscrit sur des plateformes | 8 | 38% |
| Sélectif sur les projets | 7 | 14%  (thin) |
| Fait ses comptes au centime | 7 | 14%  (thin) |
| Vit du bouche-à-oreille | 13 | 0% |
| Attaché à la déontologie | 5 | 0%  (thin) |

### By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| under $44,000 | 16 | 56% |
| $44,000 to $67,000 | 17 | 18% |
| $67,000 and up | 17 | 18% |

### Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| habit | 11 | "Mes clients viennent tous par recommandation, je n'ai jamais payé pour un client et mon carnet est plein comme ça. Une plateforme de plus, avec Archidvisor et l'annuaire gratuit de l'Ordre qui existent déjà, je ne vois pas ce qu'elle m'apporte." (P004) · "Mon carnet est plein grâce aux recommandations, je n'ai jamais payé pour un client et je ne vois pas pourquoi je commencerais à céder 8 % de mes honoraires à une plateforme. Les particuliers qui passent par ce genre de site veulent surtout un plan gratuit et un devis à comparer." (P005) |
| trust | 7 | "Je n'ai pas le temps de répondre à des dossiers cadrés par une IA avec des budgets de rêve, et 8 % de mes honoraires, c'est quasiment toute ma marge sur une petite mission. Je ne m'inscris pas à une plateforme qui n'existe pas encore dans ma région." (P002) · "Les leads de plateformes, je connais : des particuliers qui veulent une esquisse gratuite et qui disparaissent. Et 8 % sur des honoraires déjà serrés, c'est souvent toute ma marge sur une petite mission ; je laisse les autres essuyer les plâtres et j'attends de voir ce que ça donne dans le groupe WhatsApp." (P010) |
| values | 6 | "Reverser 8 % de mes honoraires à une plateforme commerciale, je ne suis pas sûr que l'Ordre l'accepte, et je ne vais pas risquer ma déontologie pour un apporteur d'affaires. Et avec mes marges, 8 % c'est une bonne partie de ce qui me reste sur une mission." (P003) · "Reverser 8 % de mes honoraires à une plateforme parce qu'elle m'a amené un client, ça ressemble exactement à un apporteur d'affaires rémunéré, et je ne signe rien de ce genre sans savoir ce qu'en dit l'Ordre. J'ai besoin de clients, mais pas au prix de ma déontologie, et il y a déjà Archidvisor et l'annuaire gratuit de l'Ordre." (P025) |
| quality | 4 | "J'ai déjà testé deux plateformes : des particuliers qui veulent une esquisse gratuite et un chiffrage, puis plus de nouvelles. Une IA qui cadre le projet ne change pas qui est au bout, et mes vrais clients viennent du bouche-à-oreille et du groupe WhatsApp." (P008) · "J'ai déjà testé deux plateformes de mise en relation et les leads étaient des particuliers qui voulaient une extension à 40 000 € pour 120 m². Mes bons projets viennent du bouche-à-oreille et du groupe WhatsApp des confrères ; je mettrai peut-être un profil puisque c'est gratuit, mais je n'attends rien et je ne compte pas payer 8 % dessus." (P009) |
| price | 4 | "J'ai déjà 3 à 5 demandes par mois sans payer personne ; donner 8 % de mes honoraires, déjà serrés, pour des projets de particuliers dont la moitié n'aboutit pas, ça ne vaut pas le coup." (P029) · "Sur une extension de maison, mes honoraires couvrent à peine les soirées que je passe sur le permis ; 8 % de ça, c'est ma marge qui part. Je ne vais pas payer un pourcentage à un intermédiaire sur des honoraires déjà tirés vers le bas." (P047) |
| need | 3 | "Après trente ans d'exercice, mes projets viennent du bouche-à-oreille et de clients que je connais ; je n'ai pas besoin d'une plateforme et je n'ai pas le temps de postuler contre deux confrères sur des dossiers de particuliers qui comparent surtout les prix." (P001) · "Mon agence vit des marchés publics et des promoteurs, pas des extensions de particuliers. J'ai déjà testé ce genre de plateforme : des gens qui veulent un plan gratuit et qui disparaissent, je ne vais pas y remettre du temps de mes équipes." (P006) |

### Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 13 | "Mon carnet est vide et l'inscription ne me coûte rien : je ne paie que si un client signe, donc je n'ai rien à perdre à tester. Avec seulement 3 architectes sur le dossier, j'ai une vraie chance, pas comme sur les plateformes où on est 15 à répondre." (P007) · "Mon carnet est vide et l'inscription ne me coûte rien : je ne paie que si je signe, donc je m'inscris dès que ça ouvre dans ma région. 8 % sur un projet que je n'aurais pas eu, c'est mieux que rien." (P011) |
| price | 2 | "Inscription gratuite et je ne paie que si je signe : à mon niveau d'activité, je ne peux pas me permettre de refuser des projets sans risque. Je m'inscris, mais sans illusion, comme sur Archidvisor." (P018) · "Inscription gratuite et je ne paie que si je signe, donc je n'ai rien à perdre à créer un profil à côté d'Archidvisor. Mais je n'y croirai qu'après avoir vu la tête des premiers dossiers." (P021) |

### What would flip a no

- Que le budget du client soit vérifié et réaliste, et que je reçoive le dossier en exclusivité sans avoir à rédiger de candidature.
- Voir des projets réels déjà passés par la plateforme dans ma région, avec des budgets vérifiés par un professionnel, et une commission plafonnée autour de 4 % ou limitée à la première facture.
- Un avis écrit du Conseil de l'Ordre validant le modèle, et une commission plus basse ou plafonnée par projet.
- Une période creuse sans recommandations, et la preuve par des confrères de ma région que les dossiers envoyés sont sérieux, avec un vrai budget et des clients qui signent.
- Que des confrères de mon groupe WhatsApp me disent qu'ils y ont signé de vrais projets bien budgétés, avec des clients sérieux, sans y perdre leur temps.
- Des projets de taille sérieuse (promoteurs, collectivités, entreprises) avec un financement vérifié avant que le dossier m'arrive.
- Que des confrères de ma région me confirment avoir signé de vrais projets payants via ArchiMatch, avec des clients au budget vérifié et qui savent qu'ils paieront des honoraires.
- Des retours de confrères de ma région, dans le groupe WhatsApp, disant que les budgets des dossiers ArchiMatch sont réalistes et que les projets se signent vraiment.
- Des retours concrets de confrères de ma région qui ont signé de vraies missions via la plateforme, avec un taux de signature réel, et une commission plafonnée ou dégressive sur les gros projets.
- Une commission beaucoup plus basse, autour de 3 %, avec des projets réellement qualifiés (budget réaliste, permis nécessaire) et zéro paperasse en plus de mes factures.
- Un creux réel dans mon activité, ou une commission plafonnée et nettement plus basse (autour de 3 %) sur des projets bien cadrés avec un vrai budget.
- Que des confrères de mon groupe WhatsApp me disent qu'ils ont signé de vrais projets correctement budgétés via ArchiMatch, sans y passer des heures.

Buyers say they would buy **1.0 times** in the first month on average.

50 buyers gave all four price answers. Run founder-pricing's van_westendorp.py on the answers folder.

## Pricing

> Note de lecture : les outils affichent « $ » ; ici, côté architectes les montants sont des **pourcentages de commission**, côté clients des **euros**. Panels simulés : ils servent à choisir quoi tester, pas à prouver.

### Ce que disent les acheteurs simulés

**Architectes (50 réponses, `pricing-curve.md`)**
- Fourchette acceptable : **2 % à 8 %** des honoraires. Point d'indifférence (IPP) : **4 %**. Médianes : trop bas 2 %, bonne affaire 4 %, cher 6 %, trop cher 10 %.
- **Les 8 % pitchés sont pile à la limite haute (PME)** : 13 architectes sur 50 ont mis 8 % comme « je n'achète pas ».

**Déposants (14 réponses exploitables sur 20, `pricing-curve-clients.md`)** — s'il fallait payer le cadrage + 3 architectes :
- Fourchette acceptable : **30 € à 250 €**, IPP **90 €**. Médianes : bonne affaire 50 €, cher 150 €.

### Ce que font les concurrents (`competitors.md`)

0 % (annuaire de l'Ordre) · **7 % + 35 €/mois** (Archidvisor) · 5 à 10 % selon le CNOA. Le client ne paie nulle part.

### Ce dont l'entreprise a besoin (`cfo.md`, outil de l'expert-comptable du pack)

Hypothèse : honoraires moyens de **15 000 € HT** par projet signé (ESTIMATION, projets ciblés ≥ 100 k€ de travaux). Coût variable par projet signé : 310 €.

| commission par projet | ≈ taux sur 15 k€ | marge au plan (20/mois) | point mort | résultat année 1 |
|---|---:|---:|---:|---:|
| 480 € | 3,2 % | -6 % | 24 projets/mois | -32 610 € |
| 600 € | 4 % | 15 % | 14 / mois | -22 170 € |
| **750 €** | **5 %** | **32 %** | **9 / mois** | **-9 120 €** |
| 960 € | 6,4 % | 47 % | 7 / mois | +9 150 € |
| 1 150 € | 7,7 % | 56 % | 5 / mois | +25 680 € |

**La tension centrale :** le taux que les architectes acceptent sans discuter (4 %) ne fait pas vivre l'entreprise ; le taux qui la rend rentable dès l'année 1 (≥ 6,5 %) est celui qu'une majorité refuse.

### 1. Le prix recommandé

**5 % des honoraires HT, plafonné à 1 500 € par projet, facturé en une fois à la signature du contrat d'architecte** (sur la base des honoraires du contrat signé).

Pourquoi :
- 5 % est dans la fourchette acceptable (2-8 %), sous Archidvisor (7 %), et entre le point d'indifférence (4 %) et le seuil « cher » (6 %).
- **Le plafond** répond à l'objection n°1 des architectes établis (« plafonnée ou dégressive sur les gros projets »).
- **Une seule facture à la signature** répond à « usine à gaz administrative » et au contournement (la plateforme ne dépend plus de factures étalées sur 18 mois qu'elle ne voit pas), et règle la trésorerie : sans ça, l'encaissement s'étale sur toute la durée de la mission.
- 0 € si rien n'est signé : pas de paiement à la candidature (le « quand il se positionne » du fondateur est rejeté par le panel : 2 architectes sur 3 paieraient pour rien).

### 2. L'échelle (côté architectes)

| palier | prix | pour qui |
|---|---|---|
| **Essentiel** | 5 % à la signature, plafond 1 500 € | tout architecte inscrit à l'Ordre |
| **Fondateur** (50 premiers d'une ville) | 3 % les 12 premiers mois, plafond 1 000 € | amorçage, en échange d'un retour d'expérience |
| *(plus tard)* **Prioritaire** | abonnement ~49 €/mois + 3 % | agences qui veulent plus de dossiers ; à tester une fois la demande prouvée |

### 3. L'offre d'ouverture

Statut **« Architecte fondateur »** : 3 % plafonnés à 1 000 € pendant 12 mois, réservé aux 50 premiers inscrits de la métropole de lancement, jusqu'au jour d'ouverture publique (date fixée par `/founder-launch`). Vraie limite, vraie date, pas de faux prix barré.

### 4. Ce qu'il faut tester avec de vrais acheteurs

1. **Architectes : 4 % vs 6 %** (plafond 1 500 €) — deux versions de la page d'inscription, envoyées à deux moitiés d'une liste de 200 architectes de la métropole ; mesurer les inscriptions avec acceptation des CGV.
2. **Déposants : gratuit vs « dossier vérifié » à 49 €** — le payant filtre les « touristes » (la plainte n°1 des architectes) et répond à « gratuit = c'est moi qui paie en cachette » ; mesurer dossiers déposés et taux de signature à 60 jours.
3. Vérifier l'hypothèse des **15 000 € d'honoraires moyens** sur les 10 premiers projets signés : c'est la variable la plus fragile du modèle.

### 5. Les objections de prix, mot pour mot (panel architectes)

- « 8 % sur des honoraires déjà serrés, c'est souvent toute ma marge sur une petite mission. » (P010)
- « Sur une extension de maison, mes honoraires couvrent à peine les soirées que je passe sur le permis ; 8 % de ça, c'est ma marge qui part. » (P047)
- « J'ai déjà 3 à 5 demandes par mois sans payer personne ; donner 8 % de mes honoraires, déjà serrés, pour des projets de particuliers dont la moitié n'aboutit pas, ça ne vaut pas le coup. » (P029)

Côté clients, l'objection n'est pas le prix mais la **transparence** : « Gratuit pour moi, ça veut dire que la commission de l'architecte se retrouve dans ses honoraires, donc dans ma facture. » (panel déposants, P001)

## The offer

L'offre est construite pour **l'architecte**, qui paie, avec la méthode de la lentille Offre. Le déposant a sa propre promesse (en bas). Pitch avant : `pitch-v1.md`. Pitch après : `pitch.md`.

### 1. Les obstacles (dans les mots du panel et des plaintes concurrentes)

Avant : 1. « 8 %, c'est toute ma marge » · 2. « Je n'ai jamais payé pour un client » · 3. « Les leads de plateforme veulent un plan gratuit et disparaissent » · 4. « Le budget du client sera irréaliste » · 5. « Le client n'aura pas son prêt » · 6. « Est-ce compatible avec l'Ordre ? » · 7. « Comment savez-vous ce que je facture ? Usine à gaz » · 8. « Je n'ai pas le temps de rédiger des candidatures » · 9. « Mis en concurrence à 3, je fais une esquisse gratuite pour rien » · 10. « Archidvisor et l'annuaire de l'Ordre existent déjà » · 11. « Pas encore dans ma région ».
Pendant : 12. Coordonnées client communiquées trop tard ou trop tôt · 13. Tirer les honoraires vers le bas face aux 2 autres · 14. Petits projets mal payés.
Après : 15. Projet abandonné après signature · 16. Commission prélevée sur toute la durée de la mission · 17. Aucun retour si le client disparaît.

### 2. Solutions, notées (valeur 1-5 / coût 1-5), gardées en gras

| obstacle | solution | valeur | coût |
|---|---|---:|---:|
| 1, 16 | **5 %, plafond 1 500 €, une seule facture à la signature** | 5 | 1 |
| 3, 4, 14 | **Dossier vérifié** : seuil 100 k€ de travaux, budget contrôlé au coût réel du m² | 5 | 2 |
| 5, 15 | **Financement déclaré (apport ou accord de principe) + remboursement si abandon faute de financement** | 5 | 2 (75 €/projet modélisé) |
| 9, 8 | **Règle « zéro esquisse gratuite » dans les CGU + candidature en 10 minutes** | 5 | 1 |
| 6 | **Avis juridique écrit publié** ; viser ensuite une position écrite du CROA | 5 | 2 |
| 7 | **Rien à déclarer après la signature** | 4 | 1 |
| 2, 11 | **Statut fondateur** (50 places par ville) | 3 | 3 |
| 13 | Fourchette d'honoraires indicative affichée au client (repère, pas d'enchère) | 3 | 1 |
| 10 | Comparatif honnête avec Archidvisor / annuaire de l'Ordre | 2 | 1 |
| — | Suivi de chantier, contrat type, paiement séquestre | 3 | 5 (écarté pour la V1) |

### 3. La pile

- **Le cœur : « Projets Signables ».** Des projets de particuliers de plus de 100 k€ de travaux dans votre métropole, cadrés, au budget vérifié et au financement déclaré, envoyés à 3 architectes seulement.
- **Bonus 1 : Zéro esquisse gratuite.** C'est écrit dans les CGU côté client. Répond à « je fais une esquisse pour rien ».
- **Bonus 2 : 10 minutes pour postuler.** Disponibilité, 3 références, fourchette d'honoraires. Répond à « pas le temps ».
- **Bonus 3 : Une seule facture.** 5 %, plafonnés à 1 500 €, émis à la signature, puis rien à déclarer. Répond à « usine à gaz ».
- **Garantie « Financement ».** Si le projet est abandonné avant le dépôt du permis faute de financement, la commission est remboursée. Coût modélisé : 10 % des projets × 750 € = 75 € par projet signé.
- **Urgence réelle.** Statut fondateur pour les 50 premiers de la ville jusqu'à l'ouverture publique.
  - **Modification après les chiffres du CFO** (non re-testée) : le tarif fondateur à 3 % ne vaut que pour les **2 premiers projets signés** de chaque architecte, pas 12 mois. À 450 € par projet, chaque signature ne laisse que 65 € et le point mort monte à 61 projets par mois.
- **Conformité.** Avis juridique écrit, consultable avant l'inscription. **Le pitch le présente comme acquis, alors qu'il reste à obtenir avant le lancement** (voir `ops.md`).

### 4. Équation de valeur (architecte), avant / après (1-10)

| élément | v1 | v2 | ce qui le fait bouger |
|---|---:|---:|---|
| Résultat rêvé (projets signés, bien payés) | 6 | 7 | seuil 100 k€ |
| Probabilité perçue | 3 | 5 | budget vérifié, financement, garantie, avis juridique |
| Délai | 5 | 5 | inchangé (cycle de signature long) |
| Effort et sacrifice | 3 | 6 | 10 min, zéro esquisse, facture unique, plafond |

### 5. Le re-test (panel simulé, même graine 625958)

| | v1 (`panel/`, 50 architectes) | v2 (`panel-v2/`, 20 architectes) |
|---|---:|---:|
| Taux d'inscription | **30 %** | **55 %** |
| Gérants de petite agence | 7 % | 67 % (peu de données) |
| Architectes qui vivent du bouche-à-oreille | 0 % | 20 % (peu de données) |
| Fourchette de prix acceptable | 2 à 8 % | **1 à 6 %** |

- **Ce qui a baissé :** les refus pour cause de prix (4 sur 50, soit 8 %, puis 1 sur 20, soit 5 %) et le grief « usine à gaz ».
- **Ce qui ne bouge pas :**
  - **la déontologie** : un avis payé par la plateforme « n'est pas l'Ordre ». Seule une position écrite du CROA ou du CNOA lève l'objection ;
  - **la preuve sociale** : « des confrères de mon groupe WhatsApp qui ont signé » ;
  - **la peur de la mise en concurrence sur les honoraires** à 3.
- **Prudence :** plusieurs agents ont compté « s'inscrire gratuitement » comme un achat. Une inscription n'est pas un projet signé. Lisez donc 55 % comme le haut de la fourchette.

### 6. La promesse côté déposant (non re-testée, tirée du panel clients)

Le panel clients a voté à 50 %. Il n'a soulevé aucune objection de prix, mais 9 refus sur 10 portent sur la confiance. D'où quatre promesses :
1. **« Même prix qu'en direct »** : la commission est affichée, et l'architecte s'engage par écrit à ne pas la répercuter.
2. **« Personne ne vous appelle sans votre accord »** : vos coordonnées ne partent qu'aux architectes que vous retenez.
3. **« D'abord : avez-vous besoin d'un architecte ? »** : un diagnostic honnête, y compris quand la réponse est non.
4. **« Pourquoi ces 3 ? »** : le critère de sélection est expliqué, et aucun architecte ne peut payer pour être choisi.

## The numbers

> Les rapports de l'outil affichent « $ » et « a day ». Lire **euros HT** et **par mois** : l'unité est un projet signé et les volumes sont mensuels. Toutes les hypothèses sont des ESTIMATIONS, sources et raisonnement dans `cfo-sources.md`. Pas un conseil financier, fiscal ou juridique : un expert-comptable doit valider la structure, la TVA et la fiscalité.

- **La marge.** Chaque projet signé rapporte 750 € (5 % de 15 000 € d'honoraires) et coûte 385 € en variable. Il laisse **365 € (49 %)**. Au plan de 20 projets signés par mois, la **marge nette est de 22 %**.
- **Le point mort : 11 projets signés par mois**, soit environ 44 dossiers déposés par mois (avec 1 dossier sur 4 signé).
- **L'année 1 perd 15 645 €** d'exploitation. Avec le démarrage, la **trésorerie nécessaire est de 43 285 €**. La mise de départ n'est pas remboursée dans l'année.
- **La ligne à surveiller : la commission encaissée par projet.** À 450 € (tarif fondateur généralisé), la marge passe à -29 % et l'année 1 à -41 745 €. À 960 €, l'année 1 devient positive (+2 625 €). Deux leviers la font bouger : le **taux** et les **honoraires moyens** (15 000 € est l'hypothèse la plus fragile).
- **Trois leviers, chiffrés avec l'outil :**
  1. **Commission moyenne à 960 €** (6,4 %, ou des projets plus gros) : année 1 à **+2 625 €**, point mort à 7 par mois.
  2. **Coût d'acquisition** : c'est 240 € sur 385 de coût variable. Les coûts unitaires +15 % donnent une année 1 à -20 669 €. Inversement, des partenariats gratuits (courtiers, agents immobiliers) font baisser ce poste plus que tout autre.
  3. **Volume** : à -20 %, l'année 1 passe à -21 996 €. La rampe compte autant que le prix.
- **Trésorerie.** La facture unique à la signature est vitale. Une commission prélevée au fil des factures de l'architecte étalerait l'encaissement sur 6 à 18 mois et creuserait encore le besoin de trésorerie.
- **Conditions financières du conseil :** les unit economics par projet sont positives, mais **l'année 1 est négative**, donc la condition n'est remplie qu'à moitié. Il faut prouver une commission moyenne ≥ 750 € et un coût par dossier ≤ 60 €.


Every number below comes from the input file. Nothing is looked up or guessed.

### One projet signé (volumes = projets signés PAR MOIS)

| line | per projet signé (volumes = projets signés PAR MOIS) |
| --- | ---: |
| Price | $750.00 |
| Acquisition déposants : 4 dossiers x 60 EUR par projet signé (ESTIMATION) | -$240.00 |
| Acquisition / activation architectes, part par projet signé (ESTIMATION) | -$50.00 |
| IA de cadrage + hébergement, 4 dossiers (ESTIMATION) | -$8.00 |
| Frais d'encaissement 2 % (ESTIMATION) | -$12.00 |
| Garantie financement : 10 % des projets remboursés x 750 EUR (ESTIMATION) | -$75.00 |
| **Contribution** (what each projet signé (volumes = projets signés PAR MOIS) leaves to pay the fixed costs) | **$365.00** (49%) |

### The margin that matters

Fixed costs: $3,950 a month (Rémunération fondateur (minimum, ESTIMATION) $2,500, Contenu SEO / pages locales (ESTIMATION) $800, Outils, logiciels, hébergement fixe (ESTIMATION) $300, Expert-comptable + banque (ESTIMATION) $250, Assurance RC pro (ESTIMATION) $100).

- **Break-even: 11 projet signé (volumes = projets signés PAR MOIS)s a day.** Below that you lose money every month.
- **Profit margin at your plan** (20 a day): **22%** of every sale, after every cost.

### Year 1, month by month

| month | projet signé (volumes = projets signés PAR MOIS)s a day | revenue | profit | cumulative (after $23,000 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | $0 | -$3,950 | -$26,950 |
| 2 | 1 | $750 | -$3,585 | -$30,535 |
| 3 | 2 | $1,500 | -$3,220 | -$33,755 |
| 4 | 3 | $2,250 | -$2,855 | -$36,610 |
| 5 | 4 | $3,000 | -$2,490 | -$39,100 |
| 6 | 5 | $3,750 | -$2,125 | -$41,225 |
| 7 | 7 | $5,250 | -$1,395 | -$42,620 |
| 8 | 9 | $6,750 | -$665 | -$43,285 |
| 9 | 11 | $8,250 | $65 | -$43,220 |
| 10 | 13 | $9,750 | $795 | -$42,425 |
| 11 | 15 | $11,250 | $1,525 | -$40,900 |
| 12 | 17 | $12,750 | $2,255 | -$38,645 |

- **Year 1 operating profit: -$15,645** on $65,250 of revenue.
- After the $23,000 startup spend: -$38,645.
- Startup money earned back: not within year 1.
- Cash you need before it pays for itself: **$43,285**.

### What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 22% | 11 | -$15,645 |
| Price -10% | 14% | 14 | -$22,170 |
| Volume -20% | 16% | 11 | -$21,996 |
| Unit costs +15% | 15% | 13 | -$20,669 |

### Red flags

- Year 1 loses money on operations (-$15,645).
- The startup spend is not earned back within year 1.

## Marketing

Il s'appuie sur les panels (architectes : `panel/`, `panel-v2/` ; clients : `panel-clients/`), les concurrents (`competitors.md`), l'offre (`offer.md`) et les chiffres (`cfo.md`). Les citations des panels servent à la recherche et ne doivent **jamais** apparaître comme témoignages dans une publicité.

### 1. Positionnement

**Recommandé (côté déposant) :**
> Pour les particuliers qui rénovent ou agrandissent leur maison et qui « ne savent pas par où commencer », ArchiMatch est le service qui transforme votre idée en un dossier clair et vous présente 3 architectes vérifiés et disponibles, au même prix qu'en direct, contrairement aux annuaires où vous appelez 15 agences au hasard.

Ce que disent les panels : chez les déposants, les « perdus » adhèrent à 75 % et la rénovation lourde à 100 % (peu de données). Le cadrage par l'IA est la seule vraie différence face à Archidvisor et Archibien. Enfin, « même prix qu'en direct » répond à la première objection client.

Variantes :
- *Côté architecte (recommandé pour le recrutement)* : « Pour les architectes qui ne veulent plus perdre leurs soirées sur des demandes sans budget, ArchiMatch envoie des projets de plus de 100 k€ au budget vérifié, à 3 architectes maximum, sans esquisse gratuite, et ne coûte rien tant que vous n'avez pas signé. »
- *Angle banque* : « Votre banquier veut des devis d'architecte ? Dossier clair en 10 minutes, 3 architectes en 7 jours. » C'est le déclencheur le plus cité par les déposants qui adhèrent (4 sur 10).

Écarté : les PME et commerçants (0 % dans le panel clients), malgré l'obligation légale du recours à l'architecte pour les personnes morales. À retester plus tard avec une offre dédiée (un humain au téléphone, des références de locaux).

### 2. Canaux

**Déposants (demande)**

| canal | pourquoi | coût | succès si |
|---|---|---|---|
| **Publicité Google sur les recherches locales** (« architecte extension [ville] », « faut-il un architecte pour 150 m² ») | Intention forte, au moment du besoin | 1 500 €/mois au départ | coût par dossier ≤ 60 €, 25 dossiers/mois |
| **Outil gratuit « Ai-je besoin d'un architecte ? »** (le cadrage IA comme porte d'entrée) + pages locales SEO | Répond à l'objection « est-ce que j'ai besoin d'un architecte ? », fait du lien entrant | 800 €/mois de contenu (déjà dans les coûts fixes) | 30 % des diagnostics deviennent des dossiers |
| **Partenariats avec courtiers en crédit et agents immobiliers** | « Mon banquier veut des devis » ; ils voient les acheteurs de maisons à rénover avant tout le monde | Temps fondateur + apport d'affaires éventuel | 5 partenaires actifs, 10 dossiers/mois |

**Architectes (offre)**

| canal | pourquoi | coût | succès si |
|---|---|---|---|
| **Prospection directe** : annuaire public de l'Ordre de la ville, appel + email, 20 par jour | Les « carnets vides » adhèrent à 100 % : il faut les trouver | Temps fondateur | 50 fondateurs en 8 semaines |
| **Groupes WhatsApp et réseaux locaux d'architectes, via les fondateurs** | Le déclic n°1 des refus : « des confrères qui ont signé » | 0 € | 3 recommandations par fondateur actif |
| **Événements du CROA et maisons de l'architecture** | Crédibilité + question déontologique traitée en face | 0 à 300 € | 1 position écrite obtenue |

**Ce qu'on ne fait pas :** Instagram et TikTok grand public (achat trop rare, pas d'intention), annuaires payants, publicité nationale. Une seule ville.

### 3. Campagne de 30 jours (lancement public le lundi 1er février 2027, voir `launch.md`)

| date | canal | action / message |
|---|---|---|
| lun. 18 janv. | Prospection architectes | Relance des fondateurs du test : « Ouverture publique le 1er février : vos 2 premiers projets à 3 % ». Clôture du statut fondateur le 31 janvier |
| mar. 19 janv. | Site | Mise en ligne de l'outil « Ai-je besoin d'un architecte ? » (hook 1) |
| mer. 20 janv. | Courtiers | Envoi du kit partenaire à 15 courtiers : dossier type + lien suivi |
| jeu. 21 janv. | Blog / SEO | Guide « Extension de maison : le seuil des 150 m² expliqué » (hook 2) |
| ven. 22 janv. | LinkedIn fondateur | Récit du test : nombre de dossiers et de signatures, chiffres réels uniquement |
| lun. 25 janv. | Agents immobiliers | Rencontre avec 5 agences : « vos acheteurs de maisons à rénover » |
| mar. 26 janv. | Blog / SEO | Page « Combien coûte un architecte pour une rénovation à [ville] ? » (hook 4) |
| jeu. 28 janv. | Architectes | Webinaire de 30 min : « Comment on vérifie un budget » + avis juridique |
| ven. 29 janv. | Tous | Répétition générale, parcours testé par 5 proches |
| **lun. 1er févr.** | Google Ads + site | **Lancement** : 3 annonces (hooks 3, 5 et 6), budget de 50 €/jour |
| mar. 2 févr. | Courtiers | Relance des 15, premiers dossiers partenaires |
| mer. 3 févr. | LinkedIn / groupes locaux | « C'est ouvert à [ville] » + lien vers l'outil gratuit |
| ven. 5 févr. | Revue | Coût par dossier, taux de candidatures en 72 h |
| lun. 8 févr. | Blog | Coulisses : « Comment un projet devient un dossier en 10 minutes » |
| mer. 10 févr. | Google Ads | Coupure de l'annonce la plus chère, budget renforcé sur la meilleure |
| jeu. 11 févr. | Architectes | Point avec les architectes actifs : qualité des dossiers (note sur 5) |
| ven. 12 févr. | Revue | Revue J+14 (voir `launch.md`) |
| lun. 15 févr. | Agents immobiliers | Deuxième vague de 5 agences |
| mer. 17 févr. | Blog | Guide « Accord de principe bancaire et devis d'architecte » (hook 7) |

**Quand il n'y a rien de neuf :** un dossier anonymisé avant et après le cadrage, une question de déposant avec sa réponse, une règle du seuil des 150 m², un chiffre du mois (dossiers et signatures réels).

**Offre de lancement :** le statut fondateur pour les architectes (2 premiers projets à 3 %) se termine le 31 janvier 2027. Il n'y a pas de remise côté client : le service est gratuit.

### 4. Dix accroches

1. « Ai-je besoin d'un architecte ? Réponse en 2 minutes, gratuite. » *(« est-ce que j'ai besoin d'un architecte ? »)*
2. « 150 m² après travaux : le seuil que personne ne vous explique. » *(« perdu, ne sait pas par où commencer »)*
3. « Votre banquier veut des devis d'architecte ? Dossier clair en 10 minutes. » *(le déclencheur des déposants qui adhèrent)*
4. « Même prix qu'en direct. La commission est affichée, pas cachée. » *(« gratuit = c'est moi qui paie »)*
5. « 3 architectes, pas 30. Et personne ne vous appelle sans votre accord. » *(« harcelé par des démarcheurs »)*
6. « Pourquoi ces 3 ? On vous le dit, et aucun ne paie pour être choisi. » *(« l'algo met ceux qui paient »)*
7. « Rénovation : sachez si votre budget tient avant de rencontrer un architecte. » *(« budget irréaliste »)*
8. *Architectes :* « Zéro esquisse gratuite. C'est écrit dans les CGU. » *(« je fais une esquisse pour rien »)*
9. *Architectes :* « 0 € tant que vous n'avez pas signé. 1 500 € maximum ensuite. » *(« 8 %, c'est toute ma marge »)*
10. *Architectes :* « Budget vérifié, financement déclaré, et remboursement si le prêt tombe. » *(« le client n'aura pas son prêt »)*

### 5. Budget et indicateurs

- **Répartition mensuelle (après le lancement) :** 1 500 € de Google Ads (dans le coût d'acquisition de 60 € par dossier), 800 € de contenu (dans les coûts fixes). Partenariats et prospection : temps du fondateur.
- **Le maximum payable pour un projet signé :** 750 € de commission moins 145 € d'autres coûts variables (architectes 50, IA 8, encaissement 12, garantie 75) = **605 €**. Rapporté à 4 dossiers par signature, c'est **151 € par dossier au maximum** avant de perdre de l'argent. Le plan tient à 60 €.
- **Trois chiffres à suivre chaque semaine :**
  1. **Coût par dossier déposé** : on change d'annonce ou de canal au-delà de 90 €.
  2. **Part des dossiers avec 3 candidatures en 72 h** : on recrute plus d'architectes en dessous de 80 %.
  3. **Taux de signature à 60 jours** : on revoit le seuil, la vérification ou le prix en dessous de 15 % (le plan suppose 25 %).

## Brand

À partir de : le positionnement (`marketing.md`), les concurrents (`competitors.md`, dont Archidvisor, Archibien, Archionline et Trouver mon Architecte) et les raisons d'adhérer des panels (« je ne sais pas par où commencer », « mon banquier veut des devis », « dossier vérifié »).

### 1. Dix noms possibles

| nom | style | ce qu'il dit | à l'oral / en icône | risque |
|---|---|---|---|---|
| ArchiMatch | descriptif | mise en relation avec un architecte | clair, anglicisme | **trop proche des « Archi-… » concurrents** (Archidvisor, Archibien, Archionline). « Match » évoque les sites de rencontre |
| **Trois Archis** | descriptif | la promesse des 3 architectes | se retient, se dit facilement | « archi » familier ; Archidvisor fait aussi 3 agences |
| **Le Bon Dossier** | bénéfice | le cadrage d'abord, avant l'architecte | très clair pour un particulier | générique, marque difficile à protéger |
| **Esquisse** | évocateur | le premier geste d'un projet | joli, métier | contradiction avec « zéro esquisse gratuite » ; nom très courant |
| **Seuil** | évocateur | le seuil des 150 m², le pas de porte | court, mystérieux | abstrait, il faut l'expliquer |
| Mon Projet Archi | descriptif | « c'est pour moi » | long | très générique |
| Plan Clair | bénéfice | un projet enfin clair | se dit bien | générique |
| Cadrage | métier | le cœur du produit | court | froid, technique |
| **Faîte** | évocateur | le sommet d'un toit, « c'est fait » | élégant, jeu de mots | orthographe (faîte / faite / fête) |
| Bâtir Juste | valeurs | la confiance, le juste prix | sérieux | un peu solennel |

**Les 3 retenus :** **Seuil** (distinctif, protégeable, relié au besoin réel), **Le Bon Dossier** (le plus clair pour le déposant, à associer à un logo fort) et **Trois Archis** (la promesse, mais attention à la proximité avec Archidvisor). Abandonner « ArchiMatch » : il se confond avec la famille « Archi-… » des concurrents.

#### Vérifications à faire vous-même

Je n'ai pu lancer que des recherches publiques. Aucune n'a trouvé de plateforme nommée « Archimatch ». Les sites de registre et de domaines étaient injoignables depuis mon environnement.
- **Marque** : [INPI, base marques](https://data.inpi.fr/) (France) et [EUIPO eSearch](https://euipo.europa.eu/eSearch/) (UE). Classes à vérifier : **42** (services d'architecture et de conception), **35** (mise en relation commerciale, publicité), **9** (logiciel) et **36/37** si vous touchez au financement ou aux travaux.
- **Domaines** : .fr via l'[AFNIC](https://www.afnic.fr/) et .com via n'importe quel bureau d'enregistrement. Alternatives : seuil-architecte.fr, leboncadrage.fr.
- **Comptes** : Instagram, LinkedIn (page entreprise), YouTube, TikTok.
- **Confusion** : tenez-vous à distance des noms « Archi-… » cités dans `competitors.md`.
- Un conseil en propriété industrielle confirme le choix. Rien n'est protégé tant que le dépôt à l'INPI n'est pas fait.

### 2. Promesse et voix

- **La promesse :** *« Un projet clair, 3 architectes vérifiés, au même prix qu'en direct. »*
- **Signatures (3 options) :**
  1. « Votre projet, enfin clair. »
  2. « Le bon architecte commence par le bon dossier. »
  3. « Trois architectes. Zéro démarchage. »
- **La voix :**
  - **Claire** : *faire* « Il vous faut un architecte : votre maison dépassera 150 m² » ; *ne pas faire* « Optimisez votre parcours projet grâce à notre IA de pointe ».
  - **Honnête** : *faire* « Vous n'avez pas besoin d'architecte. Voici à qui vous adresser » ; *ne pas faire* « Le meilleur architecte garanti à 100 % ».
  - **Confraternelle** (envers les architectes) : *faire* « Votre temps vaut des honoraires : pas d'esquisse gratuite » ; *ne pas faire* « Boostez votre CA avec nos leads ».
- **Avant / après (ligne du pitch v1) :**
  - Avant : « un algorithme choisit 3 architectes dont le profil correspond ».
  - Après : « 3 architectes inscrits à l'Ordre, choisis pour votre type de projet, votre ville et votre budget. On vous dit pourquoi eux, et aucun ne paie pour être choisi. »

### 3. L'identité visuelle (brief)

- **Couleurs** (contrastes calculés au rapport WCAG) :
  - **Encre** `#1F2A2E` : texte et titres. Sur Papier : 13,3:1 (AAA).
  - **Papier** `#F6F3EE` : fond chaud, rappel du papier calque.
  - **Brique** `#B5532C` : action et accent (boutons). Texte blanc sur brique : 4,95:1 (AA). Brique sur Papier : 4,48:1, **juste sous AA pour le texte courant** : à réserver aux grands textes (≥ 24 px, ou ≥ 18,7 px en gras, AA grand texte) et aux éléments graphiques, ou foncer à `#A84A25` pour du texte courant.
- **Typographie** : **Fraunces** pour les titres et **Inter** pour le texte. Les deux sont gratuites (SIL Open Font License) sur [Google Fonts](https://fonts.google.com/).
- **Brief du logo** : un trait d'architecte (une ligne de seuil ou de faîte) et non une maison clipart. Il doit fonctionner en icône de 32 px, en en-tête d'email et sur la signature PDF du dossier. À éviter : loupe, cœur ou « match » de site de rencontre, compas cliché, dégradés.
- **Les 5 premiers points de contact :**
  1. **La page d'accueil** : la promesse, un bouton « Ai-je besoin d'un architecte ? » et la commission affichée.
  2. **Le dossier PDF généré** : c'est le vrai « produit visible », à soigner comme un rendu d'architecte.
  3. **L'email de confirmation** : « Vos 3 architectes sous 7 jours. Personne ne vous appellera sans votre accord. »
  4. **Le premier post LinkedIn** : les chiffres réels du test.
  5. **La réponse à la première plainte** : sous 24 h, signée par le fondateur, avec ce qui change.

## Operations

Le fonctionnement réel, du dépôt d'un dossier à l'encaissement de la commission. Les coûts reprennent `numbers.json` ; toute différence est signalée.

### 1. Le cycle quotidien (★ = vu par le client ou l'architecte)

1. ★ **Dépôt** : le déposant fait le diagnostic « Ai-je besoin d'un architecte ? », puis le cadrage IA (10 min), et reçoit un dossier PDF.
2. **Vérification** (humaine en V1, 15 min par dossier) :
   - surface après travaux et seuil des 150 m² ;
   - budget comparé au coût au m² des travaux du type de projet ;
   - financement déclaré (apport ou accord de principe) ;
   - seuil de 100 k€ de travaux.
   Si le dossier n'est pas conforme : réponse honnête au déposant (pas besoin d'architecte, budget à revoir, etc.).
3. **Sélection** : 3 architectes selon la zone, le type de projet, les références, la disponibilité déclarée et le taux de réponse. La règle est écrite et publique.
4. ★ **Envoi aux 3** : dossier anonymisé, 72 h pour postuler (disponibilité, 3 références, fourchette d'honoraires). Sans réponse, la place passe au suivant sur liste d'attente.
5. ★ **Présentation au déposant** sous 7 jours : 3 candidatures, avec le « pourquoi eux ». Les coordonnées ne sont échangées qu'avec les architectes que le déposant retient.
6. ★ **Suivi à J+15, J+30 et J+60** : rendez-vous pris ? contrat signé ? Un email au déposant et à l'architecte.
7. ★ **Signature** : l'architecte téléverse la page de son contrat qui porte les honoraires, et une facture de commission unique est émise (5 %, plafond 1 500 €).
8. **Contrôle anti-contournement** : relance à J+90 et J+180, déclaration sur l'honneur dans les CGU, pénalité contractuelle en cas de signature non déclarée. On peut aussi vérifier les permis de construire publiés par la commune quand ils sont publics.
9. **Le soir** : tableau de bord (dossiers, candidatures en 72 h, signatures, encaissements) et réponses aux messages.

### 2. Prestataires et outils (prix à vérifier sur les pages officielles)

| besoin | options | remarque |
|---|---|---|
| Paiement / facture de commission | [Stripe](https://stripe.com/fr/pricing), [GoCardless](https://gocardless.com/fr-fr/tarifs/) (prélèvement SEPA) | le prélèvement SEPA est souvent moins cher pour 750 € ; vérifier par rapport aux 12 € de `numbers.json` |
| Modèle d'IA pour le cadrage | API d'un fournisseur de modèles de langage | quelques centimes à quelques dizaines de centimes par dossier selon le modèle ; les 8 € pour 4 dossiers de `numbers.json` sont prudents |
| MVP | no-code (Webflow / Bubble) + automatisations, ou un freelance | 15 000 € estimés ; demander **3 devis** |
| CRM / suivi des dossiers | outil de base de données simple ou CRM gratuit au départ | |
| Signature des CGU / contrats | outil de signature électronique | |
| Comptabilité | expert-comptable en ligne | 250 €/mois estimés, à faire chiffrer |
| Assurance | **RC professionnelle** pour un intermédiaire / une plateforme | 100 €/mois estimés, à faire chiffrer par 2 courtiers |
| Juridique | avocat en droit de la construction / déontologie des architectes + droit du numérique | 3 000 € estimés, **le poste le plus critique** |

### 3. L'équipe

- **Mois 1 à 3 (test et lancement)** : le fondateur seul. Il fait la prospection des architectes (2 h par jour), la vérification des dossiers (15 min par dossier) et les partenariats (courtiers, agents).
- **Au plan (20 signatures par mois, environ 80 dossiers)** : 80 × 15 min = 20 h de vérification par mois, plus le suivi. Cela tient pour une personne. **Au-delà de 40 signatures par mois**, prévoir un temps partiel « vérification et suivi » ; il n'est pas dans `numbers.json`, donc **il faut relancer `/founder-cfo`** à ce moment-là.
- Les charges sociales et le statut du dirigeant (rémunération ou dividendes) sont à voir avec l'expert-comptable.

### 4. Les procédures clés

**A. Vérifier un dossier (15 min)**
1. Ouvrir le PDF.
2. Contrôler la surface avant et après travaux et le seuil des 150 m².
3. Diviser le budget par la surface et comparer au barème interne par type de projet (à construire avec 3 architectes fondateurs).
4. Si l'écart dépasse 30 % : appeler le déposant (5 min).
5. Vérifier que le financement est déclaré.
6. Statut : Validé / À revoir / Pas besoin d'architecte.
7. Si validé : lancer la sélection.

**B. Une plainte (déposant ou architecte)**
1. Accuser réception sous 4 h.
2. Appeler sous 24 h.
3. Noter les faits dans le CRM.
4. Corriger : ajouter un candidat, rembourser au titre de la garantie, ou exclure un architecte qui a demandé une esquisse gratuite.
5. Envoyer par écrit ce qui change.

**C. Une signature**
1. Recevoir la page du contrat portant les honoraires.
2. Calculer 5 %, plafonné.
3. Émettre la facture.
4. Lancer le prélèvement à 30 jours.
5. Remercier les deux parties et demander un avis au déposant, uniquement si le projet est réel.

**D. La revue hebdomadaire (lundi)**
- Coût par dossier.
- Part des dossiers avec 3 candidatures en 72 h.
- Signatures.
- Liste d'attente des architectes par type de projet : recruter là où il en manque.

### 5. Règles, autorisations, assurances (à confirmer auprès d'un professionnel ; pas un conseil juridique)

- [ ] **Déontologie des architectes : condition bloquante.** Obtenir un avis écrit d'un avocat **et** solliciter la position du CROA de la région ou du CNOA sur une commission versée par l'architecte. Source : [Ordre des architectes, code de déontologie](https://www.architectes.org/sites/cnoa/files/2024-05/code_de_deontologie.pdf). Le décret du 26 juin 2026 qui le modifie est à vérifier ([Légifrance](https://www.legifrance.gouv.fr/)). *Sans cela, 6 refus sur 50 dans le panel ne bougeront pas.*
- [ ] **Obligations des plateformes en ligne** : transparence sur les critères de classement et sur l'existence d'une rémunération par les professionnels (Code de la consommation, art. L111-7 et suivants, sur [Légifrance](https://www.legifrance.gouv.fr/)). Cela rejoint la promesse « pourquoi ces 3 ».
- [ ] **Usage du titre d'architecte** : n'accepter que des inscrits au tableau de l'Ordre et vérifier chaque inscription (voir l'[enquête DGCCRF](https://www.economie.gouv.fr/dgccrf/qualification-darchitecte-sur-internet)).
- [ ] **RGPD** : registre des traitements, durée de conservation des dossiers, consentement au partage des coordonnées ([CNIL](https://www.cnil.fr/)).
- [ ] **Médiation de la consommation** pour les déposants particuliers ([economie.gouv.fr, médiateur de la consommation](https://www.economie.gouv.fr/mediation-conso)).
- [ ] **Immatriculation** de la société ([guichet unique INPI](https://procedures.inpi.fr/)), compte bancaire professionnel, TVA sur les commissions.
- [ ] **CGU déposants + CGV architectes** : zéro esquisse gratuite, commission à la signature, plafond, garantie financement, pénalité en cas de contournement.
- [ ] **RC professionnelle** de la plateforme.

### 6. Registre des risques

| # | risque | probabilité | gravité | plan |
|---|---|---|---|---|
| 1 | L'Ordre juge la commission non conforme | moyenne | **fatale** | avis avant de coder ; plan B : abonnement architecte (ex. 49 €/mois) ou dossier payé par le déposant (49 €) |
| 2 | Contournement : signature sans déclaration | élevée | forte | facture unique, pénalité, relances J+90/J+180 ; garder une commission basse pour que déclarer coûte moins que tricher |
| 3 | Pas assez d'architectes réactifs (moins de 3 candidatures en 72 h) | moyenne | forte | liste d'attente, 50 fondateurs avant d'ouvrir, une seule ville |
| 4 | Coût par dossier > 90 € | moyenne | forte | partenariats courtiers et agents, outil SEO, couper les annonces |
| 5 | Honoraires moyens < 15 000 € | moyenne | forte | seuil de 100 k€ de travaux, mesure dès les 10 premières signatures, relancer le CFO |
| 6 | Un concurrent (Archidvisor) copie le cadrage IA | élevée | moyenne | vitesse, densité locale, qualité de la vérification humaine, relation avec les architectes |
| 7 | Une IA donne un mauvais conseil réglementaire (seuil, permis) | moyenne | moyenne | vérification humaine en V1, mention « indicatif », relecture par un architecte fondateur |
| 8 | Fuite de données ou démarchage | faible | forte | coordonnées partagées seulement avec consentement, accès journalisés |
| 9 | Fondateur seul malade ou débordé | moyenne | moyenne | procédures écrites, délais affichés réalistes, un architecte référent en appui |
| 10 | Mauvais avis public au lancement | moyenne | moyenne | procédure plainte B, réponse publique sous 24 h, correction visible |

## Launch plan

Le lancement public est prévu le **lundi 1er février 2027**, dans **une seule métropole** : celle où vous avez du réseau. Il reste à la choisir (par exemple Lyon, Nantes ou Lille ; évitez Bordeaux, siège d'Archidvisor). Mais d'abord, on teste sans coder.

### 1. Tester avant de dépenser : le « test conciergerie » (12 oct. au 13 déc. 2026)

C'est le test d'un service avec de vrais clients au prix prévu, fait **à la main** : formulaire + IA générique pour le cadrage, vérification par vous, envoi par email, facture manuelle. Le MVP à 15 000 € n'est **pas** engagé avant le résultat.

**Lignes de succès, écrites avant de commencer :**

| mesure | seuil | ce que dit le panel |
|---|---|---|
| Architectes qui acceptent les CGV à 5 % (sur 200 contactés) | **≥ 30** (15 %) | 55 % s'inscrivent dans le panel v2 (borne haute) |
| Dossiers déposés en 6 semaines | **≥ 25**, à un coût de **≤ 60 € par dossier** | 50 % des déposants du panel utiliseraient le service |
| Dossiers avec 3 candidatures en 72 h | **≥ 80 %** | — |
| Contrats signés à 60 jours (mesurés jusqu'à fin janvier) | **≥ 3** | plan : 1 sur 4 |
| Honoraires moyens des contrats signés | **≥ 12 000 €** | hypothèse : 15 000 € |
| Position écrite de l'Ordre (CROA) ou avis d'avocat favorable | **obtenu** | 6 refus sur 50 pour la déontologie |

Si les vrais chiffres sont nettement sous ces seuils, faites confiance au réel et non au panel. Retour à `/founder-offer` (si le refus vient de l'offre), à `/founder-pricing` (s'il vient du taux) ou à l'idée elle-même (si la demande manque). **Si l'Ordre dit non, on arrête le modèle à la commission** et on teste le plan B (abonnement ou dossier payé par le client).

### 2. Le compte à rebours (semaine par semaine ; ★ = chemin critique)

| semaine | tâches | qui | échéance |
|---|---|---|---|
| 12 oct. | ★ Choisir la ville. ★ Prendre rendez-vous avec l'avocat (déontologie + CGU). Lister 200 architectes depuis l'annuaire public de l'Ordre. | fondateur | 16 oct. |
| 19 oct. | Page « Architecte fondateur » (no-code). Premiers appels (20 par jour). ★ Courrier au CROA demandant sa position. | fondateur | 23 oct. |
| 26 oct. | Formulaire déposant + prompt de cadrage + modèle de dossier PDF. Barème coût/m² avec 3 architectes fondateurs. | fondateur | 30 oct. |
| 2 nov. | **Début du test** : Google Ads 30 €/jour + 5 courtiers + 5 agences immobilières. | fondateur | 6 nov. |
| 9 nov. au 11 déc. | Dossiers traités à la main (procédure A), envoi aux 3, suivi J+15. Revue chaque lundi. | fondateur | continu |
| 14 déc. | **Bilan du test** vs lignes de succès. Décision go / no-go / pivot. ★ Avis juridique reçu. | fondateur | 18 déc. |
| 4 janv. 2027 | Si go : commande du MVP (3 devis reçus en décembre). Immatriculation, banque, RC pro, CGU finales. | fondateur + freelance | 8 janv. |
| 11 janv. | ★ MVP : dépôt + diagnostic « Ai-je besoin d'un architecte ? » + back-office + facturation. | freelance | 22 janv. |
| 18 janv. | Campagne J-14 (`marketing.md`). Marque : nom choisi, domaine, logo (`brand.md`). | fondateur | 22 janv. |
| 25 janv. | Recette du parcours avec 5 proches et 3 architectes fondateurs (**ouverture en douceur**). | fondateur | 29 janv. |
| **1er févr.** | **Lancement public** | | |

Les tâches ★ décalent le lancement si elles glissent : la position de l'Ordre et l'avis juridique, le bilan du test, le MVP.

### 3. Le jour du lancement (lundi 1er février 2027)

| heure | quoi |
|---|---|
| 8 h 00 | Vérifier que le site, le formulaire, le cadrage IA et l'envoi d'email fonctionnent (dossier test) |
| 8 h 30 | Activer les 3 annonces Google (50 €/jour) |
| 9 h 00 | Email aux architectes fondateurs : « C'est ouvert » + rappel des règles (72 h, zéro esquisse gratuite) |
| 9 h 30 | Post LinkedIn + message dans les groupes locaux (par les fondateurs, pas de faux comptes) |
| 10 h 00 | Appel aux courtiers et agences partenaires |
| 12 h 00 | Premier point : dossiers reçus, erreurs, temps de vérification |
| 14 h 00 à 17 h 00 | Vérification des dossiers du jour et lancement des sélections |
| 18 h 00 | Bilan du jour |
| **Si ça casse** | Formulaire en panne → un formulaire de secours prêt d'avance. IA en panne → cadrage par téléphone. Coût par dossier au-delà de 90 € dès J+3 → couper l'annonce la plus chère. (Registre des risques : `ops.md`) |

### 4. Les 30 premiers jours

| indicateur (chaque semaine) | seuil d'alerte | action |
|---|---|---|
| Dossiers déposés | < 10 par semaine | renforcer les partenariats courtiers, revoir les annonces |
| Coût par dossier | > 90 € | couper ou réécrire les annonces, pousser l'outil SEO |
| Dossiers avec 3 candidatures en 72 h | < 80 % | recruter des architectes sur les types de projet manquants |
| Signatures cumulées vs point mort (11 par mois) | < 3 au mois 1 | normal ; < 9 au mois 4, revoir prix et seuil |

**Points d'étape :**
- **J+7 (8 févr.)** : les dossiers sont-ils réalistes ? Les architectes répondent-ils ?
- **J+14 (15 févr.)** : quel canal amène les dossiers qui signent ?
- **J+30 (3 mars)** : coût par dossier et taux de signature réels, à remettre dans `numbers.json` puis à faire recalculer par `/founder-cfo`.

_The panel is simulated buyers and the numbers are projections from your inputs. Confirm demand with real customers and costs with real quotes before you spend. Not financial, legal or tax advice._
