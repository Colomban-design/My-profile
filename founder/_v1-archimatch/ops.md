# Opérations : ArchiMatch

Le fonctionnement réel, du dépôt d'un dossier à l'encaissement de la commission. Les coûts reprennent `numbers.json` ; toute différence est signalée.

## 1. Le cycle quotidien (★ = vu par le client ou l'architecte)

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

## 2. Prestataires et outils (prix à vérifier sur les pages officielles)

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

## 3. L'équipe

- **Mois 1 à 3 (test et lancement)** : le fondateur seul. Il fait la prospection des architectes (2 h par jour), la vérification des dossiers (15 min par dossier) et les partenariats (courtiers, agents).
- **Au plan (20 signatures par mois, environ 80 dossiers)** : 80 × 15 min = 20 h de vérification par mois, plus le suivi. Cela tient pour une personne. **Au-delà de 40 signatures par mois**, prévoir un temps partiel « vérification et suivi » ; il n'est pas dans `numbers.json`, donc **il faut relancer `/founder-cfo`** à ce moment-là.
- Les charges sociales et le statut du dirigeant (rémunération ou dividendes) sont à voir avec l'expert-comptable.

## 4. Les procédures clés

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

## 5. Règles, autorisations, assurances (à confirmer auprès d'un professionnel ; pas un conseil juridique)

- [ ] **Déontologie des architectes : condition bloquante.** Obtenir un avis écrit d'un avocat **et** solliciter la position du CROA de la région ou du CNOA sur une commission versée par l'architecte. Source : [Ordre des architectes, code de déontologie](https://www.architectes.org/sites/cnoa/files/2024-05/code_de_deontologie.pdf). Le décret du 26 juin 2026 qui le modifie est à vérifier ([Légifrance](https://www.legifrance.gouv.fr/)). *Sans cela, 6 refus sur 50 dans le panel ne bougeront pas.*
- [ ] **Obligations des plateformes en ligne** : transparence sur les critères de classement et sur l'existence d'une rémunération par les professionnels (Code de la consommation, art. L111-7 et suivants, sur [Légifrance](https://www.legifrance.gouv.fr/)). Cela rejoint la promesse « pourquoi ces 3 ».
- [ ] **Usage du titre d'architecte** : n'accepter que des inscrits au tableau de l'Ordre et vérifier chaque inscription (voir l'[enquête DGCCRF](https://www.economie.gouv.fr/dgccrf/qualification-darchitecte-sur-internet)).
- [ ] **RGPD** : registre des traitements, durée de conservation des dossiers, consentement au partage des coordonnées ([CNIL](https://www.cnil.fr/)).
- [ ] **Médiation de la consommation** pour les déposants particuliers ([economie.gouv.fr, médiateur de la consommation](https://www.economie.gouv.fr/mediation-conso)).
- [ ] **Immatriculation** de la société ([guichet unique INPI](https://procedures.inpi.fr/)), compte bancaire professionnel, TVA sur les commissions.
- [ ] **CGU déposants + CGV architectes** : zéro esquisse gratuite, commission à la signature, plafond, garantie financement, pénalité en cas de contournement.
- [ ] **RC professionnelle** de la plateforme.

## 6. Registre des risques

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
