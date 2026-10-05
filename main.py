"""Sprint 6 : API PostgreSQL avec un schéma versionné par Alembic."""

from fastapi import FastAPI, HTTPException, Response, Depends
from schemas import Etudiant, EtudiantEnregistre
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import get_db
from models import Etudiant as EtudiantORM

app = FastAPI(title="Gestion des étudiants - Sprint 6")


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


def trouver_etudiant(id: int, db: Session) -> EtudiantORM:
    etudiant = db.get(EtudiantORM, id)
    if etudiant is None:
        raise HTTPException(status_code=404, detail="Étudiant introuvable")
    return etudiant


@app.post("/etudiants", response_model=EtudiantEnregistre, status_code=201)
def ajouter_etudiant(etudiant: Etudiant, db: Session = Depends(get_db)):
    nouveau = EtudiantORM(**etudiant.model_dump())
    db.add(nouveau)
    db.commit()
    db.refresh(nouveau)
    return nouveau


@app.get("/etudiants", response_model=list[EtudiantEnregistre])
def lister_etudiants(db: Session = Depends(get_db)):
    return db.scalars(select(EtudiantORM).order_by(EtudiantORM.id)).all()


@app.get("/etudiants/{id}", response_model=EtudiantEnregistre)
def lire_etudiant(id: int, db: Session = Depends(get_db)):
    return trouver_etudiant(id, db)


@app.put("/etudiants/{id}", response_model=EtudiantEnregistre)
def modifier_etudiant(id: int, etudiant: Etudiant, db: Session = Depends(get_db)):
    actuel = trouver_etudiant(id, db)
    for champ, valeur in etudiant.model_dump().items():
        setattr(actuel, champ, valeur)
    db.commit()
    db.refresh(actuel)
    return actuel


@app.delete("/etudiants/{id}", status_code=204)
def supprimer_etudiant(id: int, db: Session = Depends(get_db)):
    db.delete(trouver_etudiant(id, db))
    db.commit()
    return Response(status_code=204)


