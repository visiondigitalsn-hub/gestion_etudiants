"""Sprints 1 et 2 : routes et validation des données."""

from fastapi import FastAPI, HTTPException, Response
from schemas import Etudiant, EtudiantEnregistre
import data

app = FastAPI(title="Gestion des étudiants - Sprint 3")


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


def trouver_etudiant(id: int) -> EtudiantEnregistre:
    for etudiant in data.etudiants:
        if etudiant.id == id:
            return etudiant
    raise HTTPException(status_code=404, detail="Étudiant introuvable")


@app.post("/etudiants", response_model=EtudiantEnregistre, status_code=201)
async def ajouter_etudiant(etudiant: Etudiant):
    nouvel_etudiant = EtudiantEnregistre(id=data.prochain_id, **etudiant.model_dump())
    data.prochain_id += 1
    data.etudiants.append(nouvel_etudiant)
    return nouvel_etudiant


@app.get("/etudiants", response_model=list[EtudiantEnregistre])
async def lister_etudiants():
    return data.etudiants


@app.get("/etudiants/{id}", response_model=EtudiantEnregistre)
async def lire_etudiant(id: int):
    return trouver_etudiant(id)


@app.put("/etudiants/{id}", response_model=EtudiantEnregistre)
async def modifier_etudiant(id: int, etudiant: Etudiant):
    ancien = trouver_etudiant(id)
    nouveau = EtudiantEnregistre(id=id, **etudiant.model_dump())
    data.etudiants[data.etudiants.index(ancien)] = nouveau
    return nouveau


@app.delete("/etudiants/{id}", status_code=204)
async def supprimer_etudiant(id: int):
    data.etudiants.remove(trouver_etudiant(id))
    return Response(status_code=204)
