"""Migrations PostgreSQL utilisant la configuration du projet, sans secret en dur."""
from alembic import context
from app.database import Base, engine
from app import models

target_metadata = Base.metadata

def include_object(obj, name, type_, reflected, compare_to):
    # La table manuelle du sprint 4 ne fait pas partie de ce modèle ORM.
    return type_ != "table" or name in target_metadata.tables

if context.is_offline_mode():
    context.configure(url=engine.url, target_metadata=target_metadata,
                      literal_binds=True, dialect_opts={"paramstyle": "named"},
                      include_object=include_object, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()
else:
    def run_with_connection(connection):
        context.configure(connection=connection, target_metadata=target_metadata,
                          include_object=include_object, compare_type=True)
        with context.begin_transaction():
            context.run_migrations()

    external_connection = context.config.attributes.get("connection")
    if external_connection is not None:
        run_with_connection(external_connection)
    else:
        with engine.connect() as connection:
            run_with_connection(connection)
