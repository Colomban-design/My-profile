# Opérations : Archibald

## 1. Le cycle (★ = vu par le client ou l'architecte)

1. ★ **Le diagnostic et le brief IA** (5 min). Le PDF contient le budget, le PLU (avec sa **source** : le document d'urbanisme consulté, ou « non trouvé »), la faisabilité, le style et une **estimation des honoraires**.
2. ★ **Le rappel humain sous 48 h, si le client le demande** : relecture du brief, et une réponse honnête si un architecte n'est pas nécessaire.
3. **Le matching.** Les critères publiés sont la zone, le type de projet, la technique (bois, rénovation énergétique, etc.), les réalisations comparables et la disponibilité. Aucun critère payant. Pendant les 3 premiers mois, **un architecte référent relit le brief**.
4. ★ **Les architectes** reçoivent le brief anonymisé et ont 72 h pour se dire intéressés. Le client reçoit au plus 3 profils, avec fourchette d'honoraires. Les coordonnées ne sont échangées qu'avec ceux qu'il choisit.
5. ★ **Le contrat d'architecte** est signé hors plateforme (contrat type de l'Ordre recommandé). L'échéancier des honoraires est saisi dans Archibald.
6. ★ **Le dépôt au séquestre** des honoraires de la première étape, voire de toute la conception, chez le **prestataire de paiement agréé**.
7. ★ **L'étape livrée** (esquisse, APS, APD, PC…) : le client valide sous 7 jours, sinon c'est validé automatiquement. Le prestataire débloque les fonds, moins la commission de 8 %, vers l'architecte.
8. ★ **En cas de désaccord** : gel des fonds de l'étape, puis médiation (procédure B).
9. **Le suivi anti-fuite** : la part des honoraires du contrat réellement passée par le séquestre, avec relance aux étapes non déposées.

## 2. Prestataires (à comparer, prix à demander)

| besoin | options | point clé |
|---|---|---|
| **Séquestre / paiements de marketplace** | prestataires de paiement pour marketplaces agréés en Europe (par ex. [Stripe Connect](https://stripe.com/fr/resources/more/payment-solutions-marketplace-france), Mangopay, Lemonway) | **les fonds doivent rester chez l'établissement agréé, jamais sur le compte d'Archibald** ; vérifier son statut auprès de l'ACPR ; KYC des architectes |
| Agent IA + PDF | déjà en place | ajouter la source du PLU et la mention « indicatif » |
| Signature électronique | outil du marché | contrat et échéancier |
| Comptabilité | expert-comptable | TVA sur les commissions, flux en séquestre |
| Assurance | RC professionnelle d'intermédiaire de plateforme | à faire chiffrer par 2 courtiers |
| Juridique | avocat en droit du numérique et des paiements + droit de la construction et déontologie des architectes | **le poste le plus critique** |

## 3. L'équipe

- **Les 3 premiers mois :** le fondateur fait les rappels (20 min par brief), le recrutement d'architectes et le contenu Instagram. Un **architecte référent** relit les briefs (rémunéré à l'acte ou en parts à discuter : ce coût n'est pas dans `numbers.json`).
- **Au plan (20 missions/mois, environ 80 briefs) :** environ 27 h par mois de rappels, ce qui reste faisable seul. **Au-delà de 40 missions par mois**, il faudra un temps partiel « succès client » : relancez `/founder-cfo` à ce moment.

## 4. Les procédures clés

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

## 5. Règles, agréments, assurances (à confirmer par un professionnel ; pas un conseil juridique)

- [ ] **Le séquestre : condition bloquante.** Encaisser des fonds pour le compte de tiers relève des services de paiement. Archibald doit passer par un **établissement de paiement ou de monnaie électronique agréé**, en être agent, ou relever d'une exemption ([JDN sur l'ACPR et les marketplaces](https://www.journaldunet.com/retail/1146067-les-marketplaces-francaises-mises-en-peril-par-les-autorites-bancaires/), [FrenchWeb](https://www.frenchweb.fr/places-de-marche-ce-quil-faut-savoir-sur-la-reglementation-des-paiements/275851) ; articles de 2015-2017, **à faire confirmer par un avocat en droit des paiements**). Ne jamais faire transiter l'argent par le compte d'Archibald.
- [ ] **La déontologie des architectes : une commission de 8 à 10 % sur les honoraires.** Obtenir un avis d'avocat et solliciter la position du CROA ou du CNOA ([code de déontologie](https://architectes.org/sites/cnoa/files/2024-05/code_de_deontologie.pdf)). 2 architectes sur 20 refusent pour cette raison dans le panel, et 6 sur 50 dans la v1.
- [ ] **Les obligations des plateformes** : transparence des critères de classement et de la rémunération versée par les professionnels (Code de la consommation, art. L111-7 et suivants, [Légifrance](https://www.legifrance.gouv.fr/)). Cela rejoint « aucun critère payant ».
- [ ] **Le titre d'architecte** : vérifier l'inscription à l'Ordre de chaque architecte ([DGCCRF](https://www.economie.gouv.fr/dgccrf/qualification-darchitecte-sur-internet)).
- [ ] **Le RGPD** : consentement au partage des coordonnées, durée de conservation des briefs ([CNIL](https://www.cnil.fr/)).
- [ ] **L'IA et le PLU** : mention « estimation indicative, non opposable », source citée, renvoi vers le service urbanisme de la commune.
- [ ] **La médiation de la consommation** ([economie.gouv.fr](https://www.economie.gouv.fr/mediation-conso)).
- [ ] **Les CGU clients et les CGV architectes** : pas d'esquisse gratuite, honoraires identiques au direct, règles de déblocage, validation tacite à 7 jours, médiation.
- [ ] **La RC professionnelle.**

## 6. Registre des risques

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
