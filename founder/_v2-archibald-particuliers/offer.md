# Offre : Archibald

Ce document part du pitch du fondateur (`pitch-clients-v1.md`, `pitch-architectes.md`) et des panels (`panel/`, `panel-clients/`, `panel-clients-v2/`), avec la méthode de la lentille Offre.

## 1. Les obstacles, dans les mots des panels

**Côté clients**
1. « Payer 5 % en plus, c'est payer deux fois. »
2. « Un architecte recommandé par un proche ne me coûte rien. »
3. « L'algorithme me propose ceux qui paient, pas les meilleurs. »
4. « Je préfère parler à un humain qu'à une IA. »
5. « Mon banquier veut des devis. »
6. « Ai-je vraiment besoin d'un architecte ? »
7. « Je vais être harcelé de coups de fil. »
8. « Je ne sais pas ce que coûte un architecte. »
9. « Qui tient l'argent du séquestre ? »
10. « Le séquestre ne couvre pas le chantier, là où je me suis fait avoir. »

**Côté architectes**

11. « 10 %, c'est ma marge. »
12. « Je n'ai jamais payé pour un client. »
13. « Le budget du client sera irréaliste. »
14. « Je ferai une esquisse gratuite contre deux confrères. »
15. « Un tiers garde mon argent et décide si l'étape est validée. »
16. « Est-ce compatible avec la déontologie ? »
17. « Le PLU lu par une IA sera faux. »

## 2. Ce qu'on garde, ce qu'on retire

| décision | répond à |
|---|---|
| **Supprimer les 5 % côté client** (client : 5 % → 70 % d'adhésion) | 1, 2 |
| **« Honoraires garantis identiques à ceux pratiqués en direct »**, écrit dans le contrat architecte | 1, 3 |
| **Critères de matching publiés, aucun architecte ne paie pour être proposé** | 3 |
| **Un humain rappelle sous 48 h**, mais **seulement si le client le demande** (un client du panel a relevé la contradiction avec « personne ne vous appelle ») | 4, 7 |
| **Diagnostic « Ai-je besoin d'un architecte ? » honnête**, y compris quand la réponse est non | 6 |
| **Fourchette d'honoraires affichée avant tout rendez-vous** | 8 |
| **Séquestre tenu par un établissement de paiement agréé, nommé** ; règles de déblocage écrites ; validation tacite après 7 jours ; médiation en cas de désaccord | 9, 15 |
| **Séquestre étendu au suivi de chantier** (honoraires de l'architecte, pas les travaux) | 10, et élargit la base de commission |
| **8 % plutôt que 10 %, sans abonnement ; 5 % sur les 3 premières missions des fondateurs** | 11 |
| **Pas d'esquisse gratuite**, inscrit dans les CGU | 14 |
| **Brief relu par un architecte référent pendant les 3 premiers mois** ; l'agent dit « je ne sais pas » sur le PLU quand la source manque | 13, 17 |
| Avis juridique + démarche auprès de l'Ordre (`ops.md`) | 16 |
| *Écarté :* le séquestre sur les travaux des entreprises | autre métier, autre agrément |

## 3. La pile

- **La chose unique (demandée par la lentille Produit) : « Votre architecte est payé, votre projet est protégé. »** C'est le séquestre qui distingue Archibald. Le brief IA est la porte d'entrée gratuite, et le matching est le moyen.
- **Côté client, gratuitement :**
  - le diagnostic honnête (« Ai-je besoin d'un architecte ? ») ;
  - un brief PDF à montrer à la banque ;
  - 3 architectes compatibles, avec réalisations comparables et fourchette d'honoraires ;
  - le séquestre étape par étape, avec médiation ;
  - un rappel humain sur demande.
- **Côté architecte :**
  - des clients au brief cadré ;
  - le paiement garanti par le séquestre ;
  - zéro esquisse gratuite ;
  - 8 % seulement sur ce qui passe par le séquestre, sans abonnement.
- **Garantie client :** si l'architecte ne livre pas l'étape validée au contrat, les fonds de cette étape sont rendus, après médiation. Elle ne coûte rien à Archibald, puisque les fonds sont séquestrés.
- **Garantie architecte :** une étape livrée et non contestée sous 7 jours est payée automatiquement.
- **Urgence réelle :** le statut fondateur pour les 50 premiers architectes de la ville, jusqu'à l'ouverture publique.

## 4. Équation de valeur, avant et après (1 à 10)

| | client avant | client après | architecte avant | architecte après |
|---|---:|---:|---:|---:|
| Résultat rêvé | 7 | 7 | 6 | 7 |
| Probabilité perçue | 3 | 6 | 4 | 5 |
| Délai | 6 | 6 | 5 | 5 |
| Effort et sacrifice | 4 (5 % en plus) | 8 (gratuit) | 4 | 5 |

## 5. Le re-test

- **Clients** (même graine 1102, 20 personnes) : **5 % → 70 %**.
  - Par segment (peu de données) : 80 % pour la maison neuve, 75 % pour l'extension, 57 % pour la rénovation.
  - L'objection qui reste : « l'algorithme propose ceux qui paient ». Elle est **atténuée, pas levée** : seuls les premiers avis vérifiés la feront tomber.
- **Architectes : pas de re-test de l'offre Archibald.** Dans la v1 (`_v1-archimatch/panel-v2/`), une offre comparable (5 % plafonné, zéro esquisse, garantie) avait fait passer l'adhésion de 30 % à 55 %. **À re-tester à 8 %** avant d'engager quoi que ce soit.
