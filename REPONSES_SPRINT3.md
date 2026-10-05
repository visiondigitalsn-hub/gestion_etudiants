# Sprint 3 - Réponses aux questions

## Partie 1 Comprendre le CRUD

1. **Que signifie CRUD ?** Create, Read, Update et Delete : créer, lire, modifier et supprimer des données.

2. **Que fait chaque opération et quelle méthode HTTP utiliser ?** Create ajoute un étudiant avec POST. Read consulte un étudiant ou la liste avec GET. Update remplace les informations avec PUT. Delete retire un étudiant avec DELETE.

3. **Pourquoi proposer les quatre opérations ?** Ajouter permet d’inscrire un étudiant ; afficher permet de consulter les dossiers ; modifier permet de corriger les informations ; supprimer permet de retirer un dossier devenu inutile.

## Partie 2 Simuler une base de données

1. **Pourquoi utilise-t-on une liste ?** Elle permet de regrouper plusieurs objets étudiants et de les parcourir, ajouter, remplacer ou retirer simplement.

2. **Cette liste est-elle une base de données ?** Non. C’est une collection Python en mémoire, sans stockage durable ni mécanismes de base de données.

3. **Que se passe-t-il si l’on redémarre le serveur ?** Le processus recrée une liste vide et réinitialise le compteur des identifiants. Les étudiants précédents sont perdus.

## Partie 3 Ajouter un étudiant

1. **Que contient maintenant la liste ?** Les objets étudiants créés par les requêtes POST, avec leurs informations validées et leur identifiant attribué par le serveur.

2. **Les données sont-elles conservées après le redémarrage ?** Non : elles existent uniquement dans la mémoire du processus.

## Partie 4 Lister les étudiants

1. **Que retourne cette route ?** GET /etudiants retourne un tableau JSON de tous les étudiants. Si aucun étudiant n’est enregistré, la réponse est [].

2. **Pourquoi utilise-t-on GET ?** L’opération consulte les données sans les modifier.

## Partie 5 Rechercher un étudiant

1. **Pourquoi un identifiant est-il nécessaire ?** Il distingue chaque étudiant, même si deux étudiants portent le même nom. Il reste stable lors d’une modification et ne dépend pas de la position dans la liste.

2. **Que faire si l’étudiant n’existe pas ?** Lever une HTTPException avec le code 404 et un message indiquant que l’étudiant est introuvable.

## Partie 6 Modifier un étudiant

1. **Pourquoi utilise-t-on PUT ?** PUT remplace les informations de la ressource désignée par son identifiant. Les champs obligatoires doivent être envoyés ; l’identifiant est conservé. Le téléphone omis prend la valeur None.

## Partie 7 Supprimer un étudiant

1. **Pourquoi utilise-t-on DELETE ?** Cette méthode demande la suppression de la ressource identifiée. Ici, une suppression réussie renvoie 204, sans corps de réponse.

## Partie 8 Gestion des erreurs

1. **Quel code HTTP faut-il retourner ?** 404 pour la lecture, la modification ou la suppression d’un étudiant inexistant. Des paramètres ou données de types invalides produisent plutôt 422.

2. **Pourquoi gérer ces erreurs ?** Le client doit savoir que l’action n’a pas abouti et pourquoi. Cela évite de présenter un faux succès ou de modifier un autre dossier.

## Partie 9 Structure du projet

1. **Peut-on tout écrire dans main.py ?** Oui pour un petit exercice, mais le fichier devient vite difficile à lire et à maintenir.

2. **Pourquoi séparer le code ?** Chaque fichier a un rôle clair. La séparation facilite la lecture, les tests et les évolutions du projet.

3. **Quel est le rôle de schemas.py ?** Définir les modèles Pydantic : Etudiant pour les données reçues et EtudiantEnregistre pour les réponses contenant un identifiant.

4. **Quel est le rôle de data.py ?** Contenir la liste des étudiants et le compteur d’identifiants. main.py conserve les routes et la logique des opérations.

Sources : https://fastapi.tiangolo.com/tutorial/handling-errors/ ; https://fastapi.tiangolo.com/tutorial/response-status-code/
