"""Modèle ORM : une instance représente une ligne PostgreSQL."""
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Etudiant(Base):
    __tablename__ = "etudiants"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom: Mapped[str] = mapped_column(String, nullable=False)
    prenom: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    telephone: Mapped[str | None] = mapped_column(String, nullable=True)
