"""Sprints 1 et 2 : routes et validation des données."""

from fastapi import FastAPI
from schemas import Etudiant

app = FastAPI(title="Gestion des étudiants - Sprints 1 et 2")


@app.get("/")
def accueil():
    return {"message": "Bienvenue dans mon API"}


@app.get("/bonjour")
def bonjour():
    return {"message": "Bonjour à tous"}


@app.get("/bonjour/{nom}")
def bonjour_personnalise(nom: str):
    return {"message": f"Bonjour {nom}"}


@app.get("/addition/{a}/{b}")
def addition(a: int, b: int):
    return {"resultat": a + b}


@app.post("/etudiants", response_model=Etudiant)
def recevoir_etudiant(etudiant: Etudiant):
    """Retourner les données validées, sans stockage à ce stade."""
    return etudiant
