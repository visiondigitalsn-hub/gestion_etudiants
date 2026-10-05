"""Générer la table puis vérifier la connexion réelle à PostgreSQL."""
from sqlalchemy import inspect, text
from database import Base, engine
import models

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    with engine.connect() as connection:
        print("Connexion :", connection.execute(text("SELECT current_database(), current_user")).one())
    print("Colonnes :", [c["name"] for c in inspect(engine).get_columns("etudiants")])
