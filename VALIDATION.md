# Validation du sprint 1

Vérifications réellement exécutées avec `python verifier.py` dans l'environnement du projet : toutes réussies.

- Sept réponses JSON conformes : accueil, bonjour, Ali, Fatou, Mamadou, addition 10 + 20, addition -5 + 2.
- Une entrée non entière dans l'addition renvoie HTTP 422 avec une erreur localisée sur le paramètre `a`.
- Swagger répond HTTP 200 et contient l'interface Swagger UI.
- OpenAPI répond HTTP 200 et décrit exactement les quatre chemins de l'exercice en GET.
- Une application FastAPI sans route racine renvoie bien HTTP 404 sur `/`, comme à l'étape initiale du sprint.

Ces vérifications utilisent le client de test de FastAPI. Elles ne remplacent pas l'exécution manuelle des quatre opérations avec le bouton Execute de Swagger.

Le serveur Uvicorn a également été lancé : les requêtes HTTP réelles vers la racine et Swagger ont répondu 200.

## À terminer par l'étudiant
1. Ouvrir http://127.0.0.1:8000/docs et exécuter les quatre opérations GET.
2. Prendre une capture du message de bienvenue et une capture de Swagger.
3. Insérer les deux captures dans le rapport, conserver une page maximum et adapter les apprentissages à son expérience.

## Rejouer la vérification
```powershell
.\env\Scripts\python.exe -m pip install -r requirements-test.txt
.\env\Scripts\python.exe verifier.py
```
