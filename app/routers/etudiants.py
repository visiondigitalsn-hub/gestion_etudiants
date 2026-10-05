"""Routes HTTP : validation, dépendance de session et erreurs 404."""
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix='/etudiants', tags=['Étudiants'])

@router.post('',response_model=schemas.EtudiantEnregistre,status_code=201)
def ajouter_etudiant(etudiant: schemas.Etudiant, db: Session = Depends(get_db)):
    return crud.creer(db, etudiant)

@router.get('',response_model=list[schemas.EtudiantEnregistre])
def lister_etudiants(db: Session = Depends(get_db)):
    return crud.lister(db)

@router.get('/{id}',response_model=schemas.EtudiantEnregistre)
def lire_etudiant(id: int, db: Session = Depends(get_db)):
    etudiant = crud.lire(db, id)
    if etudiant is None:
        raise HTTPException(status_code=404,detail='Étudiant introuvable')
    return etudiant

@router.put('/{id}',response_model=schemas.EtudiantEnregistre)
def modifier_etudiant(id: int, etudiant: schemas.Etudiant, db: Session = Depends(get_db)):
    resultat = crud.modifier(db, id, etudiant)
    if resultat is None:
        raise HTTPException(status_code=404,detail='Étudiant introuvable')
    return resultat

@router.delete('/{id}',status_code=204)
def supprimer_etudiant(id: int, db: Session = Depends(get_db)):
    if not crud.supprimer(db, id):
        raise HTTPException(status_code=404,detail='Étudiant introuvable')
    return Response(status_code=204)
