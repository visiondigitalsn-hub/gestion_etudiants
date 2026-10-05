"""Connexion PostgreSQL et sessions SQLAlchemy (sprints 4 et 5)."""
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

url = os.getenv("DATABASE_URL") or URL.create(
    "postgresql+psycopg", username=os.getenv("PGUSER", "postgres"),
    password=os.getenv("PGPASSWORD"), host=os.getenv("PGHOST", "127.0.0.1"),
    port=int(os.getenv("PGPORT", "5432")), database=os.getenv("PGDATABASE", "gestion_etudiants"),
)
engine = create_engine(url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
