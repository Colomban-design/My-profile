# Opérations : Archibald Relais

## 1. Le cycle (★ = vu par le client)

1. ★ **La demande** : ville, type d'ERP, mission attendue (dépôt de l'autorisation de travaux ou du permis, visites, suivi), délai, dossier de l'agence.
2. **Le sourcing** dans le réseau vérifié, ou un recrutement express si la ville n'est pas couverte.
3. ★ **2 profils sous 48 h**, avec la fiche relais : Ordre, RC et décennale (attestations et plafonds), 3 dossiers ERP comparables, 2 références joignables.
4. ★ **Un entretien de 20 minutes** entre l'agence et le relais.
5. ★ **Le contrat** de sous-traitance entre l'agence et le relais (contrat-type Archibald), avec la clause de non-sollicitation et le délai de dépôt. Facture de 490 € à l'agence.
6. **Le suivi** à J+7 (dossier reçu ?), puis à la date de dépôt (tenue ?).
7. ★ **La garantie** : si le délai n'est pas tenu, forfait remboursé et nouveau relais en 48 h.
8. **La notation** du relais par l'agence : délai, qualité, communication. Elle alimente la base.

## 2. Prestataires et outils

| besoin | options | remarque |
|---|---|---|
| Base des relais + CRM | outil de base de données / CRM du marché | fiche relais, villes, références ERP, notes |
| Vérification Ordre | annuaire public de l'Ordre des architectes | inscription au tableau |
| Brief relais | l'agent IA existant d'Archibald | il est réutilisé |
| Facturation | outil de facturation + prélèvement / carte | séquestre **optionnel** via un établissement de paiement agréé, plus tard |
| Juridique | avocat (sous-traitance, non-sollicitation, responsabilité d'intermédiaire) | |
| Assurance | RC pro d'intermédiaire | |

## 3. L'équipe

- **Les 6 premiers mois :** le fondateur seul. Il vend aux agences et contractants, recrute les relais (objectif : 100 dans 30 villes) et fait le suivi.
- **À partir de 30 relais par mois :** un « responsable réseau relais » à temps partiel (sourcing et vérification). Ce poste n'est pas dans `numbers.json` : relancez `/founder-cfo` à ce moment-là.

## 4. Les procédures clés

**A. Vérifier un relais (avant sa première mission)**
1. Vérifier l'inscription à l'Ordre.
2. Obtenir les attestations RC pro et décennale de l'année.
3. Obtenir 3 dossiers ERP avec leur résultat (autorisation obtenue ? délai ?).
4. Passer 2 appels de références.
5. Faire signer la charte : délai, non-sollicitation, pas d'esquisse gratuite.

**B. Un délai de dépôt non tenu**
1. Prévenir l'agence le jour même.
2. Proposer un nouveau relais sous 48 h.
3. Rembourser le forfait.
4. Noter le relais ; après deux incidents, il sort du réseau.

**C. Une sollicitation directe du client final par un relais**
1. Rassembler les preuves.
2. Appliquer la pénalité prévue au contrat.
3. Exclure le relais du réseau.

## 5. Règles et responsabilités (à confirmer par un professionnel ; pas un conseil juridique)

- [ ] **Le statut d'Archibald** : un service de mise en relation et de vérification facturé à l'agence. **La responsabilité de la mission reste chez le relais et chez l'agence qui le sous-traite.** C'est à écrire noir sur blanc dans les CGV.
- [ ] **Le contrat-type de sous-traitance entre l'agence et le relais** : délai, non-sollicitation, assurances.
- [ ] **La déontologie :** ici, **l'architecte ne paie aucune commission**. Le risque de rémunération d'un apporteur d'affaires, soulevé dans les versions précédentes, disparaît côté relais. Faites tout de même valider le schéma par un avocat.
- [ ] **Le RGPD** pour la base des relais (consentement, conservation).
- [ ] **La RC pro d'Archibald.**
- [ ] *Plus tard :* le séquestre via un établissement de paiement agréé (voir `_v2-archibald-particuliers/ops.md`).

## 6. Registre des risques

| # | risque | probabilité | gravité | plan |
|---|---|---|---|---|
| 1 | Un premier relais rate son dossier et le client part | moyenne | **forte** | vérification stricte, entretien préalable, garantie de délai, suivi à J+7 |
| 2 | Pas de relais disponible dans une ville demandée | élevée au début | forte | 100 relais dans 30 villes avant l'ouverture, recrutement express |
| 3 | Désintermédiation : l'agence garde le relais en direct ensuite | élevée | moyenne | **accepter** : le client paie pour chaque **nouvelle** ville ; le pack de 10 fidélise ; la valeur vient de la vérification et de la garantie |
| 4 | Le relais démarche le client final | moyenne | forte | clause signée, pénalité, exclusion du réseau |
| 5 | Volume de relais trop faible par client | moyenne | forte | cibler les clients à plus de 20 ouvertures par an ; le pack de 10 |
| 6 | Une grande agence construit son propre réseau | moyenne | moyenne | Archibald sert tout le monde, et la notation croisée a plus de valeur à mesure qu'elle grossit |
| 7 | Fondateur seul débordé | moyenne | moyenne | procédures écrites, temps partiel réseau dès 30 relais par mois |
