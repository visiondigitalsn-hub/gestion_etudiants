"""Tests réels PostgreSQL : CRUD, validation et persistance hors session."""
from uuid import uuid4
from fastapi.testclient import TestClient
from sqlalchemy import inspect, select, text
from database import Base, engine, SessionLocal
from models import Etudiant
from main import app

def verifier():
    Base.metadata.create_all(engine)
    assert engine.dialect.name == "postgresql"
    assert set(c["name"] for c in inspect(engine).get_columns("etudiants")) == {
        "id", "nom", "prenom", "age", "email", "telephone"
    }
    donnees = {"nom": "Test", "prenom": "Persistence", "age": 23,
               "email": f"{uuid4().hex}@example.com"}
    id = None
    try:
        with TestClient(app) as client:
            r = client.post("/etudiants", json=donnees)
            assert r.status_code == 201, r.text
            id = r.json()["id"]
            # Une nouvelle session indépendante relit le commit de l'API.
            with SessionLocal() as db:
                assert db.get(Etudiant, id).email == donnees["email"]
            assert client.get(f"/etudiants/{id}").json()["prenom"] == "Persistence"
            assert any(e["id"] == id for e in client.get("/etudiants").json())
            assert client.post("/etudiants", json={**donnees, "age": "invalide"}).status_code == 422
            nouveau = {**donnees, "age": 25, "telephone": "000000000"}
            assert client.put(f"/etudiants/{id}", json=nouveau).status_code == 200
            with SessionLocal() as db:
                assert db.get(Etudiant, id).age == 25
            assert client.delete(f"/etudiants/{id}").status_code == 204
            for methode in ["get", "put", "delete"]:
                arguments = {"json": donnees} if methode == "put" else {}
                assert getattr(client, methode)(f"/etudiants/{id}", **arguments).status_code == 404
        # add/flush ne remplacent pas commit : fermeture => rollback.
        with SessionLocal() as db:
            temporaire = Etudiant(**donnees)
            db.add(temporaire)
            db.flush()
            id_sans_commit = temporaire.id
        with SessionLocal() as db:
            assert db.get(Etudiant, id_sans_commit) is None
        print("OK : PostgreSQL réel, table, CRUD, 422, 404, persistance et rollback sans commit.")
    finally:
        if id is not None:
            with SessionLocal() as db:
                restant = db.get(Etudiant, id)
                if restant is not None:
                    db.delete(restant)
                    db.commit()

if __name__ == "__main__":
    verifier()
