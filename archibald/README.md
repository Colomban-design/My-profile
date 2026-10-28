# Archibald Rénov : prototype technique

Le commercial IA des entreprises de rénovation. Quand un particulier demande un devis, Archibald
lui répond en moins d'une minute. Il lui demande d'abord par SMS comment il veut être recontacté
(accord écrit, preuve gardée 3 ans), puis prépare le projet en quelques questions. Il envoie ensuite
au dirigeant une fiche classée « à visiter / à rappeler / à surveiller » et relance les devis à J+3,
J+10 et J+20.

Ce dossier est un **prototype qui tourne**. Il n'est pas encore branché à un vrai opérateur SMS ni
à un vrai canal voix. Tout se teste sans clé API.

## Lancer

```bash
cd archibald
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

python -m archibald.cli demo --scripted   # un lead complet, de la demande au devis signé
pytest                                    # 22 tests : consentement, STOP, prix, humain, relances, horaires
python -m archibald.cli serve             # webhooks sur http://127.0.0.1:8000
```

Avec `ANTHROPIC_API_KEY` dans l'environnement, `demo` et `serve` utilisent Claude pour la
conversation. Sinon, c'est le script de secours qui la mène.

| Variable | Défaut | Rôle |
|---|---|---|
| `ANTHROPIC_API_KEY` | (aucune) | active `ClaudeQualifier` |
| `ARCHIBALD_MODEL` | `claude-opus-5-5` | modèle utilisé pour la qualification |
| `ARCHIBALD_EFFORT` | `low` | effort de raisonnement : conversation courte, la latence compte |

## Démo interactive (pour un rendez-vous)

`demo/index.html` est une démo autonome qui tourne dans le navigateur, sans serveur ni clé. Elle est
publiée en lien privé sur claude.ai, et `python -m archibald.cli serve` la sert aussi sur
http://127.0.0.1:8000/.

- **Trois volets** : le téléphone du client, ce que voit l'entreprise (demandes, fiche, devis et
  relances, alertes du patron), et les preuves (accords horodatés gardés 3 ans, tableau de bord,
  journal).
- **Six scénarios** : projet idéal par appel, demande de prix, client qui veut le patron, contact
  recommandé, STOP, projet hors zone. Une demande libre permet de jouer soi-même le client.
- **Horloge simulée** (+1 h, +1 jour, +3 jours, « avancer jusqu'à la prochaine relance ») pour
  montrer les relances J+3 / J+10 / J+20 et le respect des heures.
- **Script ou Claude** : ouverte dans Claude, la démo peut confier la conversation à Claude
  (sur le compte de la personne qui regarde). Le garde-fou prix s'applique aussi.
- La bande « À l'instant » explique chaque étape en une phrase : c'est le fil de la présentation.

Le moteur de la démo est un portage JavaScript des règles du prototype Python (consentement,
STOP, classement, garde-fou, relances). Les tests (`pytest`) restent la référence.

## Essayer les webhooks

```bash
curl -X POST localhost:8000/leads -d '{"company_id":"demo","telephone":"+33611111111","prenom":"Julie","message":"Extension 30 m²"}'
curl -X POST localhost:8000/sms/inbound -d '{"from":"+33611111111","text":"3"}'
curl -X POST localhost:8000/sms/inbound -d '{"from":"+33611111111","text":"30 m², maison de 110 m²"}'
curl "localhost:8000/report?company_id=demo"
```

## Ce qui est fait / ce qui reste

| Fait (prototype) | Reste à faire avant un pilote réel |
|---|---|
| SMS d'accord en premier, choix appel / plus tard / écrit | **validation du parcours par un avocat** (réforme du 11/08/2026) |
| STOP immédiat : bloque tout, relances comprises, même sur une nouvelle demande | brancher un opérateur SMS français (numéro dédié, accusés de réception, signature des webhooks) |
| preuve de chaque étape du consentement, conservée 3 ans | canal voix : opérateur + transcription en direct + synthèse vocale, branché sur le même `Qualifier` |
| qualification par Claude (sortie JSON) ou par script de secours | authentification des webhooks, chiffrement de la base, hébergement en UE |
| garde-fou : aucun montant annoncé au client, même si le modèle en écrit un | connecteurs logiciel de devis (Obat, Tolteck…) : pour l'instant export JSON générique |
| fiche classée avec raisons et seuil architecte (150 m²) | interface dirigeant (aujourd'hui : SMS + e-mail + `/report`) |
| relances J+3 / J+10 / J+20, uniquement du lundi au samedi dans les heures fixées | mesures réelles du pilote : délai de réponse, taux d'accord, visites, devis signés |
| motif d'hésitation (prix, délai, financement, concurrent) remonté au dirigeant | |

Architecture détaillée : [docs/architecture.md](docs/architecture.md).
