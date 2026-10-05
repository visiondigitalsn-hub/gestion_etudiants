# Rapport du sprint 2

Projet : https://github.com/visiondigitalsn-hub/gestion_etudiants

## Ce qui a été réalisé

Le projet du sprint 1 a été complété par schemas.py, qui contient le modèle Etudiant, et par la route POST /etudiants. L’utilisateur peut envoyer un nom, un prénom, un âge et un email. Le téléphone peut être renseigné ou laissé absent. La route retourne les données validées en JSON ; aucun stockage n’est prévu dans ce sprint.

## Ce que ce travail permet de comprendre

Pydantic vérifie les données avant que la fonction de la route soit appelée. Les quatre champs principaux sont obligatoires. L’annotation int permet de convertir un âge numérique et de refuser un texte comme « vingt trois ». Optional[str] autorise une chaîne ou None, tandis que = None permet d’omettre le téléphone.

## Résultats des tests

Les données correctes sont acceptées. Un âge invalide et l’absence de l’email produisent une erreur 422 sans exécuter la fonction. Les cas avec téléphone, sans téléphone et avec la valeur null fonctionnent. Les routes GET du sprint 1 et la documentation OpenAPI ont également été vérifiées. Les essais manuels dans Swagger restent à effectuer.

## Difficulté et solution

Le point délicat est de distinguer un champ qui accepte None d’un champ qui peut être omis. La déclaration telephone: Optional[str] = None répond aux deux besoins. Le champ email reste une simple chaîne, comme demandé : le format d’une adresse email n’est donc pas contrôlé.

## Captures Swagger

À ajouter par l’étudiant : requête valide et erreur 422.
