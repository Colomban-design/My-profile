# Plan de lancement : ArchiMatch

Le lancement public est prévu le **lundi 1er février 2027**, dans **une seule métropole** : celle où vous avez du réseau. Il reste à la choisir (par exemple Lyon, Nantes ou Lille ; évitez Bordeaux, siège d'Archidvisor). Mais d'abord, on teste sans coder.

## 1. Tester avant de dépenser : le « test conciergerie » (12 oct. au 13 déc. 2026)

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

## 2. Le compte à rebours (semaine par semaine ; ★ = chemin critique)

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

## 3. Le jour du lancement (lundi 1er février 2027)

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

## 4. Les 30 premiers jours

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
