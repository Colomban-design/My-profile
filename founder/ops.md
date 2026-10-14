# Opérations : Archibald, l'agent IA pour architectes

> Ce n'est pas un conseil juridique. Faites valider les points 1 à 4 par un avocat (droit du numérique) et un conseil en déontologie avant le lancement payant.

## 1. Les obligations légales (avant le premier client payant)

| sujet | ce qu'il faut faire | pourquoi |
|---|---|---|
| **AI Act, article 50** | La première phrase de l'agent dit qu'il est une IA (« Je suis l'assistant IA de l'agence X »). Le PDF le mentionne aussi. | Obligatoire depuis le 2 août 2026 ; amendes jusqu'à 15 M€ ou 3 % du CA ([donneespersonnelles.fr](https://donneespersonnelles.fr/transparence-ia-article-50-ai-act)) |
| **RGPD : rôles** | L'architecte est **responsable de traitement**, Archibald est **sous-traitant**. Un contrat de sous-traitance (DPA, art. 28) est signé à l'abonnement. | Les données client (adresse, budget) sont des données personnelles |
| **RGPD : sous-traitants ultérieurs** | Une liste publique et datée : hébergeur, fournisseur du modèle d'IA, envoi d'e-mails, avec le pays de chacun. Contrat « zéro rétention, zéro entraînement » chez le fournisseur IA. | C'est l'objection n°2 du re-test : « hébergé en France, mais qui voit les données ? » |
| **RGPD : client final** | Une mention d'information dans la conversation, une durée de conservation (par ex. 12 mois sans suite), une suppression à la demande | Droits des personnes |
| **Option réseau** | Le transfert à un confrère se fait seulement avec un **consentement explicite du client** (case non cochée) et une activation par l'architecte. | Un nouveau destinataire des données, donc un consentement distinct |
| **Déontologie** | Le contenu de l'agent est relu par un avocat en droit des professions réglementées. Une saisine de l'Ordre (CNOA) est faite **avant** de communiquer dessus. **On ne mentionne pas l'Ordre dans la publicité tant qu'aucun avis n'est rendu.** | Code de déontologie ([CNOA](https://architectes.org/sites/cnoa/files/2024-05/code_de_deontologie.pdf)). Dans le re-test, la phrase « avis demandé » a **réveillé** la méfiance au lieu de rassurer. |
| **Responsabilité** | L'agent n'affirme rien au client. Le brief est marqué « aide à la préparation, à vérifier par l'architecte », avec les sources PLU (lien vers le document d'urbanisme). CGV avec une limitation de responsabilité. RC pro éditeur. | « S'il se trompe, c'est moi qui porte la faute » (objection n°1 du panel v1) |

## 2. Le flux quotidien

1. Un client arrive sur le site de l'agence, ou appelle (option téléphone).
2. L'agent se présente comme une IA, pose 8 à 12 questions, sans rien affirmer.
3. Le brief PDF privé part à l'architecte en moins d'une minute, avec ses alertes : budget, seuil des 150 m², points de PLU à vérifier.
4. L'architecte clique sur l'un des trois boutons : **rappeler** (un créneau est proposé au client), **décliner** (le message type, validé par l'architecte, part chez le client), ou **décliner et proposer un confrère** (si l'option réseau est active et que le client y consent).
5. Le client reçoit une réponse sous 48 h. C'est l'engagement demandé par le panel clients (« un rappel sous 48 h, sinon je vais ailleurs »). Une relance automatique part vers l'architecte au bout de 24 h.

## 3. Qualité et mesure

- **Taux d'exactitude du brief** : l'architecte note chaque brief (pouce haut ou bas, plus un champ libre). L'objectif est ≥ 90 % de briefs jugés « justes » sur 50 briefs avant d'ouvrir une 2e ville.
- **Taux d'abandon de la conversation côté client** : l'objectif est < 30 %. Au-delà, on raccourcit le questionnaire.
- **Délai de rappel** par l'architecte : il est affiché à l'architecte, mais jamais publié.
- **Le réseau** : demandes transmises, acceptées par le confrère, puis transformées en rendez-vous.

## 4. Fournisseurs et outils

- Un hébergement en France (OVHcloud, Scaleway ou équivalent), en vérifiant leurs offres de modèles d'IA hébergés en UE.
- Un fournisseur de modèle IA avec contrat UE et zéro rétention. Une solution de repli chez un second fournisseur.
- La téléphonie (option) via un opérateur de voix IA, avec des numéros français.
- Le paiement par prélèvement SEPA ou carte, des factures HT automatiques.

## 5. Risques opérationnels

| risque | parade |
|---|---|
| L'agent répond quelque chose de faux au client | Le mode « prise de brief » interdit toute affirmation. Des tests automatiques sur 100 conversations type tournent avant chaque mise à jour. |
| Panne du fournisseur IA | Un fournisseur de secours, et sinon un formulaire classique en repli |
| Plainte d'un client final | Une réponse du fondateur sous 24 h, et le droit de suppression appliqué immédiatement |
| Un architecte reçoit trop peu de demandes | Un tableau de bord mensuel « X demandes, Y heures économisées ». En dessous de 3 demandes par mois, on propose la formule à la demande (voir `pricing.md`). |
