"""Vérifier PostgreSQL et créer la table manuelle du sprint 4."""
from pathlib import Path
from sqlalchemy import text
from database import engine

if __name__ == '__main__':
    with engine.begin() as db:
        db.execute(text(Path(__file__).with_name('sprint4_table_manuelle.sql').read_text(encoding='utf-8')))
        print('Connexion vérifiée :', db.execute(text('SELECT current_database(), current_user, inet_server_port()')).one())
        print('Table manuelle : etudiants_manuels, schéma public.')
