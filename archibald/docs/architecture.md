# Architecture

## Vue d'ensemble

```
 formulaire du site ─┐                     ┌─> SMS au client (opérateur SMS)
 appel manqué ───────┤  POST /leads        ├─> appel (opérateur voix, étape suivante)
                     ▼                     │
 SMS du client ──> server.py ──> engine.py ┼─> fiche par e-mail + alerte SMS au dirigeant
                     ▲            │   │    │
 logiciel de devis ──┘ /quotes    │   │    └─> relances de devis (tick, par cron)
                                  ▼   ▼
                         qualifier.py  store.py (SQLite)
                         Claude ou     leads, preuves d'accord, opposition (STOP),
                         script        messages, fiches, devis, relances, journal
```

| Module | Rôle |
|---|---|
| `engine.py` | orchestration : chaque événement passe par là, et toutes les règles d'envoi sont dans `_can_send` |
| `consent.py` | textes d'accord, lecture des réponses 1/2/3, détection de STOP |
| `qualifier.py` | `ClaudeQualifier` (API Messages, sortie JSON validée par schéma) et `ScriptedQualifier` (secours) ; garde-fou prix |
| `scoring.py` | classement à visiter / à rappeler / à surveiller, raisons lisibles, seuil architecte |
| `fiche.py` | fiche texte pour le dirigeant + export JSON pour le logiciel de devis |
| `store.py` | stockage SQLite |
| `providers.py` | interfaces SMS / voix / e-mail ; versions console pour la démo et les tests |
| `server.py` | webhooks HTTP (bibliothèque standard) |

## Parcours d'un lead

1. **Demande reçue** (`POST /leads`). Si le numéro a déjà répondu STOP, on n'envoie rien. Sinon,
   un seul SMS part tout de suite. Il dit que c'est une IA, rappelle la demande de devis, propose
   1) appel maintenant, 2) plus tard, 3) écrit, et rappelle STOP. Pour un contact recommandé (si
   l'entreprise l'a choisi), il n'y a pas d'appel IA : on propose l'écrit ou l'appel du dirigeant.
2. **Réponse du client.**
   - **1** : on lance l'appel, mais seulement dans les heures fixées. En dehors, on propose de
     continuer par écrit.
   - **2** : on demande le créneau, puis on transmet au dirigeant.
   - **3** : la qualification commence.
   - **Réponse floue** : on repose la question. Aucune qualification ne démarre sans accord.
3. **Qualification**, une question par message : travaux, surface (et surface actuelle), commune,
   délai, budget, financement. Le client peut demander un humain à tout moment, et le dirigeant
   est alors prévenu par SMS. Si le client demande un prix, on n'en donne jamais.
4. **Fiche** : elle est classée avec ses raisons et envoyée par e-mail avec l'export JSON. Si elle
   est « à visiter », le dirigeant reçoit aussi une alerte SMS.
5. **Devis** (`POST /quotes`) : relances à J+3, J+10 et J+20, envoyées par `tick` (cron) du lundi au
   samedi, dans les heures fixées. Une réponse du client arrête les relances. Son motif
   d'hésitation est classé et remonté, et le dirigeant reprend la main. Signé ou perdu
   (`POST /quotes/<id>/status`) : les relances s'arrêtent.

## Consentement (à faire valider par un avocat)

- Depuis le 11/08/2026, le démarchage téléphonique demande un accord préalable. Archibald ne
  démarche pas : il répond à une demande de devis que la personne vient de faire, et il demande
  quand même l'accord par écrit avant tout appel ou toute qualification.
- Chaque étape est enregistrée dans `consents` (`demande_envoyee`, `accord_appel`, `accord_ecrit`,
  `plus_tard`, `stop`) avec le texte exact et la date de fin de conservation (3 ans).
- **STOP** inscrit le numéro dans `optouts`. Toutes les relances sont annulées, et toute nouvelle
  demande depuis ce numéro est ignorée. Seul le message de confirmation part.
- La rénovation énergétique fait l'objet d'une interdiction totale de démarchage. C'est une raison
  de plus de ne traiter que les demandes entrantes, et de ne jamais acheter de fichiers.
- AI Act, art. 50 : l'assistant se présente comme une IA dès le premier message.
- Leads de plateformes (achetés) : pas branchés tant que l'avocat n'a pas validé que l'accord
  donné sur la plateforme couvre ce contact.

## Transfert à un humain : quand et vers qui

| Déclencheur | Ce que voit le client | Ce que reçoit le dirigeant |
|---|---|---|
| « je veux parler à quelqu'un » | « Marc vous rappelle dans l'heure (en journée) » | SMS d'alerte + fiche partielle |
| choix 2 + créneau | « Marc vous rappelle (jeudi 18h) » | SMS avec le créneau |
| refus du modèle / réponse inexploitable | message neutre, rappel par le dirigeant | SMS d'alerte |
| message après la fiche | rien d'automatique | le message, tel quel |
| hésitation sur un devis | « Marc vous rappelle pour en parler » | motif classé (prix, délai…) + texte |
| fiche « à visiter » | confirmation | SMS d'alerte en plus de l'e-mail |

## Claude dans la boucle

- Un appel API par message du client : `beta.messages.create` avec une sortie structurée
  (`output_config.format` = schéma JSON). On reçoit à la fois la réplique et tous les champs
  connus, sans analyse de texte libre.
- Effort `low` par défaut. Le prompt système est mis en cache (`cache_control`), et le repli
  côté serveur (`fallbacks="default"`) couvre les surcharges.
- Si l'API est indisponible (limite de débit, réseau, erreur 5xx), le script de secours répond :
  le client n'attend jamais.
- **Garde-fou après le modèle** : si la réplique contient un montant que le client n'a pas dit
  lui-même, elle est remplacée par la réponse type « pas de prix avant la visite ».
- **Sécurité** : le texte du client est traité comme une donnée. Le prompt système le dit, et
  surtout les actions sensibles (appel, STOP, envoi, relances) sont décidées par le code et jamais
  par le modèle. Le modèle ne peut ni appeler, ni lever une opposition, ni écrire au dirigeant
  autre chose qu'une fiche.

## Données

`leads` (état : `attente_accord` → `qualification` → `qualifie`, ou `plus_tard`,
`transfere_humain`, `stop`), `consents`, `optouts`, `messages`, `fiches`, `quotes`, `followups`
(`a_envoyer` / `envoye` / `annule`), `events` (journal qui alimente `/report`).

## Coûts

Les hypothèses de coût par client sont dans `founder/numbers.json` : voix 18 €, texte/SMS 8 €,
SMS d'accord 3 €, hébergement 4 € par mois. Ce sont des estimations, pas des mesures. Le pilote
doit mesurer le coût réel par lead (nombre de SMS, minutes de voix, jetons API) avant de fixer
le prix final.

## Prochaine étape technique : la voix

Opérateur voix français → transcription en continu → le même `Qualifier` → synthèse vocale. Le
moteur ne change pas : `start_call` ouvre la session, et chaque tour de parole passe par
`_qualify`. Il reste à traiter la latence (viser moins d'une seconde par réplique), les coupures,
et la phrase d'annonce « vous parlez à une IA » au décroché.
