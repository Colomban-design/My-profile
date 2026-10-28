# Brancher Archibald sur un vrai numéro

La démo (`/`) fonctionne déjà en **mode simulation** : aucun SMS ne part, on répond à la place du
client. Pour que le téléphone de la personne en face sonne vraiment, il faut trois choses :
un compte Twilio, un numéro, et une adresse publique pour le serveur.

## 1. Compte et numéro Twilio

Crée un compte sur twilio.com et note **Account SID** et **Auth Token** (page d'accueil de la console).

Deux options pour le numéro :

| | Test rapide (aujourd'hui) | Numéro français (pour les vrais rendez-vous) |
|---|---|---|
| Numéro | n'importe quel numéro proposé par la console d'essai | numéro français de type « plateforme technique » ou national, qui accepte SMS et appels |
| Délai | quelques minutes | le temps que Twilio valide le dossier |
| Ce qu'il faut | rien | Kbis ou SIREN, pièce d'identité du représentant, justificatif d'adresse en France |
| Limites | le compte d'essai n'écrit et n'appelle **que les numéros vérifiés** dans la console, et ajoute une mention « compte d'essai » | aucune pour la démo |

Les numéros mobiles français (06/07) ne conviennent pas : les opérateurs bloquent les messages
automatisés qui en partent. Vérifie les règles à jour dans les guides France de Twilio (SMS, voix,
réglementaire) au moment de commander le numéro.

Pour un rendez-vous chez un artisan avec un compte d'essai : ajoute son numéro dans
« Verified Caller IDs » juste avant (il reçoit un code), ou fais la démo avec ton propre téléphone.

## 2. Mettre le serveur en ligne

**Le plus rapide, depuis ton ordinateur** (pendant la démo, l'ordinateur doit rester allumé) :

```bash
cd archibald
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
cloudflared tunnel --url http://localhost:8000     # affiche une adresse https://….trycloudflare.com
```

**Pour que ça tourne tout le temps** : déploie le `Dockerfile` sur un hébergeur (Render, Railway,
Fly.io, Scaleway…). Choisis une offre qui ne met pas le service en veille : Twilio attend une
réponse en quelques secondes. Monte un disque sur `/data` pour garder la base (preuves d'accord).

## 3. Variables d'environnement

| Variable | Exemple | Rôle |
|---|---|---|
| `TWILIO_ACCOUNT_SID` | `AC…` | compte Twilio |
| `TWILIO_AUTH_TOKEN` | `…` | sert aussi à vérifier que les webhooks viennent bien de Twilio |
| `TWILIO_FROM` | `+339…` | le numéro Twilio |
| `PUBLIC_URL` | `https://archibald-demo.onrender.com` | adresse publique, **sans / final** |
| `DEMO_CODE` | `atelier` | code à saisir sur la page : sans lui, personne ne peut faire envoyer de SMS (recommandé) |
| `ARCHIBALD_ENTREPRISE` | `Maisons Durand Rénovation` | nom affiché et signé dans les messages |
| `ARCHIBALD_DIRIGEANT` | `Marc` | prénom du patron |
| `ARCHIBALD_TEL_DIRIGEANT` | `06 12 34 56 78` | reçoit les alertes (projet à visiter, demande de rappel) : mets le tien pendant la démo |
| `ARCHIBALD_HEURE_DEBUT` / `_FIN` | `8` / `21` | pas d'appel en dehors |
| `ANTHROPIC_API_KEY` | `sk-ant-…` | facultatif : Claude mène la conversation au lieu du script |
| `DEMO_MAX_PAR_NUMERO` / `DEMO_MAX_PAR_JOUR` | `3` / `50` | plafonds anti-abus |

Puis : `python -m archibald.cli serve --host 0.0.0.0` (ou le Dockerfile). Le terminal affiche
« Mode réel : SMS et appels via Twilio ».

## 4. Relier le numéro au serveur

Dans la console Twilio → Phone Numbers → ton numéro → **Messaging** :
« A message comes in » → Webhook → `PUBLIC_URL/twilio/sms` → HTTP POST.

Rien à régler côté voix : les appels sont lancés par Archibald, qui donne lui-même à Twilio
l'adresse à suivre (`/twilio/voice/answer`).

## 5. Vérifier avant un rendez-vous

1. Ouvre `PUBLIC_URL` sur ton téléphone, entre ton prénom, ton numéro et le code.
2. Tu reçois le SMS : réponds **3**, réponds aux questions, la fiche apparaît sur la page et
   l'alerte arrive sur le téléphone du patron.
3. Refais un essai en répondant **1** (entre 8 h et 21 h) : ton téléphone sonne, l'assistant se
   présente comme une IA et pose les questions à voix haute.
4. Réponds **STOP** sur un troisième essai : plus rien ne part vers ce numéro.

## Déroulé de démo conseillé (2 minutes)

1. « Donnez-moi votre numéro, comme si vous étiez un client qui demande un devis sur votre site. »
2. Son téléphone vibre dans les secondes qui suivent. Il répond 1 : son téléphone sonne.
3. Il répond aux questions. Pendant ce temps, ton téléphone (le « patron ») reçoit l'alerte.
4. Montre la fiche sur la page : « Voilà ce que vous recevez ce soir, sans avoir décroché. »

## Avant de l'utiliser avec de vrais clients

La démo n'écrit qu'aux personnes qui tapent elles-mêmes leur numéro et cochent la case. Pour les
vrais clients d'un artisan, le parcours d'accord doit d'abord être validé par un avocat.
