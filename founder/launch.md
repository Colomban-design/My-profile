# Plan de lancement : Archibald

Le site, l'agent et le brief existent déjà : **le test porte sur la transaction, pas sur le produit.** Tout se joue dans **une seule ville** (celle où vous avez du réseau ; évitez Bordeaux, siège d'Archidvisor). L'ouverture publique est fixée au **lundi 1er février 2027**.

## 1. Tester avant de dépenser : « les 10 premiers séquestres » (12 oct. 2026 → 31 janv. 2027)

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

## 2. Le compte à rebours (★ = chemin critique)

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

## 3. Le jour d'ouverture (lundi 1er février 2027)

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

## 4. Les 30 premiers jours

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
