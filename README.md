# Gestion des étudiants - Sprint 6 : migrations Alembic

Le schéma PostgreSQL est désormais versionné. `alembic/` contient l'environnement et le modèle de script ; `migrations/` contient les révisions `0001` (création sans téléphone) et `0002` (ajout du téléphone facultatif).

## Nouvelle base vide

Après création de la base et configuration des variables PostgreSQL décrites ci-dessous :

```powershell
pip install -r requirements.txt
python -m alembic upgrade head
python -m alembic current
python -m alembic check
uvicorn main:app --reload
```

`initialiser_base.py` applique maintenant les migrations au lieu de `create_all()`.

## Base existante des sprints 4 et 5

Le téléphone était déjà présent. Ne pas rejouer une migration de création sur cette table. Le script suivant compare d'abord le schéma réel au modèle, refuse un écart ou une version intermédiaire, puis enregistre la version actuelle sans modifier les étudiants :

```powershell
python adopter_base_existante.py
python -m alembic check
```

`stamp` mémorise une version ; il n'exécute pas les opérations de la migration. Ne pas l'utiliser à l'aveugle sur une base différente.

## Cycle demandé dans le sprint 6

Sur une base de démonstration vide séparée, appliquer `python -m alembic upgrade 0001`, insérer quelques étudiants sans téléphone, puis appliquer `python -m alembic upgrade head`. Les colonnes historiques et les lignes restent présentes ; le téléphone des lignes existantes vaut NULL.

Les migrations ont été générées avec `revision --autogenerate` en faisant évoluer le modèle de sa version sans téléphone à sa version finale. Pour une prochaine évolution : modifier `models.py`, lancer `python -m alembic revision --autogenerate -m 'description'`, relire le script généré, puis appliquer `python -m alembic upgrade head`.

## Tests et historique

```powershell
pip install -r requirements-test.txt
python verifier_sprint6.py
python verifier_sprint45.py
python verifier.py
python -m alembic history
```

Le test du sprint 6 utilise un schéma temporaire unique et nettoie seulement ses propres tables. Il vérifie la première version, l'ajout nullable, la conservation des données, la révision finale, l'absence de différences et la répétition sans effet de `upgrade head`.

L'autogénération ignore la table manuelle `etudiants_manuels`, qui reste en dehors du modèle ORM. Les fonctions `downgrade()` sont fournies, mais supprimer une colonne retire ses valeurs : un retour arrière ne remplace pas une sauvegarde.

Le code et les tests sont sur GitHub ; le rapport et les captures sont fournis séparément pour le Drive.

## Guide de connexion et exercices des sprints 4 et 5

FastAPI, PostgreSQL et SQLAlchemy : les étudiants sont conservés dans la base après le redémarrage de l'API.

## Préparer PostgreSQL

Installer PostgreSQL depuis https://www.postgresql.org/download/windows/ et démarrer le serveur. Créer la base `gestion_etudiants` dans pgAdmin ou avec `createdb -U postgres gestion_etudiants`. Le mot de passe reste sur votre ordinateur.

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
$env:PGHOST = '127.0.0.1'
$env:PGPORT = '5432'
$env:PGUSER = 'postgres'
$env:PGDATABASE = 'gestion_etudiants'
$sprintDbSecret = Read-Host 'Mot de passe PostgreSQL' -AsSecureString
$env:PGPASSWORD = [System.Net.NetworkCredential]::new('', $sprintDbSecret).Password
```

`DATABASE_URL` peut remplacer ces variables. Ne pas publier sa valeur si elle contient un mot de passe.

## Sprint 4 : connexion et table manuelle

```powershell
python preparer_sprint4.py
```

Le script crée `public.etudiants_manuels`. Cette table séparée permet de comparer le SQL manuel et la génération ORM sans écraser de données.

## Sprint 5 : table ORM, insertion, lecture et API

```powershell
python initialiser_base.py
python demo_orm.py
uvicorn main:app --reload
```

Swagger : http://127.0.0.1:8000/docs

La table `public.etudiants` possède `id`, `nom`, `prenom`, `age`, `email`. Le téléphone facultatif du sprint 2 est conservé. Pydantic valide les entrées ; SQLAlchemy représente les lignes PostgreSQL.

Les routes CRUD restent disponibles : POST `/etudiants` (201), GET `/etudiants`, GET et PUT `/etudiants/{id}` (200), DELETE `/etudiants/{id}` (204). Un identifiant absent donne 404 et une entrée invalide 422. PUT remplace tous les champs, avec téléphone nul s'il est omis.

## Tests sur PostgreSQL réel

```powershell
pip install -r requirements-test.txt
python verifier.py
python verifier_sprint45.py
```

Les tests vérifient la table, le CRUD, la validation, la persistance entre sessions et le rollback sans commit. Ils créent des données fictives et retirent uniquement celles-ci. Les tests historiques des sprints 2 et 3 restent sur leurs branches.

## Fichiers

- `main.py` : routes FastAPI et session par requête.
- `database.py` : Engine, SessionLocal, Base et fermeture des sessions.
- `models.py` : modèle ORM Etudiant.
- `schemas.py` : validation Pydantic et sérialisation ORM.
- `demo_orm.py` : insertion idempotente de deux étudiants fictifs et lecture.
- `preuve_postgresql.py` : export local de résultats SQL pour contrôle.

Les rapports et captures sont fournis séparément pour le Drive du professeur.
