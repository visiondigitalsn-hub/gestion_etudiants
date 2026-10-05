# Gestion des étudiants — Sprint 2

Code FastAPI et scripts de vérification du sprint 2.

## Lancement

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger : http://127.0.0.1:8000/docs

## Vérification

```powershell
pip install -r requirements-test.txt
python verifier.py
python verifier_sprint2.py
```
