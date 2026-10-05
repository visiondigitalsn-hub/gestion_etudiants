"""Opérations persistantes ; cette couche ne connaît pas les réponses HTTP."""
from sqlalchemy import select
from sqlalchemy.orm import Session
from . import models, schemas

def lister(db: Session):
    return db.scalars(select(models.Etudiant).order_by(models.Etudiant.id)).all()

def lire(db: Session, id: int):
    return db.get(models.Etudiant, id)

def creer(db: Session, donnees: schemas.Etudiant):
    etudiant = models.Etudiant(**donnees.model_dump())
    try:
        db.add(etudiant)
        db.commit()
        db.refresh(etudiant)
        return etudiant
    except Exception:
        db.rollback()
        raise

def modifier(db: Session, id: int, donnees: schemas.Etudiant):
    etudiant = lire(db, id)
    if etudiant is None:
        return None
    try:
        for champ, valeur in donnees.model_dump().items():
            setattr(etudiant, champ, valeur)
        db.commit()
        db.refresh(etudiant)
        return etudiant
    except Exception:
        db.rollback()
        raise

def supprimer(db: Session, id: int):
    etudiant = lire(db, id)
    if etudiant is None:
        return False
    try:
        db.delete(etudiant)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise
