"""Appliquer les migrations puis vérifier la connexion PostgreSQL."""
from pathlib import Path
from alembic import command
from alembic.config import Config
from sqlalchemy import inspect, text
from database import Base, engine
import models

if __name__ == "__main__":
    command.upgrade(Config(str(Path(__file__).with_name('alembic.ini'))), 'head')
    with engine.connect() as connection:
        print("Connexion :", connection.execute(text("SELECT current_database(), current_user")).one())
    print("Colonnes :", [c["name"] for c in inspect(engine).get_columns("etudiants")])
