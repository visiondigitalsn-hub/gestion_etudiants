# Rapport - Sprint 1 : découverte de FastAPI

**Présentation du projet.** Le projet `gestion_etudiants` est une première API Python. Il comprend quatre routes GET : accueil, salutation générale, salutation personnalisée et addition de deux entiers. Les réponses sont au format JSON. FastAPI génère une documentation interactive Swagger accessible à l'adresse `/docs`.

**Réalisation.** Un environnement virtuel `env` a été créé. Le fichier `main.py` contient l'application et les quatre fonctions associées aux routes. Les annotations `str` et `int` précisent les types des paramètres. Le guide de lancement et les réponses aux questions sont fournis séparément.

**Captures à insérer par l'étudiant.** Insérer côte à côte une capture de l'API affichant le message de bienvenue et une capture de Swagger montrant les quatre opérations. Garder le rapport final sur une seule page. Les captures ne sont pas encore jointes.

**Difficultés rencontrées et solutions.** La commande Python habituelle n'était pas disponible : l'environnement a été créé avec le Python fourni par l'application. L'installation initiale des bibliothèques a rencontré une restriction réseau. L'utilisation directe de l'interpréteur de l'environnement évite également de dépendre de l'activation PowerShell.

**Notions abordées.** Isolation des dépendances, rôle du serveur Uvicorn, création de routes, réponses JSON, paramètres de chemin, validation des entiers et utilisation de Swagger. Cette synthèse est à relire et adapter pour décrire les apprentissages personnels de l'étudiant.

**Validation.** Consulter VALIDATION.md pour les résultats réellement obtenus. Avant remise, exécuter les quatre opérations dans Swagger et insérer les deux captures.
