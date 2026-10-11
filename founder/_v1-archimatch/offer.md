# Offre : ArchiMatch

L'offre est construite pour **l'architecte**, qui paie, avec la méthode de la lentille Offre. Le déposant a sa propre promesse (en bas). Pitch avant : `pitch-v1.md`. Pitch après : `pitch.md`.

## 1. Les obstacles (dans les mots du panel et des plaintes concurrentes)

Avant : 1. « 8 %, c'est toute ma marge » · 2. « Je n'ai jamais payé pour un client » · 3. « Les leads de plateforme veulent un plan gratuit et disparaissent » · 4. « Le budget du client sera irréaliste » · 5. « Le client n'aura pas son prêt » · 6. « Est-ce compatible avec l'Ordre ? » · 7. « Comment savez-vous ce que je facture ? Usine à gaz » · 8. « Je n'ai pas le temps de rédiger des candidatures » · 9. « Mis en concurrence à 3, je fais une esquisse gratuite pour rien » · 10. « Archidvisor et l'annuaire de l'Ordre existent déjà » · 11. « Pas encore dans ma région ».
Pendant : 12. Coordonnées client communiquées trop tard ou trop tôt · 13. Tirer les honoraires vers le bas face aux 2 autres · 14. Petits projets mal payés.
Après : 15. Projet abandonné après signature · 16. Commission prélevée sur toute la durée de la mission · 17. Aucun retour si le client disparaît.

## 2. Solutions, notées (valeur 1-5 / coût 1-5), gardées en gras

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

## 3. La pile

- **Le cœur : « Projets Signables ».** Des projets de particuliers de plus de 100 k€ de travaux dans votre métropole, cadrés, au budget vérifié et au financement déclaré, envoyés à 3 architectes seulement.
- **Bonus 1 : Zéro esquisse gratuite.** C'est écrit dans les CGU côté client. Répond à « je fais une esquisse pour rien ».
- **Bonus 2 : 10 minutes pour postuler.** Disponibilité, 3 références, fourchette d'honoraires. Répond à « pas le temps ».
- **Bonus 3 : Une seule facture.** 5 %, plafonnés à 1 500 €, émis à la signature, puis rien à déclarer. Répond à « usine à gaz ».
- **Garantie « Financement ».** Si le projet est abandonné avant le dépôt du permis faute de financement, la commission est remboursée. Coût modélisé : 10 % des projets × 750 € = 75 € par projet signé.
- **Urgence réelle.** Statut fondateur pour les 50 premiers de la ville jusqu'à l'ouverture publique.
  - **Modification après les chiffres du CFO** (non re-testée) : le tarif fondateur à 3 % ne vaut que pour les **2 premiers projets signés** de chaque architecte, pas 12 mois. À 450 € par projet, chaque signature ne laisse que 65 € et le point mort monte à 61 projets par mois.
- **Conformité.** Avis juridique écrit, consultable avant l'inscription. **Le pitch le présente comme acquis, alors qu'il reste à obtenir avant le lancement** (voir `ops.md`).

## 4. Équation de valeur (architecte), avant / après (1-10)

| élément | v1 | v2 | ce qui le fait bouger |
|---|---:|---:|---|
| Résultat rêvé (projets signés, bien payés) | 6 | 7 | seuil 100 k€ |
| Probabilité perçue | 3 | 5 | budget vérifié, financement, garantie, avis juridique |
| Délai | 5 | 5 | inchangé (cycle de signature long) |
| Effort et sacrifice | 3 | 6 | 10 min, zéro esquisse, facture unique, plafond |

## 5. Le re-test (panel simulé, même graine 625958)

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

## 6. La promesse côté déposant (non re-testée, tirée du panel clients)

Le panel clients a voté à 50 %. Il n'a soulevé aucune objection de prix, mais 9 refus sur 10 portent sur la confiance. D'où quatre promesses :
1. **« Même prix qu'en direct »** : la commission est affichée, et l'architecte s'engage par écrit à ne pas la répercuter.
2. **« Personne ne vous appelle sans votre accord »** : vos coordonnées ne partent qu'aux architectes que vous retenez.
3. **« D'abord : avez-vous besoin d'un architecte ? »** : un diagnostic honnête, y compris quand la réponse est non.
4. **« Pourquoi ces 3 ? »** : le critère de sélection est expliqué, et aucun architecte ne peut payer pour être choisi.
