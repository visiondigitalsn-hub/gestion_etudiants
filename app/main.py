"""Assemblage de l'application et conservation des routes du sprint 1."""
from fastapi import FastAPI
from .routers.etudiants import router

app = FastAPI(
    title='Gestion des étudiants - API finale',
    description="API pédagogique pour gérer les étudiants avec PostgreSQL. "
                "Les noms et prénoms comportent au moins deux caractères, l'âge est "
                "strictement positif et l'e-mail est validé. Les écritures sont persistantes. "
                "PUT remplace toutes les informations ; DELETE retourne 204 sans corps.",
    version='1.0.0',
    openapi_tags=[{'name':'Étudiants','description':'Création, consultation, modification et suppression des étudiants.'}],
)
app.include_router(router)

@app.get('/')
def accueil():
    return {'message':'Bienvenue dans mon API'}

@app.get('/bonjour')
def bonjour():
    return {'message':'Bonjour à tous'}

@app.get('/bonjour/{nom}')
def bonjour_personnalise(nom: str):
    return {'message':f'Bonjour {nom}'}

@app.get('/addition/{a}/{b}')
def addition(a: int,b: int):
    return {'resultat':a+b}
