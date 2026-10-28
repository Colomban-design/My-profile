# Prospection : trouver les 5 premiers pilotes

L'objectif vient de `founder/launch.md` : **5 pilotes gratuits** dans une région, à partir de
**300 entreprises** repérées et **40 démos**. Cet outil automatise ce qui est répétitif : la liste,
le classement, les e-mails et leurs relances, le repérage des réponses, la préparation des appels.
Les appels et les démos restent faits par toi : ce sont eux qui signent les pilotes.

## Mise en route (une fois, 30 minutes)

```bash
cd My-profile                       # la racine du dépôt
python -m prospection trouver --departements 69,01,38     # remplace par ta région
python -m prospection enrichir                            # facultatif, clé Google nécessaire
```

1. **La liste** : `trouver` interroge l'annuaire officiel des entreprises (gratuit, sans clé) :
   construction de maisons, maçonnerie et gros œuvre, finitions, couverture, de 1 à 49 salariés,
   en activité. Le résultat est dans `prospection/donnees/prospects.csv`, trié par score.
2. **Les contacts** : l'annuaire ne donne ni téléphone ni e-mail.
   - `enrichir` ajoute le téléphone, le site, la note et le nombre d'avis Google, avec une clé
     `GOOGLE_MAPS_API_KEY` (API « Places API (New) », payante au-delà du crédit gratuit de Google).
   - **Les e-mails, c'est toi** : pour les 50 meilleurs scores, ouvre leur site et recopie
     l'adresse de la page contact dans la colonne `email`. Compte environ 20 minutes. Ne devine
     jamais une adresse (prenom.nom@…).
   - Tu as une liste d'un salon, d'une CAPEB ou de ton réseau ? `python -m prospection importer liste.csv`.
3. **Ta boîte d'envoi**, en variables d'environnement :

| Variable | Exemple |
|---|---|
| `SMTP_HOST` / `SMTP_PORT` | `smtp.gmail.com` / `587` |
| `SMTP_USER` / `SMTP_PASSWORD` | ton adresse / un « mot de passe d'application » |
| `SMTP_FROM` | `Prénom Nom <prenom@archibald-renov.fr>` |
| `IMAP_HOST` | `imap.gmail.com` : repère tout seul les réponses et les « stop » |
| `PROSPECTION_EXPEDITEUR` / `PROSPECTION_TEL` | ton prénom / ton numéro |
| `PROSPECTION_LIEN_DEMO` / `PROSPECTION_CODE_DEMO` | l'adresse de la démo en ligne / son code |
| `PROSPECTION_ZONE` | `dans le Rhône` |
| `PROSPECTION_MAX_PAR_JOUR` | `30` (ne pas dépasser au début) |

**Délivrabilité.** Envoie depuis un domaine secondaire (par ex. `archibald-renov.fr`), avec SPF,
DKIM et DMARC configurés chez l'hébergeur du domaine. Les deux premières semaines, commence à
10 e-mails par jour, puis 20, puis 30. Les e-mails partent en texte brut, un par un, avec une
minute d'écart.

## Chaque matin (10 minutes + tes appels)

```bash
python -m prospection jour              # essai : montre ce qui partirait, rien n'est envoyé
python -m prospection jour --vraiment   # envoie
```

Dans l'ordre, la commande :
1. lit ta boîte de réception : qui a répondu (→ à rappeler), qui a dit stop (→ retiré pour toujours) ;
2. envoie les e-mails dus, dans le plafond du jour, du lundi au vendredi de 7 h à 19 h :
   - **e-mail 1** : le problème des demandes du soir et le lien de démo sur son téléphone,
   - **e-mail 2** (4 jours ouvrés plus tard) : la relance des devis,
   - **e-mail 3** (6 jours ouvrés après le 2) : le dernier message ;
3. écrit `donnees/appels-AAAA-MM-JJ.md` : les 10 appels du jour (ceux qui ont répondu d'abord),
   avec le script et les réponses aux objections.

Après chaque appel : `python -m prospection marquer <siren> demo "RDV jeudi 8h"`
(statuts : `repondu`, `demo`, `pilote`, `client`, `pas_interesse`, `stop`).
Pour voir les 3 e-mails d'un prospect avant envoi : `python -m prospection apercu <siren>`.

## Les règles (France, prospection entre professionnels)

- **E-mail** : pas besoin d'accord préalable, mais le message doit concerner l'activité
  professionnelle du destinataire. Chaque e-mail dit d'où viennent ses coordonnées et permet de
  se désinscrire en répondant « stop ». L'outil retire alors l'adresse définitivement.
- **Adresses** : uniquement celles publiées par l'entreprise elle-même (page contact). Pas
  d'adresses devinées ni achetées.
- **Téléphone** : c'est toi qui appelles, une personne à la fois, sur le numéro professionnel.
  Pas de robot d'appel ni de SMS automatique vers les prospects. Les règles du démarchage
  téléphonique ont changé le 11/08/2026 : vérifie sur cnil.fr ce qui s'applique entre
  professionnels.
- **LinkedIn** : à la main seulement. Les outils d'automatisation sont interdits par LinkedIn.
- Fais valider ces points par l'avocat qui valide déjà le parcours d'accord d'Archibald.

## Limites connues

- Je n'ai pas pu appeler l'annuaire officiel ni Google depuis l'environnement où l'outil a été
  écrit. La lecture des réponses suit leur format publié, et l'outil s'arrête avec un message
  clair si une réponse ne ressemble pas à ce qu'il attend. Lance d'abord
  `trouver --departements 69 --max 25` pour vérifier.
- Le score est une règle simple (métier, taille, ancienneté, site, avis). Ajuste-le dans
  `crm.py` après les 20 premiers appels, selon qui a vraiment répondu.
