# Sprint 3 - Validation

Les scripts verifier.py, verifier_sprint2.py et verifier_sprint3.py ont tous réussi. Les tests ne laissent pas de données dans le stockage après leur exécution.

## Vérifications automatiques
- Création de deux étudiants, réponse HTTP 201 et identifiants distincts.
- Liste complète et lecture par identifiant, HTTP 200.
- Remplacement par PUT et conservation de l'identifiant.
- Suppression, HTTP 204 sans corps, puis absence dans la liste et HTTP 404 à la lecture.
- Identifiants non réutilisés après une suppression.
- Lecture, modification et suppression inexistantes : HTTP 404, aucune mutation de la liste.
- Corps invalide et identifiant non entier : HTTP 422, aucune mutation.
- Routes historiques du sprint 1 et validation du sprint 2 préservées.

## Vérifications effectuées dans Swagger
GET /, POST /etudiants deux fois, GET /etudiants, GET /etudiants/1, PUT /etudiants/1, nouvelle lecture, DELETE /etudiants/1, nouvelle liste, puis GET, PUT et DELETE sur /etudiants/100. Les codes et résultats attendus ont été observés. Les étudiants utilisés sont fictifs et les emails utilisent le domaine example.com.

## Stockage
Après les essais Swagger, le serveur a été redémarré. GET /etudiants a répondu HTTP 200 avec [] : la perte du stockage en mémoire a été constatée.

La liste et le compteur existent seulement dans le processus. Ils sont perdus au redémarrage. Utiliser un seul processus Uvicorn pour cet exercice : plusieurs processus posséderaient des listes indépendantes.
