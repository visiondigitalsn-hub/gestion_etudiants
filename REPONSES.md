# Sprint 1 - Réponses aux questions

## Partie 1 - Environnement
1. Un environnement virtuel isole les bibliothèques du projet et évite les conflits de versions avec les autres projets.
2. FastAPI permet de créer des API web en Python : routes, validation des paramètres, réponses JSON et documentation automatique.
3. Uvicorn est le serveur ASGI qui reçoit les requêtes HTTP et exécute l'application FastAPI.

## Partie 2 - Première application
Avant de définir une route racine, ouvrir http://127.0.0.1:8000 renvoie une réponse HTTP 404 avec `{"detail":"Not Found"}`. Le serveur fonctionne, mais aucune route ne correspond à ce chemin. Dans le fichier final, la route racine existe et renvoie le message de bienvenue.

## Partie 3 - Route racine
1. GET est une méthode HTTP qui demande une ressource au serveur.
2. `/` désigne le chemin racine de l'application.
3. La fonction retourne un dictionnaire Python. FastAPI le convertit en réponse JSON.

## Partie 4 - Deuxième route
1. À cette étape, il existe deux routes créées pour l'exercice. Les routes techniques de documentation sont supplémentaires.
2. `/` est le chemin racine ; `/bonjour` est un autre chemin. Ils appellent deux fonctions différentes et retournent des messages différents.

## Partie 5 - Paramètre d'URL
1. Un paramètre est une valeur transmise à la fonction pour adapter son comportement.
2. `{nom}` définit une partie variable du chemin. FastAPI transmet sa valeur à l'argument `nom`.
3. Remplacer Ali par Fatou produit `{"message":"Bonjour Fatou"}`.

## Partie 6 - Addition
1. La route possède deux paramètres de chemin : `a` et `b`.
2. Le type `int` demande des nombres entiers. FastAPI convertit les valeurs et les valide ; l'addition est numérique.
3. `/addition/abc/10` renvoie HTTP 422 : `abc` ne peut pas être converti en entier. La fonction d'addition n'est pas exécutée.

## Partie 7 - Swagger
1. Swagger UI est une interface interactive qui affiche les opérations de l'API et permet de les tester.
2. FastAPI construit le schéma OpenAPI à partir des routes et des annotations de types. Swagger UI utilise ce schéma pour afficher la documentation.
3. Les quatre opérations GET apparaissent : `/`, `/bonjour`, `/bonjour/{nom}` et `/addition/{a}/{b}`.

## URL, endpoint et route
Une URL est l'adresse complète, par exemple `http://127.0.0.1:8000/bonjour/Ali`. Une route associe une méthode et un modèle de chemin à une fonction, par exemple `GET /bonjour/{nom}`. Un endpoint est un point d'accès de l'API ; dans FastAPI, ce terme peut aussi désigner la fonction appelée pour traiter cette opération.

## Sources
- Consignes : document Sprint 1 fourni par l'enseignant.
- https://fastapi.tiangolo.com/tutorial/first-steps/
- https://fastapi.tiangolo.com/tutorial/path-params/
