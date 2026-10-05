# Gestion des étudiants - Sprint 3

Application d'initiation avec les quatre routes demandées. Les réponses aux questions sont dans REPONSES.md. Le rapport est un document distinct.

Le sprint 2 ajoute `schemas.py` et `POST /etudiants`. Les réponses, le rapport et les résultats du sprint 2 se trouvent dans REPONSES_SPRINT2.md, RAPPORT_SPRINT2.md et VALIDATION_SPRINT2.md.

## Sprint 3 - CRUD en mémoire

`data.py` contient la liste et le compteur. `schemas.py` définit les modèles d'entrée et de réponse. `main.py` contient les routes. Les étudiants sont perdus au redémarrage : utiliser un seul processus Uvicorn.

| Opération | Route | Succès |
| --- | --- | --- |
| Créer | POST /etudiants | 201, étudiant avec id |
| Lister | GET /etudiants | 200, tableau JSON |
| Rechercher | GET /etudiants/{id} | 200, étudiant |
| Remplacer | PUT /etudiants/{id} | 200, étudiant modifié |
| Supprimer | DELETE /etudiants/{id} | 204, sans corps |

Une ressource inexistante renvoie 404 ; les données invalides renvoient 422. Le compteur ne réutilise pas les identifiants supprimés pendant la vie du processus. PUT attend tous les champs obligatoires et conserve l'id ; omettre le téléphone remet sa valeur à null.

Dans Swagger : créer deux étudiants fictifs (emails sous example.com), lister, rechercher le premier id, modifier ses champs, relire, supprimer, puis relister. Tester aussi GET, PUT et DELETE avec un id absent comme 100. Pour PUT, fournir un corps valide afin de vérifier le 404 plutôt qu'une erreur de validation.

Réponses et résultats : REPONSES_SPRINT3.md et VALIDATION_SPRINT3.md. Le rapport Word complet avec captures est fourni séparément.

```powershell
.\env\Scripts\python.exe -m pip install -r requirements-test.txt
.\env\Scripts\python.exe verifier.py
.\env\Scripts\python.exe verifier_sprint2.py
.\env\Scripts\python.exe verifier_sprint3.py
```

Les indications du sprint 2 ci-dessous décrivent sa version initiale. Avec le sprint 3, POST stocke maintenant l'étudiant et renvoie 201 avec un id supplémentaire.

## Tester le sprint 2 dans Swagger

Ouvrir `/docs`, déplier **POST /etudiants**, cliquer sur **Try it out**, coller l’un des JSON ci-dessous, puis **Execute**.

```json
{"nom":"Fall","prenom":"Mamadou","age":23,"email":"mamadou@gmail.com"}
```

Réponse attendue HTTP 200 : mêmes données avec `"telephone": null`.

```json
{"nom":"Fall","prenom":"Mamadou","age":"vingt trois","email":"mamadou@gmail.com"}
```

Réponse attendue HTTP 422, erreur sur age.

```json
{"nom":"Fall","prenom":"Mamadou","age":23}
```

Réponse attendue HTTP 422, email obligatoire manquant.

```json
{"nom":"Ali","prenom":"Diop","age":22,"email":"ali@gmail.com","telephone":"771234567"}
```

Réponse attendue HTTP 200. Retirer telephone, puis tester à nouveau : HTTP 200 et telephone null.

Le modèle demandé valide les types : `email: str` ne vérifie pas le format d’une adresse. Aucun stockage d’étudiants n’est implémenté à ce stade ; la route retourne les données validées.

## Installation standard sous Windows PowerShell

Depuis le dossier gestion_etudiants, sur une machine où Python est installé :

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Si l'activation est bloquée, utiliser directement l'interpréteur de l'environnement :

```powershell
.\env\Scripts\python.exe -m pip install -r requirements.txt
.\env\Scripts\python.exe -m uvicorn main:app --reload
```

## Vérifications attendues

| Chemin | Résultat |
| --- | --- |
| `/` | `{"message":"Bienvenue dans mon API"}` |
| `/bonjour` | `{"message":"Bonjour à tous"}` |
| `/bonjour/Ali` | `{"message":"Bonjour Ali"}` |
| `/bonjour/Fatou` | `{"message":"Bonjour Fatou"}` |
| `/bonjour/Mamadou` | `{"message":"Bonjour Mamadou"}` |
| `/addition/10/20` | `{"resultat":30}` |
| `/addition/abc/10` | HTTP 422, erreur de validation |

Ouvrir http://127.0.0.1:8000/docs. Déplier chaque opération, cliquer sur **Try it out**, renseigner les paramètres si nécessaire, puis cliquer sur **Execute**. Vérifier le code HTTP et le corps de la réponse.

Le dossier env contient un environnement local : il n'est pas portable entre ordinateurs. Le recréer avec les commandes ci-dessus sur une autre machine.

