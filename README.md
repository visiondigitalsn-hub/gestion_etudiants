# Gestion des étudiants - Sprints 1 et 2

Application d'initiation avec les quatre routes demandées. Les réponses aux questions sont dans REPONSES.md. Le rapport est un document distinct.

Le sprint 2 ajoute `schemas.py` et `POST /etudiants`. Les réponses, le rapport et les résultats du sprint 2 se trouvent dans REPONSES_SPRINT2.md, RAPPORT_SPRINT2.md et VALIDATION_SPRINT2.md.

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
