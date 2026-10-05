"""Reconnaître le schéma du sprint 5, après comparaison, sans modifier ses lignes."""
from pathlib import Path
from alembic import command
from alembic.autogenerate import compare_metadata
from alembic.config import Config
from alembic.migration import MigrationContext
from alembic.script import ScriptDirectory
from sqlalchemy import text
from database import Base, engine
import models

def adopter():
    config = Config(str(Path(__file__).with_name('alembic.ini')))
    head = ScriptDirectory.from_config(config).get_current_head()
    with engine.connect() as db:
        ctx = MigrationContext.configure(db, opts={
            'compare_type': True,
            'include_object': lambda obj, name, typ, reflected, compare_to:
                typ != 'table' or name in Base.metadata.tables,
        })
        version = ctx.get_current_revision()
        if version not in (None, head):
            raise RuntimeError('La base est déjà versionnée : utiliser alembic upgrade head.')
        differences = compare_metadata(ctx, Base.metadata)
        if differences:
            raise RuntimeError('Schéma différent du modèle : adoption refusée. Examiner la base.')
        avant = db.execute(text('SELECT * FROM etudiants ORDER BY id')).all()
    command.stamp(config, head)
    with engine.connect() as db:
        assert db.execute(text('SELECT * FROM etudiants ORDER BY id')).all() == avant
        assert db.execute(text('SELECT version_num FROM alembic_version')).scalar_one() == head
    print(f'Adoption vérifiée : révision {head}, {len(avant)} étudiants conservés. Aucun ALTER TABLE exécuté.')

if __name__ == '__main__':
    adopter()
