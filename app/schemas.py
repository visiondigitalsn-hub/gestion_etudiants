"""Modèle de validation demandé au sprint 2."""

from typing import Optional
from pydantic import BaseModel, ConfigDict


class Etudiant(BaseModel):
    nom: str
    prenom: str
    age: int
    email: str
    telephone: Optional[str] = None


class EtudiantEnregistre(Etudiant):
    model_config = ConfigDict(from_attributes=True)
    id: int
