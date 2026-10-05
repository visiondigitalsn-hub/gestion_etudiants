"""Insertion et lecture ORM demandées : add, commit, refresh, close."""
from sqlalchemy import select
from database import SessionLocal
from models import Etudiant

def demonstration():
    db = SessionLocal()
    try:
        for nom, prenom, age, email in [
            ("Exemple", "Alice", 22, "alice@example.com"),
            ("Exemple", "Boris", 24, "boris@example.com"),
        ]:
            if db.scalar(select(Etudiant).where(Etudiant.email == email)) is None:
                etudiant = Etudiant(nom=nom, prenom=prenom, age=age, email=email)
                db.add(etudiant)
                db.commit()
                db.refresh(etudiant)
                print("Insertion confirmée, identifiant :", etudiant.id)
        for etudiant in db.scalars(select(Etudiant).order_by(Etudiant.id)):
            print(etudiant.id, etudiant.nom, etudiant.prenom, etudiant.age)
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    demonstration()
