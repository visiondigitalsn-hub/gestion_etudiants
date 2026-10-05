# Gestion des étudiants - Sprint 1

Application d'initiation avec les quatre routes demandées. Les réponses aux questions sont dans REPONSES.md. Le rapport est un document distinct.

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
