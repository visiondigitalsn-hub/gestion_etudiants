"""Validation finale sur PostgreSQL réel ; nettoie seulement ses propres fixtures."""
from uuid import uuid4
from sqlalchemy import select, func
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import Etudiant
from app.schemas import EtudiantEnregistre

def verifier():
    ids=[]
    donnees={'nom':'Exemple','prenom':'Validation','age':23,'email':f'{uuid4().hex}@example.com'}
    def nombre():
        with SessionLocal() as db:
            return db.scalar(select(func.count()).select_from(Etudiant))
    try:
        with SessionLocal() as db:
            # Signale les données historiques incompatibles au lieu de les modifier.
            for e in db.scalars(select(Etudiant)):
                EtudiantEnregistre.model_validate(e)
        with TestClient(app) as client:
            for prenom in ['Validation','Second']:
                r=client.post('/etudiants',json={**donnees,'prenom':prenom})
                assert r.status_code==201,r.text
                ids.append(r.json()['id'])
            id=ids[0]
            original=client.get(f'/etudiants/{id}').json()
            assert original['nom']=='Exemple'
            assert any(e['id']==id for e in client.get('/etudiants').json())
            for champ,valeur in [('email','invalide'),('age',-1),('age',0),('nom',''),('nom','  '),('prenom','A')]:
                avant=nombre()
                corps={**donnees,champ:valeur}
                for methode,chemin in [('post','/etudiants'),('put',f'/etudiants/{id}')]:
                    r=getattr(client,methode)(chemin,json=corps)
                    assert r.status_code==422,(champ,r.text)
                    assert any(e['loc']==['body',champ] for e in r.json()['detail'])
                assert nombre()==avant
                assert client.get(f'/etudiants/{id}').json()==original
            absent=max(ids)+100000
            for methode in ['get','put','delete']:
                args={'json':donnees} if methode=='put' else {}
                r=getattr(client,methode)(f'/etudiants/{absent}',**args)
                assert r.status_code==404 and r.json()=={'detail':'Étudiant introuvable'}
                for mauvais in ['abc','0','-1']:
                    r=getattr(client,methode)(f'/etudiants/{mauvais}',**args)
                    assert r.status_code==422
                    assert any(e['loc']==['path','id'] for e in r.json()['detail'])
            nouveau={**donnees,'nom':'  Exemple  ','prenom':'  Modifie  ','age':26,'telephone':'000000000'}
            r=client.put(f'/etudiants/{id}',json=nouveau)
            assert r.status_code==200,r.text
            with SessionLocal() as db:
                e=db.get(Etudiant,id)
                assert (e.nom,e.prenom,e.age,e.telephone)==('Exemple','Modifie',26,'000000000')
            assert client.delete(f'/etudiants/{ids[1]}').status_code==204
            assert client.get(f'/etudiants/{ids[1]}').status_code==404
            schema=client.get('/openapi.json').json()
            assert schema['info']['version']=='1.0.0' and schema['info']['description']
            props=schema['components']['schemas']['Etudiant']['properties']
            assert props['email']['format']=='email' and props['age']['exclusiveMinimum']==0
            assert props['nom']['minLength']==props['prenom']['minLength']==2
            for path,methods in [('/etudiants',['get','post']),('/etudiants/{id}',['get','put','delete'])]:
                for m in methods:
                    assert schema['paths'][path][m]['summary'] and schema['paths'][path][m]['description']
            for m in ['get','put','delete']:
                assert '404' in schema['paths']['/etudiants/{id}'][m]['responses']
        print('OK : CRUD, validations POST/PUT sans écriture, 404, identifiants invalides 422 et documentation OpenAPI finale.')
    finally:
        with SessionLocal() as db:
            for id in ids:
                e=db.get(Etudiant,id)
                if e is not None: db.delete(e)
            db.commit()

if __name__=='__main__':
    verifier()
