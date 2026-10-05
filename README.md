# Gestion des étudiants — Sprints 4 et 5

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
