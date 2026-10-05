"""Routes HTTP : validation, dépendance de session et erreurs 404."""
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, Path
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix='/etudiants', tags=['Étudiants'])
Identifiant = Annotated[int, Path(gt=0,description='Identifiant entier strictement positif de l’étudiant.')]
ressource_absente = {404:{'model':schemas.Erreur,'description':'Aucun étudiant ne possède cet identifiant.'}}

@router.post('',response_model=schemas.EtudiantEnregistre,status_code=201,
             summary='Créer un étudiant',description='Valide les informations et enregistre un nouvel étudiant dans PostgreSQL.',response_description='Étudiant créé avec son identifiant.')
def ajouter_etudiant(etudiant: schemas.Etudiant, db: Session = Depends(get_db)):
    return crud.creer(db, etudiant)

@router.get('',response_model=list[schemas.EtudiantEnregistre],summary='Lister les étudiants',
            description='Retourne tous les étudiants, classés par identifiant. Une base vide retourne une liste vide.')
def lister_etudiants(db: Session = Depends(get_db)):
    return crud.lister(db)

@router.get('/{id}',response_model=schemas.EtudiantEnregistre,responses=ressource_absente,
            summary='Consulter un étudiant',description='Recherche un étudiant par identifiant. Une ressource absente retourne 404 ; un identifiant invalide retourne 422.')
def lire_etudiant(id: Identifiant, db: Session = Depends(get_db)):
    etudiant = crud.lire(db, id)
    if etudiant is None:
        raise HTTPException(status_code=404,detail='Étudiant introuvable')
    return etudiant

@router.put('/{id}',response_model=schemas.EtudiantEnregistre,responses=ressource_absente,
            summary='Remplacer les informations',description='Remplace tous les champs en conservant l’identifiant. Les champs obligatoires sont requis ; le téléphone omis devient NULL.')
def modifier_etudiant(id: Identifiant, etudiant: schemas.Etudiant, db: Session = Depends(get_db)):
    resultat = crud.modifier(db, id, etudiant)
    if resultat is None:
        raise HTTPException(status_code=404,detail='Étudiant introuvable')
    return resultat

@router.delete('/{id}',status_code=204,responses=ressource_absente,summary='Supprimer un étudiant',
               description='Supprime l’étudiant et retourne 204 sans corps. Si l’étudiant est absent, retourne 404.')
def supprimer_etudiant(id: Identifiant, db: Session = Depends(get_db)):
    if not crud.supprimer(db, id):
        raise HTTPException(status_code=404,detail='Étudiant introuvable')
    return Response(status_code=204)
