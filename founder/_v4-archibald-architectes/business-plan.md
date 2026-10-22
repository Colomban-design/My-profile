# Archibald (agent pour architectes) · Business plan

**Verdict: Not yet**

- ✓ Each abonné-mois (volumes = abonnés actifs PAR MOIS) earns $18.00 before fixed costs (46% contribution).
- ✗ Year 1 operating LOSS: $19,710.
- ✗ 20 of 100 simulated buyers buy (20%, the bar is 25%).

| key number | |
| --- | ---: |
| Price | $39.00 a abonné-mois (volumes = abonnés actifs PAR MOIS) |
| Profit margin at plan | 14% per abonné-mois (volumes = abonnés actifs PAR MOIS) |
| Break-even | 209 abonné-mois (volumes = abonnés actifs PAR MOIS)s a day |
| Year 1 operating profit | $-19,710 |
| Startup spend | $11,000 |
| Cash needed before it pays for itself | $32,300 |
| Startup money earned back | not in year 1 |
| Buyer panel | 20 buy · 80 pass |

## The idea

- Ce que c'est : un agent IA vendu aux architectes, qui cadre à leur place les demandes de leurs futurs clients. Il se branche sur le site de l'agence (et, en option, répond au téléphone) ; en 5 minutes de conversation il qualifie le projet (besoin réel d'un architecte, seuil des 150 m², règles du PLU de la parcelle, faisabilité, budget comparé au coût réel des travaux, délai, style) et remet à l'architecte un brief PDF prêt avant le premier rendez-vous, avec une estimation des honoraires. Les demandes non viables sont filtrées poliment.
- L'effet réseau : quand un architecte décline une demande (trop petite, hors spécialité, pas disponible), l'agent propose au client de la transmettre à un confrère compatible abonné à Archibald, choisi sur ses compétences réelles. Le réseau d'architectes se remplit des demandes refusées des autres, sans achat de leads.
- Pour qui : (1) les architectes libéraux et petites agences (1 à 10 personnes) qui reçoivent des demandes de particuliers et de petites entreprises ; (2) leurs futurs clients, qui parlent à l'agent.
- Ce qu'on vend, à quel prix (hypothèse à tester) : un abonnement mensuel, par exemple 79 € HT/mois (agent sur le site + brief PDF + accès au réseau), option téléphone en supplément ; pas de commission sur les honoraires.
- Où et comment : en ligne, France ; installation en une ligne de code sur le site existant (WordPress, Wix, etc.) ou lien à partager. Actifs existants : agent conversationnel fonctionnel et brief PDF automatique (déjà construits pour la marketplace Archibald), Instagram @monprojetarchi.
- Budget et contraintes : non communiqués. Ambition du fondateur : construire une très grosse entreprise ; l'outil est la porte d'entrée, le réseau d'architectes est l'actif.
- Phrase : « Pas le plus connu. Le plus compatible avec votre projet. »
- Après le pack (voir `offer.md` et `pricing.md`) : mode « prise de brief », où l'agent n'affirme rien au client ; formule à la demande à 5 € par brief ou Agence à 39 € HT par mois ; option téléphone à +15 € ; réseau optionnel.

## Summary

**L'idée.** Un assistant d'accueil IA vendu aux agences d'architecture. Il prend les demandes de leurs futurs clients sur le site (et au téléphone en option), il n'affirme rien au client, et il remet à l'architecte un brief privé : besoin réel, alertes PLU avec leurs sources, écart de budget. Les demandes déclinées peuvent, en option, aller à un confrère abonné (le réseau).

**Ce que disent les tests (simulés).**
- Le conseil vote 3 « FUND IF » sur 3, avec un score de 5,3/10, le meilleur des quatre versions testées.
- Les architectes : **20 %** d'adhésion à 79 € (100 répondants), **22 %** à 39 € (40 répondants). Le prix n'est pas le frein.
- Le segment qui achète : petites agences (30 à 44 %), technophiles (≈ 60 %), carnets vides (50 à 67 %). Ceux qui vivent du bouche-à-oreille n'achètent pas (0 %).
- Les clients finaux : **75 %** utiliseraient l'agent, à condition d'avoir un rappel sous 48 h et la transparence sur les données.

**Les chiffres.**
- 39 € HT par mois, soit 18 € de marge par abonné après l'acquisition.
- Point mort à 209 abonnés.
- L'année 1 perd 19 710 € et demande 32 300 € de trésorerie.
- À 49 €, l'année 1 est presque à l'équilibre (-5 660 €).

**Le prix à tester.** 39 € HT par mois pour les agences, une formule **à la demande à 5 € par brief** (plafond 35 €) pour les libéraux et les carnets vides, et le téléphone à +15 €.

**La thèse « outil → réseau » et l'ambition.**
- L'outil seul est une belle PME : 10 000 abonnés, soit 4,7 M€ de revenu annuel.
- La grosse entreprise ne vient pas de l'abonnement. Elle vient de **la donnée de flux** : Archibald voit passer, avant tout le monde, les projets de construction et de rénovation des particuliers (surface, budget, parcelle, délai).
- Trois extensions possibles, **à ne pas ouvrir avant 1 000 abonnés** :
  1. les mêmes clients finaux ont ensuite besoin d'un bureau d'études, d'un financement et d'artisans (la mise en relation reste au choix du client, sans commission sur l'architecte) ;
  2. d'autres professions réglementées de la maîtrise d'œuvre et de l'expertise (géomètres, diagnostiqueurs, architectes d'intérieur) ;
  3. d'autres pays européens qui ont un seuil légal de recours à l'architecte.

**Verdict.** Ça vaut le coup, **mais pas encore comme une entreprise** : c'est une hypothèse à valider en 60 jours. Le risque n°1 n'est ni le prix ni la technique. C'est le **volume de demandes froides** par architecte, que seules 10 vraies conversations peuvent mesurer (`launch.md`, étape 0).

## What the board said

**Vote : 3 « FUND IF » (financer sous conditions) sur 3. Score moyen : 5,3/10** (Offre 5 · Monopole 5 · Produit 6). C'est le meilleur score des quatre versions testées (v3 Relais : 4,3/10). Les mémos complets sont dans `board/`.

### Ce que les trois membres jugent solide

- **Une douleur nommée par le marché lui-même.** Budgets irréalistes, esquisses gratuites, la moitié des demandes qui n'aboutit pas, soirées perdues : ces plaintes reviennent spontanément dans tous les panels d'architectes depuis la v1.
- **Le blocage déontologique est levé.** Il n'y a plus de commission sur les honoraires, et l'architecte ne paie plus « pour un client ». Il paie pour un outil.
- **Les actifs existent.** L'agent conversationnel et le brief PDF sont déjà construits, et la mise en place tient en une ligne de code.
- **L'effet réseau est bien conçu.** Les refus d'un abonné deviennent des demandes pour un autre abonné. Un standard IA générique ne peut pas offrir ça.

### Les risques soulevés par plusieurs membres

1. **Le volume de demandes entrantes est inconnu (3/3).** Si un architecte reçoit peu de demandes froides, le filtre ne lui rapporte rien. Il résilie, et le réseau ne se remplit pas. **Le panel le confirme** : 33 des 80 refus sont des « need », du type « mes clients viennent par recommandation, je n'ai pas de flux à filtrer ».
2. **Une erreur de l'IA engage l'architecte (3/3).** PLU, seuil des 150 m², honoraires : chaque affirmation faite au client est un risque pour la crédibilité de l'agence. **Le panel le confirme** : 33 refus pour « trust », avec la phrase qui revient le plus souvent : « s'il se trompe, c'est moi qui porte la faute ».
3. **Le démarrage à froid du réseau (Monopole, Produit).** Un renvoi n'a de valeur que s'il existe un confrère compatible dans la même zone. Avec des abonnés dispersés, l'effet réseau est nul.
4. **Trop de promesses (Produit).** Le pitch en contient huit, et chacune peut casser l'expérience devant le client.
5. **Le plafond de marché (Offre, Monopole).** 29 500 architectes × 79 € × 12 ≈ 28 M€ par an, et seulement si 100 % s'abonnent.

### Ce que le conseil juge de la thèse « outil → réseau »

Elle est **juste dans l'ordre, fausse si on inverse**. Le réseau ne devient l'actif que si l'outil est d'abord indispensable seul (Produit). Il faut donc le prouver ville par ville, avec une densité mesurée (Monopole). Pour la « très grosse entreprise », le conseil demande un chemin d'expansion écrit au-delà de l'abonnement. Pistes : autres professions réglementées de la maîtrise d'œuvre, autres pays, ou une prise de valeur sur le flux de projets qualifiés (voir `summary.md`).

### Conditions (checklist)

- [ ] **Couper les promesses** : une seule promesse au lancement, le brief prêt avant le rendez-vous, avec le tri des demandes. Le PLU et les honoraires restent internes à l'architecte tant que leur exactitude n'est pas prouvée. → fait dans `offer.md` (mode « prise de brief »).
- [ ] **Maîtriser les ruptures** : l'IA s'annonce dès la première phrase (AI Act art. 50), l'architecte valide le ton des refus, et le renvoi se fait avec l'accord explicite de l'architecte et du client. → `offer.md`, `ops.md`
- [ ] **Prouver le volume** : sur 10 à 20 pilotes pendant 30 jours, mesurer les demandes reçues, filtrées et briefées. → `launch.md`
- [ ] **Prouver l'exactitude** : 50 briefs validés par les pilotes et un taux publié. → `launch.md`
- [ ] **Une zone pilote, pas la France** : viser une densité dominante dans une métropole avant toute expansion. → `launch.md`
- [ ] **Chiffrer le coût d'acquisition, la marge et l'expansion.** → `cfo.md`, `summary.md`

## The competition

Recherche du 14/10/2026 sur sources publiques. Plusieurs sites étaient injoignables depuis mon environnement : certains chiffres viennent des extraits de recherche, pas de la page complète. Les concurrents côté particuliers (Archidvisor, Archibien) sont analysés dans `_v2-archibald-particuliers/competitors.md`.

### 1. Le tableau

| Concurrent / substitut | Type | Pour qui | Ce que ça fait | Prix | Source |
|---|---|---|---|---|---|
| **L'architecte lui-même, au téléphone** | Substitut n°1 | tous | « je trie en dix minutes au téléphone » : c'est la réponse la plus fréquente du panel | son temps | panel `panel/` (simulé) |
| **Formulaire de contact + agenda en ligne** (Calendly, formulaire Wix/WordPress) | Substitut | agences avec site | prise de rendez-vous, sans qualification | 0 à 15 €/mois | connaissance générale |
| **NextPhone**, réceptionniste IA « pour architectes » | Direct (US) | cabinets américains | répond au téléphone, qualifie, prend rendez-vous | non relevé | [getnextphone.com](https://www.getnextphone.com/ai-receptionist-for-architects) |
| **DocsBot**, chatbot sectoriel « architect services » | Direct (US) | cabinets | chatbot de site entraîné sur les documents du cabinet | non relevé | [docsbot.ai](https://docsbot.ai/industry/architect-services) |
| **Tars**, agent de génération de leads pour architectes d'intérieur | Direct (US) | décorateurs | qualification de prospects sur site | non relevé | [hellotars.com](https://webflow.hellotars.com/ai-agents/interior-design-lead-generation-ai-agent) |
| **Standards téléphoniques IA génériques** (CloudTalk et autres) | Indirect | TPE/PME | décroche, prend un message, transfère | environ 30 à 200 €/mois ; 99 € pour 200 min chez CloudTalk | [CloudTalk tarifs](https://www.cloudtalk.io/fr/tarifs-agent-vocal-ia/), [CloudTalk blog](https://www.cloudtalk.io/fr/blog/combien-coute-un-service-de-secretariat-telephonique-ia/) |
| **Logiciels de gestion d'agence** (Kolonell et autres) | Indirect, **copieur probable** | agences | honoraires, phases, temps, facturation | 30 à 80 €/utilisateur/mois (éditeur) | [Kolonell](https://kolonell.com/fr/blog/logiciel-gestion-cabinet-architecture-strasbourg-2026) |
| **Secrétariat téléphonique externalisé** | Substitut | agences | humain qui prend les messages | ~100 à 300 €/mois (ordre de grandeur, non vérifié) | — |
| **Annuaire de l'Ordre, Archidvisor, bouche-à-oreille** | Substitut au **réseau** | particuliers | trouver un architecte | gratuit / commission | `_v2-archibald-particuliers/competitors.md` |
| **Confrères entre eux** (« je l'envoie à un ami ») | Substitut au **réseau** | architectes | renvoi informel des demandes refusées | gratuit | panel `panel/` |

### 2. Le vide

**Je n'ai trouvé aucun agent de qualification en français, conçu pour les architectes**, qui connaisse le seuil des 150 m², le PLU et le coût réel des travaux, et qui remette un brief à l'architecte. Les produits spécialisés sont américains (NextPhone, DocsBot, Tars). Les outils français sont génériques (standards IA) ou ne gèrent pas l'accueil (logiciels d'agence). Une recherche sur les chatbots de cabinets d'architecture en France ne renvoie que des articles sur l'IA de conception ([Construires](https://www.construires.fr/ia-et-architecture-la-revolution-silencieuse-des-cabinets-francais/), [Médias24](https://medias24.com/agence-presse/une-petite-apprehension-lia-sinvite-timidement-dans-les-cabinets-darchitecture/)).

**Personne ne relie non plus les refus d'un architecte aux disponibilités d'un confrère.** C'est aujourd'hui informel, par téléphone, entre amis.

Le vide est **réel mais étroit**. Le panel le borne : il intéresse les agences qui reçoivent un flux de demandes froides par leur site ou leur téléphone (petites agences 44 %, architectes au carnet vide 67 %). Il n'intéresse presque pas ceux qui vivent du bouche-à-oreille (0 %).

### 3. La menace

- **La copie par un logiciel d'agence (le risque n°1).** Kolonell ou un concurrent peut ajouter un « assistant d'accueil » à son offre à 30-80 €/utilisateur. Ce qui protège Archibald : le savoir métier dans le brief, la donnée de conversion (quelles demandes aboutissent) et surtout **le réseau**, qu'un éditeur ne partagera pas entre ses clients.
- **L'arrivée en France d'un acteur américain** (NextPhone, DocsBot). C'est peu probable à court terme : le droit français de l'urbanisme, l'AI Act et le RGPD rendent la localisation coûteuse.
- **Les standards IA génériques qui baissent leurs prix.** Ils tirent la référence de prix vers le bas, et c'est pourquoi le prix doit s'appuyer sur le brief et le réseau, pas sur « un robot qui décroche ».

### 4. Les contraintes que tout concurrent subit aussi

- **AI Act, article 50** : depuis le 2 août 2026, un chatbot doit dire à l'utilisateur qu'il parle à une IA. Les amendes vont jusqu'à 15 M€ ou 3 % du chiffre d'affaires ([donneespersonnelles.fr](https://donneespersonnelles.fr/transparence-ia-article-50-ai-act), [jorijn.com](https://jorijn.com/en/blog/eu-ai-act-website-chatbot-disclosure-august-2026/)).
- **Code de déontologie des architectes** : la publicité, les honoraires et le démarchage sont encadrés ([CNOA, code de déontologie](https://architectes.org/sites/cnoa/files/2024-05/code_de_deontologie.pdf)). C'est un frein pour les copieurs non spécialisés, et un avantage pour qui obtient un avis favorable de l'Ordre.

### 5. Conclusion

Il n'y a pas de concurrent direct en France aujourd'hui, mais la barrière technique est faible. **La fenêtre est de 12 à 24 mois** : c'est le temps d'atteindre une densité de réseau dans 2 ou 3 métropoles et d'obtenir un avis de l'Ordre, avant qu'un éditeur de logiciel d'agence ne copie l'outil.

## The buyer panel

**20 buy · 80 pass** (20% buy) out of 100 simulated buyers. Seed 3101, so the same cards can be dealt again.

These are simulated buyers, not customers. Use this to find objections and weak spots, then confirm the big ones with real people before you spend.

### By segment

| group | buyers | buy rate |
| --- | ---: | ---: |
| Gérant d'une petite agence (2 à 10 personnes) | 25 | 44% |
| Architecte libéral seul, installé depuis longtemps | 25 | 20% |
| Architecte d'une agence plus grosse, orientée marchés publics et promoteurs | 10 | 10% |
| Architecte libéral seul, jeune installé (moins de 5 ans) | 40 | 8% |

### By buying behaviour

| group | buyers | buy rate |
| --- | ---: | ---: |
| Carnet vide, cherche du travail | 15 | 67% |
| Technophile | 12 | 58% |
| Noyé sous les demandes non qualifiées | 18 | 17% |
| Fait ses comptes au centime | 15 | 0% |
| Vit du bouche-à-oreille | 22 | 0% |
| Attaché à la déontologie | 8 | 0% |
| Méfiant envers l'IA | 10 | 0% |

### By income

| group | buyers | buy rate |
| --- | ---: | ---: |
| $63,000 and up | 35 | 34% |
| $38,000 to $63,000 | 32 | 22% |
| under $38,000 | 33 | 3% |

### Why they pass

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 33 | "Mon agence vit des marchés publics et des promoteurs, pas des particuliers qui arrivent par le site : je n'ai pas assez de ces demandes pour payer 79 € par mois. Et annoncer une fourchette d'honoraires avant le rendez-vous, c'est me lier les mains dans la négociation." (P001) · "Mes clients arrivent par recommandation, ils m'appellent directement et je cadre le projet moi-même au téléphone. Je n'ai pas un flux de demandes froides à filtrer qui justifie 79 € par mois sur mes 42 000 € annuels." (P006) |
| trust | 33 | "Je perds des heures sur des demandes qui n'aboutissent pas, donc le tri m'intéresse vraiment, mais je ne laisse pas une IA annoncer à un client ce que permet le PLU ou ce que coûtent ses travaux : s'il se trompe, c'est moi qui porte la faute. Et avec ce que je gagne, 79 € par mois pour un outil auquel je ne fais pas confiance, c'est non." (P002) · "Mes clients viennent d'anciens clients qui leur ont donné mon numéro : ils veulent m'entendre moi, pas une IA, et je ne vais pas confier leurs projets et leurs budgets à un outil dont je ne sais pas où il stocke les données. Avec ce que je gagne, près de 950 € par an pour filtrer des demandes que je reçois déjà au compte-gouttes, ça ne se justifie pas." (P003) |
| price | 11 | "79 € par mois, c'est presque 1 000 € par an pour trier des demandes que je trie déjà moi-même en dix minutes au téléphone. Avec mes honoraires serrés, je ne prends pas un abonnement de plus tant que je n'ai pas la preuve qu'il me rapporte des projets." (P012) · "79 € par mois, c'est près de 1 000 € par an pour trier des demandes que je trie déjà moi-même au téléphone en dix minutes ; avec mes revenus, je ne rajoute pas un abonnement de plus, même avec l'essai gratuit, parce que je sais que je finirais par le résilier." (P029) |
| values | 2 | "Je reçois peu de demandes, je les trie moi-même au téléphone depuis trente ans, et je ne vais pas mettre une IA entre moi et un futur client ni envoyer mes refus chez les confrères. 79 € par mois, c'est près de mille euros par an pour un problème que j'ai une fois par mois." (P035) · "Je ne laisse pas une IA annoncer des fourchettes d'honoraires et orienter mes prospects vers des confrères en mon nom sans savoir ce qu'en pense l'Ordre. Et transmettre les demandes que je refuse, c'est nourrir la concurrence, pas mon agence." (P053) |
| other | 1 | "Le tri des demandes, ça m'intéresse vraiment, la moitié ne mènent à rien. Mais un robot qui annonce une fourchette d'honoraires avant même que j'aie vu le client, c'est me lier les mains, et je ne paie pas 79 € par mois pour ça. J'activerais peut-être l'essai par curiosité, mais je ne vois pas aujourd'hui ce qui me ferait payer ensuite." (P032) |

### Why they buy

| reason | buyers | in their words |
| --- | ---: | --- |
| need | 16 | "Je rate des appels en chantier et je perds du temps avec des demandes de 20 m² sans budget ; l'essai gratuit sans engagement, je le lance tout de suite, et les demandes déclinées par des confrères m'intéressent vraiment quand on vient de s'installer. Si au bout de 30 jours il m'a ramené ou trié au moins un vrai projet, je garde les 79 €, même si c'est une vraie ligne dans mon budget." (P005) · "Mon carnet est vide, donc tout ce qui peut m'amener des clients, je le teste, surtout avec 30 jours gratuits et sans engagement. Ce qui m'intéresse, ce n'est pas le tri : c'est de recevoir les demandes que les autres déclinent dans ma spécialité." (P007) |
| convenience | 4 | "Je passe mes soirées sur des permis et je perds trop de temps en premiers rendez-vous avec des gens qui n'ont ni le budget ni besoin d'un architecte ; 30 jours d'essai gratuit, sans engagement, j'aime tester ce genre d'outil, donc je l'installe et je juge sur pièces." (P040) · "J'aime tester ces outils et l'essai gratuit sans engagement ne me coûte rien ; si ça m'évite de rappeler entre deux visites de chantier des gens qui veulent une extension de 20 m² avec 15 000 €, je le garde, sans doute avec l'option téléphone." (P049) |

### What would flip a no

- Pouvoir désactiver complètement la fourchette d'honoraires et voir sur l'essai qu'il me trie réellement plusieurs demandes par mois que je traite aujourd'hui à la main.
- Qu'il se contente de poser les questions et de me faire le brief, sans rien affirmer au client sur le PLU ni le budget, et que je puisse le tester sur mes vraies demandes pendant l'essai.
- Un hébergement en France clairement garanti et conforme RGPD, validé ou recommandé par l'Ordre ou un confrère que je connais, et une formule téléphone seule moins chère pour ne plus rater d'appels sur le chantier.
- Qu'un confrère que je connais l'utilise depuis des mois et me montre que ses clients ne s'en plaignent pas et qu'il en a tiré des projets réels qui couvrent largement l'abonnement.
- Que le réseau de transmission entre confrères m'apporte vraiment des projets dans ma spécialité, preuves à l'appui, sans que l'agent n'annonce de chiffre d'honoraires.
- Un avis écrit de l'Ordre (ou du CNOA) confirmant que l'outil, l'affichage d'honoraires par l'IA et la transmission entre confrères sont conformes au code de déontologie, plus la possibilité de désactiver la fourchette d'honoraires et le filtrage pour ne garder que la prise de rendez-vous et le brief.
- La preuve concrète que le réseau de confrères m'envoie des demandes réelles dans ma zone et ma spécialité, par exemple un nombre de projets transmis garanti pendant l'essai.
- Une preuve concrète que le réseau m'apporterait des demandes réelles dans ma spécialité et ma zone (nombre d'architectes abonnés et de demandes transmises près de chez moi), avec un hébergement des données en France clairement expliqué.
- Une preuve chiffrée que le réseau m'apporte au moins un vrai projet signé dans ma spécialité pendant l'essai, ou un prix autour de 30-40 € pour une petite structure comme la mienne.
- Un avis écrit ou une validation de l'Ordre des architectes confirmant que l'outil et l'échange de demandes entre confrères sont conformes à la déontologie.
- Que le réseau de confrères m'envoie réellement des projets dans ma spécialité, prouvé pendant l'essai, avec la possibilité de couper complètement l'affichage des honoraires dans le brief.
- Que les demandes reçues des confrères m'apportent réellement des projets signés pendant l'essai, de quoi couvrir largement l'abonnement.

Buyers say they would buy **1.0 times** in the first month on average.

100 buyers gave all four price answers. Run founder-pricing's van_westendorp.py on the answers folder.

## Pricing

> L'outil affiche « $ » : lisez **euros HT par mois** (offre de base). Les panels sont simulés : ils servent à choisir quoi tester, pas à prouver.

### Ce que disent les panels

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

### Ce dont l'entreprise a besoin (`cfo.md`)

| prix | marge par abonné | point mort | année 1 |
|---|---:|---:|---:|
| 29 € | 8 € | 469 abonnés | -33 760 € |
| **39 €** | **18 €** | **209 abonnés** | **-19 710 €** |
| 49 € | 28 € | 134 abonnés | -5 660 € |
| 59 € | 38 € | 99 abonnés | +8 390 € |

### 1. Le prix recommandé : une échelle à deux marches

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

### 2. Ce qu'il faut tester en premier

- **Test A (pilote, 30 jours)** : sur 20 agences, comparer l'affichage de « 39 € » à celui de « 49 € avec le téléphone inclus ». Mesurer la conversion de l'essai vers le payant.
- **Test B** : chez les libéraux, mesurer le taux d'activation de la formule à la demande et le nombre moyen de briefs par mois. Si la moyenne dépasse 7 briefs, la formule rapporte plus que 35 €… mais elle est plafonnée, donc on vérifie qu'elle reste rentable (coût d'environ 0,50 € par brief).
- **Ne pas tester** : une commission sur les projets transmis (rejetée pour raisons de déontologie dans trois versions), ni un prix sous 29 €.

### 3. Ce que le prix ne règle pas

Le prix ne règle ni la confiance (« s'il se trompe, c'est moi qui porte la faute »), ni l'Ordre, ni les données. Ces points se traitent dans l'offre (`offer.md`) et les opérations (`ops.md`), pas dans le tarif.

## The offer

### La chose unique (demandée par la lentille Produit)

> **« Vos demandes arrivent avec un brief. Vous ne rappelez que les bons projets. »**

Une seule promesse au lancement : **le brief privé, prêt avant le premier appel**. Le PLU, le budget et le seuil des 150 m² y figurent comme des **alertes pour l'architecte**, jamais comme des réponses données au client. Le réseau est un **bonus optionnel**, pas la promesse.

### 1. Les obstacles, dans les mots des panels

**Côté architectes (140 réponses, v1 + v2) :**
1. « Je n'ai pas de flux de demandes froides : mes clients viennent par recommandation. » (n°1, besoin)
2. « S'il se trompe sur le PLU ou le budget devant le client, c'est moi qui porte la faute. » (confiance)
3. « Une fourchette d'honoraires annoncée avant le rendez-vous me lie les mains. » (levé en v2)
4. « Mes clients veulent me parler à moi, pas à une IA. »
5. « Hébergé en France, d'accord, mais quel modèle d'IA, et quels sous-traitants voient les données ? »
6. « L'Ordre n'a pas rendu d'avis. » En v2, la phrase « avis demandé » a **aggravé** cette objection.
7. « Transmettre mes refus à un confrère, c'est nourrir la concurrence. »
8. « Le réseau ne vaut que s'il y a du monde dans mon département. » (carnets vides)
9. « 39 €, c'est une ligne de plus : je viens de résilier des logiciels. »

**Côté clients finaux (20 réponses, 75 % l'utiliseraient) :**
1. « Une fourchette ce n'est pas un devis, et ma banque veut un devis. »
2. « Je veux un rappel de l'architecte sous 48 h, sinon je vais ailleurs. »
3. « Je ne donne pas mon budget ni mon adresse à un robot sans savoir où ça va. »
4. « Est-ce que l'architecte lit vraiment le récapitulatif ? »

### 2. Les solutions retenues (valeur ↑ / coût ↓)

| solution | répond à | coût |
|---|---|---|
| **Formule à la demande** (5 € par brief, 0 € fixe) | archi 1, 9 ; et réseau 8 | aucun |
| **Mode « prise de brief »** : l'agent n'affirme rien au client, toute l'analyse va dans le brief privé avec ses sources | archi 2, 3 | déjà fait en v2 |
| **Mode « message seul »** au téléphone, sans questionnaire, pour les clients recommandés | archi 4 | faible |
| **Une phrase de l'architecte** en ouverture (« Bonjour, je suis l'assistant de Claire Martin, architecte : elle lit chaque demande et vous rappelle sous 48 h ») | archi 4 ; client 2, 4 | aucun |
| **Engagement de rappel sous 48 h** affiché au client, avec une relance automatique à l'architecte au bout de 24 h | client 2, 4 | aucun |
| **Page de transparence** : le modèle d'IA, la liste des sous-traitants avec leur pays, « zéro entraînement », la durée de conservation, et le DPA téléchargeable **avant** l'essai | archi 5 ; client 3 | juridique, compris dans le démarrage |
| **Ne plus parler de l'Ordre** dans la communication tant qu'aucun avis n'est rendu. À la place : « relu par un avocat en déontologie des architectes » et des **témoignages de confrères nommés** | archi 6 | 1 500 € d'avocat |
| **Réseau ouvert seulement quand la densité est atteinte** : compteur public « 23 confrères à Lyon » ; un architecte peut **recevoir** sans **envoyer** | archi 7, 8 | aucun |
| **Brief « bancable »** : une liste des pièces que la banque demandera, et la mention claire que ce n'est pas un devis | client 1 | faible |
| **Garantie** : si le premier mois payant ne vous a pas apporté au moins 3 briefs, il est remboursé | archi 1, 9 | faible |

**Écartés :** une commission sur les projets transmis (déontologie), la fourchette d'honoraires montrée au client, et une offre gratuite permanente (elle tuerait la valeur perçue).

### 3. La pile (ce que l'architecte reçoit)

1. L'agent sur le site, sur la fiche Google et dans la signature e-mail.
2. Le brief PDF privé : besoin d'un architecte, alertes PLU avec sources, écart de budget, pièces à demander.
3. Trois boutons : rappeler, décliner poliment, décliner et proposer un confrère.
4. Le tableau de bord mensuel : demandes, briefs, heures estimées économisées.
5. En option, le téléphone : prise de message en chantier.
6. En option, le réseau : recevoir, et éventuellement envoyer, les demandes déclinées dans sa spécialité.

### 4. Le pitch réécrit (v3, à tester sur de vrais architectes)

> Archibald, l'assistant d'accueil de votre agence. Vos demandes arrivent avec un brief : surface, parcelle, budget, délai, et les points de PLU à vérifier, avec leurs sources. L'assistant ne promet rien au client : il dit qu'il est une IA, que vous lisez chaque demande et que vous rappelez sous 48 h. Vous ne rappelez que les bons projets ; les autres reçoivent un refus poli, écrit par vous.
> **5 € par demande reçue, sans abonnement.** Ou 39 € HT par mois en illimité pour les agences. Le premier mois est remboursé s'il ne vous apporte pas 3 briefs. Données en France, sous-traitants listés, aucun entraînement sur vos données.

### 5. Avant / après (panels simulés)

| | v1 (79 €) | v2 (39 €, mode brief) |
|---|---:|---:|
| adhésion | 20 % (20/100) | 22 % (9/40) |
| petites agences | 44 % | 30 % |
| jeunes libéraux | 8 % | 25 % |
| technophiles / noyés / carnets vides | 58 / 17 / 67 % | 60 / 43 / 50 % |
| bouche-à-oreille / méfiants IA | 0 / 0 % | 0 / 0 % |
| refus « prix » | 11 | 2 |

**À retenir :** la v2 a fait disparaître l'objection du prix et celle des honoraires, mais pas l'objection du besoin. Archibald n'a **pas** de marché chez les architectes qui vivent de la recommandation, et ne doit pas le chercher. La cible est le segment qui reçoit des demandes de gens qu'il ne connaît pas, plus les carnets vides qui veulent le réseau. La formule à la demande et le réseau « recevoir sans envoyer » ont été conçus **après** le re-test et **n'ont pas encore été testés**.

## The numbers

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

## Unit economics: Archibald : assistant d'accueil IA pour agences d'architecture, avec réseau de renvoi entre confrères (France)

Every number below comes from the input file. Nothing is looked up or guessed.

### One abonné-mois (volumes = abonnés actifs PAR MOIS)

| line | per abonné-mois (volumes = abonnés actifs PAR MOIS) |
| --- | ---: |
| Price | $39.00 |
| IA (LLM) : ~30 conversations + briefs par mois x 0,10 EUR (ESTIMATION) | -$3.00 |
| Hébergement France/UE, stockage, envoi des PDF (ESTIMATION) | -$2.00 |
| Support et paramétrage : ~10 min par abonné et par mois x 30 EUR/h (ESTIMATION) | -$5.00 |
| Frais d'encaissement ~2,5 % (ESTIMATION) | -$1.00 |
| Acquisition amortie : 250 EUR par abonné / 25 mois de durée de vie (attrition 4 %/mois) (ESTIMATION) | -$10.00 |
| **Contribution** (what each abonné-mois (volumes = abonnés actifs PAR MOIS) leaves to pay the fixed costs) | **$18.00** (46%) |

### The margin that matters

Fixed costs: $3,750 a month (Rémunération fondateur (minimum, ESTIMATION) $2,500, Contenu, Instagram, salons et événements locaux (ESTIMATION) $500, Outils, monitoring, CRM, hébergement de base (ESTIMATION) $300, Expert-comptable + banque (ESTIMATION) $250, Assurance RC pro éditeur + DPO externe mutualisé (ESTIMATION) $200).

- **Break-even: 209 abonné-mois (volumes = abonnés actifs PAR MOIS)s a day.** Below that you lose money every month.
- **Profit margin at your plan** (300 a day): **14%** of every sale, after every cost.

### Year 1, month by month

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

### What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 14% | 209 | -$19,710 |
| Price -10% | 5% | 266 | -$25,190 |
| Volume -20% | 6% | 209 | -$24,768 |
| Unit costs +15% | 6% | 253 | -$24,136 |

### Red flags

- Year 1 loses money on operations (-$19,710).
- The startup spend is not earned back within year 1.

## Marketing

### 1. La cible exacte (d'après les panels)

**Oui :**
- les petites agences de 2 à 10 personnes qui ont un site et une fiche Google ;
- les libéraux technophiles ;
- ceux qui se disent « noyés sous les demandes de 20 m² sans budget » ;
- les jeunes installés au carnet vide (pour le réseau, en formule à la demande).

**Non (0 % dans les deux panels) :** les architectes qui vivent du bouche-à-oreille, ceux qui se méfient de l'IA, les agences tournées vers les marchés publics et les promoteurs. **On ne dépense pas un euro pour les convaincre.**

**Le signal qui qualifie un prospect :** il a un **formulaire de contact ou une fiche Google avec des avis**. Ça se vérifie en 10 secondes, sans l'appeler.

### 2. Le message

- **Accroche :** « Vos demandes arrivent avec un brief. »
- **Preuve :** un vrai brief PDF montré en entier (anonymisé), pas une capture d'interface.
- **Chiffre :** « 5 € la demande, ou 39 € par mois en illimité ». On ne parle jamais d'« IA révolutionnaire ».
- **À ne pas dire :** « l'Ordre a été saisi », « remplace votre secrétariat », « leads ».

### 3. Les canaux, par ordre

| # | canal | pourquoi | coût | objectif à 90 jours |
|---|---|---|---|---|
| 1 | **Prospection directe dans la ville pilote** : liste des agences avec formulaire et fiche Google (Pages Jaunes, Google Maps, annuaire de l'Ordre), e-mail personnalisé avec un **brief d'exemple sur leur ville**, puis un appel | le segment est petit et listable | temps du fondateur | 300 agences contactées, 40 essais |
| 2 | **Démonstration sur leur propre site** : « voici ce qu'aurait donné la dernière demande que vous avez reçue » (en 15 min, en visio) | lève l'objection « je veux voir sur pièces » | temps | 50 % des démos en essai |
| 3 | **LinkedIn** du fondateur : un brief commenté par semaine (« ce que cette demande de 25 m² à 18 000 € cachait ») | les architectes y discutent métier | 0 € | 1 000 abonnés ciblés |
| 4 | **Instagram @monprojetarchi** retourné vers les **particuliers** : « préparer son rendez-vous avec un architecte », qui renvoie vers les agences abonnées | nourrit la demande du réseau | 0 € à 200 €/mois | du trafic vers les abonnés |
| 5 | **Écoles d'architecture et maisons de l'architecture** : une intervention « s'installer et trouver ses premiers clients » | c'est là que sont les carnets vides | déplacements | 50 inscrits à la demande |
| 6 | **Parrainage** : 1 mois offert aux deux confrères | la recommandation entre confrères est le canal de confiance n°1 du panel | 39 € | 20 % des nouveaux |
| 7 | *Plus tard :* partenariats avec les éditeurs de sites d'architectes, les logiciels d'agence et les syndicats (UNSFA) | effet de levier | négocié | après 100 abonnés |

**Pas de publicité payante** avant d'avoir mesuré la conversion de l'essai vers le payant. Le coût d'acquisition cible est de 250 € maximum (`cfo.md`).

### 4. Le tunnel, avec les chiffres à mesurer

Prospect contacté → démo (objectif 15 %) → essai de 30 jours (objectif 50 % des démos) → payant (objectif 50 % des essais) → 6 mois plus tard, toujours abonné (objectif 80 %).

Avec ces taux, 300 contacts donnent environ 11 abonnés par vague. C'est cohérent avec la rampe du CFO (10, puis 20, puis 35 abonnés).

### 5. Le calendrier des 90 premiers jours

- **Semaines 1 à 2 :** page de transparence, brief d'exemple par quartier, liste des 300 agences de la ville pilote.
- **Semaines 3 à 6 :** 20 démos, 10 essais pilotes gratuits contre un témoignage.
- **Semaines 7 à 12 :** les premiers témoignages nommés, le compteur réseau public, le lancement payant, le parrainage.

## Brand

### 1. Le nom

**On garde « Archibald ».** Un prénom convient bien à un assistant : le client lit « l'assistant de l'agence », l'architecte lit « Archibald ». Le produit s'appelle **« Archibald, l'assistant d'accueil des architectes »**.

- **Ce qui ne change pas :** le compte Instagram **@monprojetarchi** reste tourné vers les particuliers (voir `marketing.md`). La marque B2B vit sur LinkedIn et dans le brief PDF.
- **Vérifications à faire vous-même** (je n'ai pas pu interroger les registres) :
  - [INPI](https://data.inpi.fr/) et [EUIPO](https://euipo.europa.eu/eSearch/), classes **9** (logiciel), **42** (SaaS) et **35** ;
  - les noms de domaine ([AFNIC](https://www.afnic.fr/)) ;
  - la validation par un conseil en propriété industrielle.

### 2. Promesse et voix

- **La promesse :** *« Vos demandes arrivent avec un brief. »*
- **Signatures :**
  1. « Ne rappelez que les bons projets. »
  2. « L'assistant qui ne parle pas à votre place. »
  3. « Pas le plus connu. Le plus compatible avec votre projet. » (pour le réseau et le grand public)
- **La voix :**
  - **Discrète** (c'est l'agence qui est en avant) : faire « Claire Martin lit chaque demande » ; ne pas faire « Archibald, votre IA ».
  - **Prudente** : faire « points de PLU à vérifier » ; ne pas faire « votre projet est faisable ».
  - **Transparente** : faire « Je suis l'assistant IA de l'agence » dès la première phrase. C'est l'AI Act, et c'est aussi la confiance.

### 3. Le look (brief)

- **Couleurs** (reprises des versions précédentes, contrastes vérifiés) :
  - **Encre** `#1F2A2E` sur **Papier** `#F6F3EE` : 13,3:1 (AAA) ;
  - **Bois** `#A84A25` pour les accents : 5,17:1 sur Papier (AA).
- **Typographie :** Fraunces pour les titres, Inter pour le texte (SIL OFL, [Google Fonts](https://fonts.google.com/)).
- **Le widget prend les couleurs de l'agence.** Archibald n'apparaît qu'en petit (« propulsé par Archibald »). Ce « propulsé par » est aussi le canal d'acquisition gratuit.
- **Logo :** un « A » tracé comme un trait d'architecte. Il doit fonctionner en 16 px dans le widget.

### 4. Les 5 premiers points de contact

1. **Le brief PDF** : c'est le produit qu'on voit, il doit être beau.
2. La première phrase du widget.
3. Le message de refus poli, que l'architecte relit et signe.
4. La page de transparence (données, sous-traitants, IA).
5. L'e-mail du tableau de bord mensuel : « 14 demandes, 9 briefs, environ 6 h économisées ».

## Operations

> Ce n'est pas un conseil juridique. Faites valider les points 1 à 4 par un avocat (droit du numérique) et un conseil en déontologie avant le lancement payant.

### 1. Les obligations légales (avant le premier client payant)

| sujet | ce qu'il faut faire | pourquoi |
|---|---|---|
| **AI Act, article 50** | La première phrase de l'agent dit qu'il est une IA (« Je suis l'assistant IA de l'agence X »). Le PDF le mentionne aussi. | Obligatoire depuis le 2 août 2026 ; amendes jusqu'à 15 M€ ou 3 % du CA ([donneespersonnelles.fr](https://donneespersonnelles.fr/transparence-ia-article-50-ai-act)) |
| **RGPD : rôles** | L'architecte est **responsable de traitement**, Archibald est **sous-traitant**. Un contrat de sous-traitance (DPA, art. 28) est signé à l'abonnement. | Les données client (adresse, budget) sont des données personnelles |
| **RGPD : sous-traitants ultérieurs** | Une liste publique et datée : hébergeur, fournisseur du modèle d'IA, envoi d'e-mails, avec le pays de chacun. Contrat « zéro rétention, zéro entraînement » chez le fournisseur IA. | C'est l'objection n°2 du re-test : « hébergé en France, mais qui voit les données ? » |
| **RGPD : client final** | Une mention d'information dans la conversation, une durée de conservation (par ex. 12 mois sans suite), une suppression à la demande | Droits des personnes |
| **Option réseau** | Le transfert à un confrère se fait seulement avec un **consentement explicite du client** (case non cochée) et une activation par l'architecte. | Un nouveau destinataire des données, donc un consentement distinct |
| **Déontologie** | Le contenu de l'agent est relu par un avocat en droit des professions réglementées. Une saisine de l'Ordre (CNOA) est faite **avant** de communiquer dessus. **On ne mentionne pas l'Ordre dans la publicité tant qu'aucun avis n'est rendu.** | Code de déontologie ([CNOA](https://architectes.org/sites/cnoa/files/2024-05/code_de_deontologie.pdf)). Dans le re-test, la phrase « avis demandé » a **réveillé** la méfiance au lieu de rassurer. |
| **Responsabilité** | L'agent n'affirme rien au client. Le brief est marqué « aide à la préparation, à vérifier par l'architecte », avec les sources PLU (lien vers le document d'urbanisme). CGV avec une limitation de responsabilité. RC pro éditeur. | « S'il se trompe, c'est moi qui porte la faute » (objection n°1 du panel v1) |

### 2. Le flux quotidien

1. Un client arrive sur le site de l'agence, ou appelle (option téléphone).
2. L'agent se présente comme une IA, pose 8 à 12 questions, sans rien affirmer.
3. Le brief PDF privé part à l'architecte en moins d'une minute, avec ses alertes : budget, seuil des 150 m², points de PLU à vérifier.
4. L'architecte clique sur l'un des trois boutons : **rappeler** (un créneau est proposé au client), **décliner** (le message type, validé par l'architecte, part chez le client), ou **décliner et proposer un confrère** (si l'option réseau est active et que le client y consent).
5. Le client reçoit une réponse sous 48 h. C'est l'engagement demandé par le panel clients (« un rappel sous 48 h, sinon je vais ailleurs »). Une relance automatique part vers l'architecte au bout de 24 h.

### 3. Qualité et mesure

- **Taux d'exactitude du brief** : l'architecte note chaque brief (pouce haut ou bas, plus un champ libre). L'objectif est ≥ 90 % de briefs jugés « justes » sur 50 briefs avant d'ouvrir une 2e ville.
- **Taux d'abandon de la conversation côté client** : l'objectif est < 30 %. Au-delà, on raccourcit le questionnaire.
- **Délai de rappel** par l'architecte : il est affiché à l'architecte, mais jamais publié.
- **Le réseau** : demandes transmises, acceptées par le confrère, puis transformées en rendez-vous.

### 4. Fournisseurs et outils

- Un hébergement en France (OVHcloud, Scaleway ou équivalent), en vérifiant leurs offres de modèles d'IA hébergés en UE.
- Un fournisseur de modèle IA avec contrat UE et zéro rétention. Une solution de repli chez un second fournisseur.
- La téléphonie (option) via un opérateur de voix IA, avec des numéros français.
- Le paiement par prélèvement SEPA ou carte, des factures HT automatiques.

### 5. Risques opérationnels

| risque | parade |
|---|---|
| L'agent répond quelque chose de faux au client | Le mode « prise de brief » interdit toute affirmation. Des tests automatiques sur 100 conversations type tournent avant chaque mise à jour. |
| Panne du fournisseur IA | Un fournisseur de secours, et sinon un formulaire classique en repli |
| Plainte d'un client final | Une réponse du fondateur sous 24 h, et le droit de suppression appliqué immédiatement |
| Un architecte reçoit trop peu de demandes | Un tableau de bord mensuel « X demandes, Y heures économisées ». En dessous de 3 demandes par mois, on propose la formule à la demande (voir `pricing.md`). |

## Launch plan

### Le principe

**Une métropole, pas la France.** Il faut la densité pour le réseau, et le contact direct pour la confiance. On choisit une ville où le fondateur a un réseau (par exemple Lyon, Bordeaux ou Nantes) et on y vise **20 % des petites agences qui ont un formulaire de contact** avant d'ouvrir une 2e ville.

### Étape 0 : avant de coder quoi que ce soit (2 semaines)

**10 vraies conversations** avec des architectes du segment cible (agences avec site, technophiles, jeunes installés). Pas de pitch : on leur pose ces questions :
1. Combien de demandes avez-vous reçues le mois dernier ? Par quel canal ? Combien ont abouti ?
2. Racontez-moi la dernière demande qui vous a fait perdre du temps.
3. Que faites-vous aujourd'hui des demandes que vous déclinez ?

**Seuil pour continuer :** au moins 6 architectes sur 10 reçoivent **4 demandes froides ou plus par mois**. Sinon, le segment est trop petit et on s'arrête là. C'est le chiffre que le conseil juge décisif, et aucun panel ne peut le donner.

### Étape 1 : le pilote (60 jours, 10 à 20 architectes, gratuit contre témoignage)

- Installation faite par le fondateur, en 30 minutes.
- **Ce qu'on mesure chaque semaine :**

| indicateur | seuil de réussite | seuil d'arrêt |
|---|---|---|
| Demandes reçues par architecte et par mois | ≥ 4 | < 2 |
| Clients finaux qui vont au bout de la conversation | ≥ 70 % | < 50 % |
| Briefs jugés « justes » par l'architecte | ≥ 90 % sur 50 briefs | < 75 % |
| Heures économisées déclarées par mois | ≥ 3 h | < 1 h |
| Plaintes de clients finaux sur l'IA | ≤ 1 sur 50 conversations | > 5 |
| Pilotes qui disent « je paierais 39 € » à la fin | ≥ 50 % | < 25 % |

### Étape 2 : le lancement payant dans la ville pilote (mois 3 à 6)

- Formules à la demande et Agence, plus la garantie du premier mois.
- Prospection directe : 300 agences, 20 démos par mois (`marketing.md`).
- **Ouvrir le réseau** quand il y a au moins 15 abonnés dans la ville, dont 5 qui **reçoivent** (carnets vides).
- **Objectif au mois 6 : 90 abonnés payants** (la rampe du CFO), une attrition de 5 % par mois au maximum, et une première demande transmise par le réseau qui se transforme en rendez-vous.

### Étape 3 : la 2e et la 3e ville (mois 7 à 12)

On les ouvre seulement si les seuils de l'étape 2 sont tenus. **Objectif au mois 12 : 270 abonnés**, au-dessus du point mort de 209.

### Les choses à faire cette semaine

1. Écrire la liste des 300 agences de la ville pilote : nom, site, formulaire oui ou non, nombre d'avis Google.
2. Appeler 10 architectes pour l'étape 0.
3. Préparer un brief d'exemple anonymisé.
4. Demander un devis à un avocat en déontologie des professions réglementées pour le contenu de l'agent et les CGV.

### Ce qui ferait tout arrêter

- Moins de 6 architectes sur 10 avec un vrai flux de demandes froides à l'étape 0.
- Des briefs faux plus d'une fois sur quatre.
- Un avis défavorable de l'Ordre sur l'accueil par une IA, ou sur la transmission entre confrères. Dans ce cas, on retire le réseau et on garde l'outil seul.

_The panel is simulated buyers and the numbers are projections from your inputs. Confirm demand with real customers and costs with real quotes before you spend. Not financial, legal or tax advice._
