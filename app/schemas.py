"""Contrats d'entrée et de sortie documentés pour l'API finale."""

from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Etudiant(BaseModel):
    """Informations nécessaires pour créer ou remplacer un étudiant."""
    model_config = ConfigDict(str_strip_whitespace=True)
    nom: str = Field(min_length=2, description='Nom : au moins deux caractères après retrait des espaces extérieurs.', examples=['Exemple'])
    prenom: str = Field(min_length=2, description='Prénom : au moins deux caractères.', examples=['Alice'])
    age: int = Field(gt=0, description='Âge entier strictement positif.', examples=[23])
    email: EmailStr = Field(description='Adresse e-mail de format valide. Aucune vérification de réception.', examples=['alice@example.com'])
    telephone: Optional[str] = Field(default=None, description='Téléphone facultatif. Aucun format imposé dans cet exercice.')


class EtudiantEnregistre(Etudiant):
    """Étudiant enregistré, avec son identifiant PostgreSQL."""
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(description='Identifiant attribué par PostgreSQL.', examples=[1])

class Erreur(BaseModel):
    """Message d'erreur pour une ressource inexistante."""
    detail: str = Field(description='Explication de la ressource introuvable.', examples=['Étudiant introuvable'])
