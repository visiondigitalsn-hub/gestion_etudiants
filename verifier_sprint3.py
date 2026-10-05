"""Vérifier tout le cycle CRUD et l'absence de mutation en cas d'erreur."""
import data
from fastapi.testclient import TestClient
from main import app


def verifier():
    sauvegarde, compteur = data.etudiants[:], data.prochain_id
    data.etudiants.clear()
    data.prochain_id = 1
    a = {"nom": "Exemple", "prenom": "Alice", "age": 23, "email": "alice@example.com"}
    b = {"nom": "Exemple", "prenom": "Boris", "age": 22, "email": "boris@example.com"}
    try:
        with TestClient(app) as c:
            assert c.get("/").status_code == 200
            assert c.get("/etudiants").json() == []
            r = c.post("/etudiants", json=a)
            assert r.status_code == 201
            premier = r.json()
            assert premier == {**a, "telephone": None, "id": 1}
            second = c.post("/etudiants", json=b).json()
            assert second["id"] == 2
            assert c.get("/etudiants").json() == [premier, second]
            assert c.get("/etudiants/1").json() == premier
            modification = {**a, "nom": "Modifie", "prenom": "Aline", "age": 24, "email": "aline@example.com"}
            r = c.put("/etudiants/1", json=modification)
            assert r.status_code == 200 and r.json() == {**modification, "telephone": None, "id": 1}
            assert c.get("/etudiants/1").json() == r.json()
            avant = c.get("/etudiants").json()
            for methode, kwargs in [("get", {}), ("put", {"json": a}), ("delete", {})]:
                r = getattr(c, methode)("/etudiants/100", **kwargs)
                assert r.status_code == 404 and r.json()["detail"] == "Étudiant introuvable"
                assert c.get("/etudiants").json() == avant
            for methode, chemin, kwargs in [("post", "/etudiants", {"json": {**a, "age": "texte"}}), ("put", "/etudiants/1", {"json": {**a, "age": "texte"}}), ("get", "/etudiants/abc", {})]:
                assert getattr(c, methode)(chemin, **kwargs).status_code == 422
                assert c.get("/etudiants").json() == avant
            r = c.delete("/etudiants/1")
            assert r.status_code == 204 and r.content == b""
            assert c.get("/etudiants").json() == [second]
            assert c.get("/etudiants/1").status_code == 404
            # L'identifiant supprimé ne doit pas être réutilisé.
            assert c.post("/etudiants", json=a).json()["id"] == 3
            assert c.get("/etudiants/2").json() == second
            schema = c.get("/openapi.json").json()["paths"]
            assert {"get", "post"} <= set(schema["/etudiants"])
            assert {"get", "put", "delete"} <= set(schema["/etudiants/{id}"])
        print("OK : CRUD complet, identifiants stables, 404, 422, suppression 204 et absence de mutations sur erreur.")
    finally:
        data.etudiants[:] = sauvegarde
        data.prochain_id = compteur


if __name__ == "__main__":
    verifier()
