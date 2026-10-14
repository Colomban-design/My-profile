# Conseil d'administration : Archibald, l'agent IA pour architectes

**Vote : 3 « FUND IF » (financer sous conditions) sur 3. Score moyen : 5,3/10** (Offre 5 · Monopole 5 · Produit 6). C'est le meilleur score des quatre versions testées (v3 Relais : 4,3/10). Les mémos complets sont dans `board/`.

## Ce que les trois membres jugent solide

- **Une douleur nommée par le marché lui-même.** Budgets irréalistes, esquisses gratuites, la moitié des demandes qui n'aboutit pas, soirées perdues : ces plaintes reviennent spontanément dans tous les panels d'architectes depuis la v1.
- **Le blocage déontologique est levé.** Il n'y a plus de commission sur les honoraires, et l'architecte ne paie plus « pour un client ». Il paie pour un outil.
- **Les actifs existent.** L'agent conversationnel et le brief PDF sont déjà construits, et la mise en place tient en une ligne de code.
- **L'effet réseau est bien conçu.** Les refus d'un abonné deviennent des demandes pour un autre abonné. Un standard IA générique ne peut pas offrir ça.

## Les risques soulevés par plusieurs membres

1. **Le volume de demandes entrantes est inconnu (3/3).** Si un architecte reçoit peu de demandes froides, le filtre ne lui rapporte rien. Il résilie, et le réseau ne se remplit pas. **Le panel le confirme** : 33 des 80 refus sont des « need », du type « mes clients viennent par recommandation, je n'ai pas de flux à filtrer ».
2. **Une erreur de l'IA engage l'architecte (3/3).** PLU, seuil des 150 m², honoraires : chaque affirmation faite au client est un risque pour la crédibilité de l'agence. **Le panel le confirme** : 33 refus pour « trust », avec la phrase qui revient le plus souvent : « s'il se trompe, c'est moi qui porte la faute ».
3. **Le démarrage à froid du réseau (Monopole, Produit).** Un renvoi n'a de valeur que s'il existe un confrère compatible dans la même zone. Avec des abonnés dispersés, l'effet réseau est nul.
4. **Trop de promesses (Produit).** Le pitch en contient huit, et chacune peut casser l'expérience devant le client.
5. **Le plafond de marché (Offre, Monopole).** 29 500 architectes × 79 € × 12 ≈ 28 M€ par an, et seulement si 100 % s'abonnent.

## Ce que le conseil juge de la thèse « outil → réseau »

Elle est **juste dans l'ordre, fausse si on inverse**. Le réseau ne devient l'actif que si l'outil est d'abord indispensable seul (Produit). Il faut donc le prouver ville par ville, avec une densité mesurée (Monopole). Pour la « très grosse entreprise », le conseil demande un chemin d'expansion écrit au-delà de l'abonnement. Pistes : autres professions réglementées de la maîtrise d'œuvre, autres pays, ou une prise de valeur sur le flux de projets qualifiés (voir `summary.md`).

## Conditions (checklist)

- [ ] **Couper les promesses** : une seule promesse au lancement, le brief prêt avant le rendez-vous, avec le tri des demandes. Le PLU et les honoraires restent internes à l'architecte tant que leur exactitude n'est pas prouvée. → fait dans `offer.md` (mode « prise de brief »).
- [ ] **Maîtriser les ruptures** : l'IA s'annonce dès la première phrase (AI Act art. 50), l'architecte valide le ton des refus, et le renvoi se fait avec l'accord explicite de l'architecte et du client. → `offer.md`, `ops.md`
- [ ] **Prouver le volume** : sur 10 à 20 pilotes pendant 30 jours, mesurer les demandes reçues, filtrées et briefées. → `launch.md`
- [ ] **Prouver l'exactitude** : 50 briefs validés par les pilotes et un taux publié. → `launch.md`
- [ ] **Une zone pilote, pas la France** : viser une densité dominante dans une métropole avant toute expansion. → `launch.md`
- [ ] **Chiffrer le coût d'acquisition, la marge et l'expansion.** → `cfo.md`, `summary.md`
