# Pivot : Archibald Rénov, le commercial IA des entreprises de rénovation

*Recherche du 20/10/2026. Tous les panels sont **simulés** : ils servent à choisir quoi tester, pas à prouver. Les montants sont en euros HT.*

## 1. Pourquoi pivoter

| version | client payeur | adhésion |
|---|---|---:|
| v1 ArchiMatch / v2 Archibald particuliers | particuliers et architectes, commission | faible |
| v3 Relais | intermédiaires du retail | 75 % (20 répondants, niche étroite) |
| v4 Agent pour architectes, 79 € | architectes | 20 % (100 répondants) |
| v4 re-test, 39 € | architectes | 22 % (40 répondants) |

Les architectes vivent surtout du bouche-à-oreille, et ces architectes-là n'achètent pas, à aucun prix (0 % dans tous les panels). **Le problème n'est ni le produit ni le prix, c'est le client.**

## 2. Les trois pistes testées (20 répondants chacune)

| piste | prix | adhésion | ce qui bloque |
|---|---|---:|---|
| **Rénov** : l'agent vendu aux entreprises de rénovation, d'extension et aux constructeurs | 149 €/mois | **55 %** | « mes clients veulent un humain » |
| Réseau d'architectes : abonnement pour recevoir des projets qualifiés | 49 €/mois | 20 % | « projet envoyé à 3 confrères = guerre des prix » |
| Courtiers : dossier travaux prêt pour la banque | 39 €/dossier | 20 % | « la banque veut des devis signés » ; « ma franchise impose ses outils » |

**Rénov gagne nettement.** Ces entreprises ont ce qui manquait aux architectes : un **flux de demandes entrantes**, des **leads achetés** (partagés avec 3 concurrents) et des **commerciaux débordés**.

## 3. Trois versions de l'offre Rénov

Les versions v2 et v3 ont été testées sur **exactement les mêmes 40 profils** (seed 4201) : la comparaison est directe.

| version | promesse | prix | adhésion |
|---|---|---|---:|
| v1 | assistant d'accueil qui qualifie et propose un créneau | 149 € | 55 % (20 répondants) |
| v2 | « il décroche seulement quand vous ne pouvez pas » | 99 € | **42 %** (40 répondants) |
| **v3** | **« plus de chantiers signés avec les mêmes demandes »** : 1. rappel en moins de 60 s de chaque lead, plateformes comprises ; 2. pré-qualification avant de se déplacer ; 3. relance des devis à J+3, J+10 et J+20 | **149 €** | **60 %** (40 répondants) |

**La leçon :** baisser le prix et rendre l'outil discret (v2) a **fait baisser** l'adhésion. Ce qui fait acheter, c'est de toucher **l'argent** : les leads payés perdus parce qu'on rappelle trop tard, les visites pour rien, les devis qui dorment. La v3 fait mieux à 149 € que la v2 à 99 €.

**Qui achète la v3 :**
- par comportement : commerciaux débordés 100 %, déjà équipés d'outils numériques 100 %, acheteurs de leads 80 % ;
- par segment : spécialistes de l'extension et de la surélévation 70 %, franchisés 67 %, rénovation globale 56 %, constructeurs de maisons 50 % ;
- ceux qui n'achètent pas : le bouche-à-oreille 0 %, les méfiants envers l'IA 0 %. **On ne les cible pas.**

**Le prix :**
- fourchette acceptable de 40 à 249 €/mois ;
- point d'indifférence à 100 € ;
- médianes : bonne affaire à 79 €, cher à 199 €.

149 € est accepté parce qu'un seul chantier signé en plus (20 à 150 k€) le rembourse pour des années.

## 4. Les objections restantes, et la réponse prévue

| objection (v3) | réponse |
|---|---|
| « Un client qui engage 80 k€ veut un humain, pas une IA » (n°1) | 20 vrais appels à écouter avant l'essai ; une voix chaleureuse, aux couleurs de l'entreprise ; transfert immédiat vers un humain si le client le demande ; option « pas d'appel aux clients recommandés » |
| « Ça fait doublon avec ma secrétaire et mon CRM » | Archibald gère les soirs, les week-ends et les leads de plateformes ; intégration CRM testée la première semaine |
| « Les plateformes m'ont déjà vendu du lead qualifié » | Tableau de bord mensuel (rappels < 60 s, visites évitées, devis relancés, chantiers signés) ; résiliation en un clic |
| « Je voudrais seulement la relance de devis » | **Formule « Relance » à 59 €/mois**, demandée spontanément par 5 profils (porte d'entrée pour ceux qui vivent du bouche-à-oreille) |
| « Ma franchise doit valider » | Vendre aux **têtes de réseau** : un contrat couvre des dizaines d'agences |

## 5. Les chiffres (estimations, `cfo-renov.md`)

| | |
|---|---:|
| Marge par client et par mois, après acquisition amortie | **79 € (53 %)** |
| Point mort | **50 clients** |
| Résultat d'exploitation, année 1 (rampe à 140 clients au mois 12) | **+10 665 €** |
| Trésorerie nécessaire | **27 245 €** |
| À 99 € | point mort à 137 clients, année 1 à -26 085 € |
| À 199 € | point mort à 31 clients, année 1 à +47 415 € |

Comparaison : l'agent pour architectes perdait 19 710 € en année 1 et demandait 209 abonnés pour atteindre le point mort.

**Le marché.** Le bâtiment compte environ 620 000 entreprises de moins de 10 salariés ([CAPEB](https://www.capeb.fr/www/capeb/media/cp-capeb-plf-2024.pdf)). La cible (rénovation globale, extension, constructeurs, franchises qui reçoivent des leads) en représente une fraction, probablement plusieurs dizaines de milliers ; c'est **à chiffrer**. Moins de 10 % des artisans utilisent l'IA, et 42 % veulent s'y mettre d'ici fin 2026 ([CAPEB / La Bonne Réponse](https://www.capeb.fr/actualites/iartisans-la-capeb-et-la-start-up-la-bonne-reponse-lancent-une-application-ia-dediee-aux-artisans-du-batiment-specialises-dans-la-renovation-energetique)).

**La concurrence trouvée** porte sur les devis par IA (Artisania, Boby) et sur l'aide technique (IArtisans by CAPEB). **Je n'ai pas trouvé d'agent qui rappelle et qualifie les leads de rénovation en France** ; c'est à confirmer par une recherche plus poussée.

## 6. Le risque n°1 est juridique, à faire valider par un avocat avant tout lancement

- **Démarchage téléphonique.** Le démarchage pour la rénovation énergétique est interdit, et la règle générale se durcit (consentement préalable). **Rappeler quelqu'un qui vient de demander un devis** est en principe une réponse à sa demande, pas du démarchage. Pour les **leads achetés sur des plateformes**, il faut que le consentement recueilli par la plateforme couvre bien l'appel par l'entreprise. Cette question décide de la fonction n°1.
- **AI Act, article 50** : l'agent dit qu'il est une IA dès la première phrase.
- **Enregistrement des appels** : le client est informé et peut refuser. RGPD : contrat de sous-traitance (DPA) et liste des sous-traitants.

## 7. Et Archibald pour les architectes ?

On ne le jette pas : **c'est le même moteur**. La rénovation est le premier marché (volume, argent, urgence). Les architectes qui reçoivent des demandes d'inconnus (petites agences, technophiles) deviennent un segment secondaire, avec le même produit et un discours adapté. Le nom Archibald et la phrase « Pas le plus connu. Le plus compatible avec votre projet. » servent plus tard, côté particuliers.

## 8. Les 30 prochains jours

1. **Avocat (droit de la consommation et démarchage)** : valider le rappel des leads entrants et achetés. Si ce n'est pas possible pour les leads achetés, on garde les SMS et les e-mails instantanés plus la relance de devis.
2. **10 entretiens** avec des dirigeants d'entreprises de rénovation ou d'extension qui achètent des leads. Les questions : combien de leads par mois, combien payés, quel délai de rappel, combien de devis non signés.
3. **Prototype** : rappel en moins de 60 s plus relance de devis, et 20 appels de démonstration enregistrés.
4. **5 pilotes gratuits** pendant 30 jours. Les seuils pour continuer : au moins 1 chantier signé attribuable par pilote, et 3 pilotes sur 5 qui disent « je paie 149 € ».
5. **1 rendez-vous avec une tête de réseau de franchise rénovation.**

**Verdict : c'est la meilleure piste des cinq versions testées.** C'est la seule qui est rentable dès l'année 1 sur le papier, et la seule où l'adhésion dépasse 50 % sur un panel de 40. Elle reste à prouver avec de vrais clients.
