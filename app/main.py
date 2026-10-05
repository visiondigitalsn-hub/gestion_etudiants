"""Assemblage de l'application et conservation des routes du sprint 1."""
from fastapi import FastAPI
from .routers.etudiants import router

app = FastAPI(title='Gestion des étudiants - Sprint 7')
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
