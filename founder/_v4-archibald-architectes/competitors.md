# Concurrents : Archibald, l'agent IA pour architectes

Recherche du 14/10/2026 sur sources publiques. Plusieurs sites étaient injoignables depuis mon environnement : certains chiffres viennent des extraits de recherche, pas de la page complète. Les concurrents côté particuliers (Archidvisor, Archibien) sont analysés dans `_v2-archibald-particuliers/competitors.md`.

## 1. Le tableau

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

## 2. Le vide

**Je n'ai trouvé aucun agent de qualification en français, conçu pour les architectes**, qui connaisse le seuil des 150 m², le PLU et le coût réel des travaux, et qui remette un brief à l'architecte. Les produits spécialisés sont américains (NextPhone, DocsBot, Tars). Les outils français sont génériques (standards IA) ou ne gèrent pas l'accueil (logiciels d'agence). Une recherche sur les chatbots de cabinets d'architecture en France ne renvoie que des articles sur l'IA de conception ([Construires](https://www.construires.fr/ia-et-architecture-la-revolution-silencieuse-des-cabinets-francais/), [Médias24](https://medias24.com/agence-presse/une-petite-apprehension-lia-sinvite-timidement-dans-les-cabinets-darchitecture/)).

**Personne ne relie non plus les refus d'un architecte aux disponibilités d'un confrère.** C'est aujourd'hui informel, par téléphone, entre amis.

Le vide est **réel mais étroit**. Le panel le borne : il intéresse les agences qui reçoivent un flux de demandes froides par leur site ou leur téléphone (petites agences 44 %, architectes au carnet vide 67 %). Il n'intéresse presque pas ceux qui vivent du bouche-à-oreille (0 %).

## 3. La menace

- **La copie par un logiciel d'agence (le risque n°1).** Kolonell ou un concurrent peut ajouter un « assistant d'accueil » à son offre à 30-80 €/utilisateur. Ce qui protège Archibald : le savoir métier dans le brief, la donnée de conversion (quelles demandes aboutissent) et surtout **le réseau**, qu'un éditeur ne partagera pas entre ses clients.
- **L'arrivée en France d'un acteur américain** (NextPhone, DocsBot). C'est peu probable à court terme : le droit français de l'urbanisme, l'AI Act et le RGPD rendent la localisation coûteuse.
- **Les standards IA génériques qui baissent leurs prix.** Ils tirent la référence de prix vers le bas, et c'est pourquoi le prix doit s'appuyer sur le brief et le réseau, pas sur « un robot qui décroche ».

## 4. Les contraintes que tout concurrent subit aussi

- **AI Act, article 50** : depuis le 2 août 2026, un chatbot doit dire à l'utilisateur qu'il parle à une IA. Les amendes vont jusqu'à 15 M€ ou 3 % du chiffre d'affaires ([donneespersonnelles.fr](https://donneespersonnelles.fr/transparence-ia-article-50-ai-act), [jorijn.com](https://jorijn.com/en/blog/eu-ai-act-website-chatbot-disclosure-august-2026/)).
- **Code de déontologie des architectes** : la publicité, les honoraires et le démarchage sont encadrés ([CNOA, code de déontologie](https://architectes.org/sites/cnoa/files/2024-05/code_de_deontologie.pdf)). C'est un frein pour les copieurs non spécialisés, et un avantage pour qui obtient un avis favorable de l'Ordre.

## 5. Conclusion

Il n'y a pas de concurrent direct en France aujourd'hui, mais la barrière technique est faible. **La fenêtre est de 12 à 24 mois** : c'est le temps d'atteindre une densité de réseau dans 2 ou 3 métropoles et d'obtenir un avis de l'Ordre, avant qu'un éditeur de logiciel d'agence ne copie l'outil.
