"""Modèle de validation demandé au sprint 2."""

from typing import Optional
from pydantic import BaseModel


class Etudiant(BaseModel):
    nom: str
    prenom: str
    age: int
    email: str
    telephone: Optional[str] = None
