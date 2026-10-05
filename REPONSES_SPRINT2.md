# Sprint 2 - Réponses aux questions

## Partie 1 Comprendre Pydantic

1. **Qu’est-ce que Pydantic ?** Une bibliothèque Python qui valide et convertit des données à partir des annotations de types.

2. **Pourquoi valider les données ?** Pour détecter les champs manquants et les valeurs incompatibles avant de les traiter.

3. **Qu’est-ce que BaseModel ?** La classe de base de Pydantic dont hérite Etudiant pour définir ses champs et bénéficier de la validation.

4. **Quelle différence entre nom: str et telephone: Optional[str] = None ?** nom est une chaîne obligatoire. telephone accepte une chaîne ou None ; sa valeur par défaut None permet de ne pas l’envoyer.

5. **Pourquoi est-il dangereux d’accepter n’importe quelles données ?** Des valeurs incohérentes peuvent provoquer des erreurs ou fausser les traitements. La validation des types ne remplace toutefois pas les autres contrôles de sécurité.

6. **Que se passe-t-il avec un âge égal à « vingt ans » ?** La conversion en entier échoue. FastAPI renvoie HTTP 422. Si le JSON ne contient que nom et age, les autres champs obligatoires manquent aussi.

## Partie 2 Le modèle Etudiant

1. **Quels champs sont obligatoires ?** nom, prenom, age et email. telephone est optionnel dans la version finale.

2. **Quels types sont utilisés ?** str pour nom, prenom et email ; int pour age ; Optional[str] pour telephone.

3. **Pourquoi utiliser des annotations de types ?** Elles définissent les données attendues, guident la validation et alimentent la documentation automatique.

## Partie 3 Comprendre POST

1. **Qu’est-ce qu’une requête POST ?** Une requête HTTP qui envoie des données au serveur pour qu’il les traite, souvent pour créer une ressource.

2. **Quelle différence entre GET et POST ?** GET demande une ressource. POST soumet des données, généralement dans le corps de la requête, et peut modifier l’état du serveur.

3. **Dans quels cas utilise-t-on POST ?** Pour envoyer un formulaire, créer un compte ou soumettre les informations d’un étudiant.

4. **Quelle méthode pour chaque action ?** Consulter : GET. Ajouter : POST. Modifier : PUT pour un remplacement, PATCH pour une modification partielle. Supprimer : DELETE.

## Partie 4 La route POST

1. **Où se trouvent les données envoyées ?** Dans le corps de la requête HTTP, ici au format JSON.

2. **Pourquoi utilise-t-on le modèle Etudiant ?** Il décrit la structure attendue et permet de recevoir des données validées sous forme d’objet Python.

3. **Que fait FastAPI avant d’exécuter la fonction ?** Il lit le JSON et utilise Pydantic pour le valider et le convertir en Etudiant. En cas d’erreur, il renvoie HTTP 422.

## Partie 5 Validation automatique

1. **Pourquoi FastAPI refuse-t-il les données incorrectes ?** « vingt trois » n’est pas convertible en entier. Dans l’autre cas, email est absent alors qu’il est obligatoire.

2. **Qui réalise la validation ?** Pydantic, intégré au traitement des requêtes de FastAPI.

3. **La fonction est-elle exécutée lorsqu’une erreur existe ?** Non. La validation échoue avant l’appel de la fonction qui traite la route.

## Partie 6 Champs optionnels

1. **Pourquoi les deux cas fonctionnent-ils ?** Un téléphone fourni comme chaîne est accepté ; s’il est absent, sa valeur par défaut est None.

2. **Quel est le rôle de Optional ?** Optional[str] autorise une chaîne ou None. À lui seul, il ne rend pas le champ omissible en Pydantic 2.

3. **Pourquoi utilise-t-on = None ?** C’est la valeur par défaut utilisée lorsque le champ n’est pas envoyé. Elle rend le champ non obligatoire.

## Partie 7 Exploration de Swagger

1. **Pourquoi Swagger connaît-il la structure de l’étudiant ?** Le schéma OpenAPI décrit les champs, les types et les champs obligatoires du modèle Pydantic.

2. **Qui génère cette documentation ?** FastAPI génère le schéma OpenAPI ; Swagger UI l’affiche sous forme interactive.

3. **Quel est l’avantage pour un développeur ?** Il voit les données attendues et peut envoyer des requêtes et examiner les réponses sans écrire de client.

Sources : https://fastapi.tiangolo.com/tutorial/body/ ; https://docs.pydantic.dev/latest/concepts/fields/
