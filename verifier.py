"""Vérifie les réponses et la documentation du sprint sans lancer de serveur."""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


def verifier():
    cas = [
        ("/", {"message": "Bienvenue dans mon API"}),
        ("/bonjour", {"message": "Bonjour à tous"}),
        ("/bonjour/Ali", {"message": "Bonjour Ali"}),
        ("/bonjour/Fatou", {"message": "Bonjour Fatou"}),
        ("/bonjour/Mamadou", {"message": "Bonjour Mamadou"}),
        ("/addition/10/20", {"resultat": 30}),
        ("/addition/-5/2", {"resultat": -3}),
    ]
    with TestClient(app) as client:
        for chemin, attendu in cas:
            reponse = client.get(chemin)
            assert reponse.status_code == 200, chemin
            assert reponse.json() == attendu, chemin
        erreur = client.get("/addition/abc/10")
        assert erreur.status_code == 422
        assert erreur.json()["detail"][0]["loc"] == ["path", "a"]
        docs = client.get("/docs")
        assert docs.status_code == 200
        assert "swagger-ui" in docs.text
        schema = client.get("/openapi.json")
        assert schema.status_code == 200
        chemins = schema.json()["paths"]
        assert set(chemins) == {"/", "/bonjour", "/bonjour/{nom}", "/addition/{a}/{b}"}
        assert all("get" in operation for operation in chemins.values())
    with TestClient(FastAPI()) as client:
        assert client.get("/").status_code == 404
    print("OK : 7 réponses JSON, erreur 422, Swagger, OpenAPI et 404 initial vérifiés.")


if __name__ == "__main__":
    verifier()
