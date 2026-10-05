"""Tests de validation du sprint 2 et du schéma OpenAPI."""
from fastapi.testclient import TestClient
from main import app
import data


def verifier():
    fall = {"nom": "Fall", "prenom": "Mamadou", "age": 23, "email": "mamadou@gmail.com"}
    ali = {"nom": "Ali", "prenom": "Diop", "age": 22, "email": "ali@gmail.com"}
    route = next(r for r in app.routes if getattr(r, "path", "") == "/etudiants")
    original = route.dependant.call
    appels = []
    anciens_etudiants = data.etudiants[:]
    ancien_id = data.prochain_id

    async def observer(etudiant):
        appels.append(etudiant)
        return await original(etudiant)

    route.dependant.call = observer
    try:
        with TestClient(app) as client:
            for donnees in [fall, {**ali, "telephone": "771234567"}, ali, {**ali, "telephone": None}]:
                avant = len(appels)
                r = client.post("/etudiants", json=donnees)
                assert r.status_code == 201, r.text
                resultat = r.json()
                assert isinstance(resultat.pop("id"), int)
                assert resultat == {**donnees, "telephone": donnees.get("telephone")}
                assert len(appels) == avant + 1
            for donnees, champ, type_erreur in [
                ({**fall, "age": "vingt trois"}, "age", "int_parsing"),
                ({k: v for k, v in fall.items() if k != "email"}, "email", "missing"),
            ]:
                avant = len(appels)
                r = client.post("/etudiants", json=donnees)
                assert r.status_code == 422, r.text
                assert any(e["loc"] == ["body", champ] and e["type"] == type_erreur for e in r.json()["detail"])
                assert len(appels) == avant, "La fonction ne doit pas être exécutée en cas d'erreur"
            # int effectue une conversion : le texte numérique est accepté.
            r = client.post("/etudiants", json={**fall, "age": "23"})
            assert r.status_code == 201 and r.json()["age"] == 23
            # email est une simple chaîne selon l'énoncé, sans contrôle de format.
            assert client.post("/etudiants", json={**fall, "email": "sans-arobase"}).status_code == 201
            schema = client.get("/openapi.json").json()
            modele = schema["components"]["schemas"]["Etudiant"]
            assert set(modele["required"]) == {"nom", "prenom", "age", "email"}
            assert "telephone" not in modele["required"]
            assert {p.get("type") for p in modele["properties"]["telephone"]["anyOf"]} == {"string", "null"}
            assert "post" in schema["paths"]["/etudiants"]
            assert client.get("/docs").status_code == 200
    finally:
        route.dependant.call = original
        data.etudiants[:] = anciens_etudiants
        data.prochain_id = ancien_id
    print("OK : données valides, âge invalide, champ manquant, téléphone optionnel, absence d'exécution sur erreur et OpenAPI.")


if __name__ == "__main__":
    verifier()
