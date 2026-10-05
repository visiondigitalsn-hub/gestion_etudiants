"""Cycle réel PostgreSQL dans un schéma de test unique, sans toucher aux données."""
from pathlib import Path
from uuid import uuid4
from alembic import command
from alembic.config import Config
from sqlalchemy import inspect, text
from database import engine

def verifier():
    assert engine.dialect.name == 'postgresql'
    schema = 'test_sprint6_' + uuid4().hex
    config = Config(str(Path(__file__).with_name('alembic.ini')))
    with engine.connect() as db:
        db.execute(text(f'CREATE SCHEMA "{schema}"'))
        db.commit()
        try:
            db.execute(text(f'SET search_path TO "{schema}"'))
            db.commit()
            config.attributes['connection'] = db
            command.upgrade(config, '0001')
            assert 'telephone' not in {c['name'] for c in inspect(db).get_columns('etudiants',schema=schema)}
            assert db.execute(text('SELECT version_num FROM alembic_version')).scalar_one() == '0001'
            db.execute(text("INSERT INTO etudiants(nom,prenom,age,email) VALUES ('Test','Migration',21,'migration@example.com')"))
            avant = db.execute(text('SELECT id,nom,prenom,age,email FROM etudiants ORDER BY id')).all()
            db.commit()
            command.upgrade(config, 'head')
            colonne = next(c for c in inspect(db).get_columns('etudiants',schema=schema) if c['name']=='telephone')
            assert colonne['nullable']
            assert db.execute(text('SELECT version_num FROM alembic_version')).scalar_one() == '0002'
            assert db.execute(text('SELECT id,nom,prenom,age,email FROM etudiants ORDER BY id')).all() == avant
            assert db.execute(text('SELECT telephone FROM etudiants')).scalar_one() is None
            db.commit()
            command.check(config)
            command.upgrade(config, 'head')
            assert db.execute(text('SELECT id,nom,prenom,age,email FROM etudiants ORDER BY id')).all() == avant
            db.commit()
            print('OK : 0001 sans téléphone, 0002 avec téléphone nullable, données conservées, version et upgrade idempotent.')
        finally:
            db.rollback()
            db.execute(text('SET search_path TO public'))
            db.execute(text(f'DROP SCHEMA "{schema}" CASCADE'))
            db.commit()

if __name__ == '__main__':
    verifier()
