"""Sprint 1 : découverte de FastAPI."""

from fastapi import FastAPI

app = FastAPI(title="Gestion des étudiants - Sprint 1")


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
