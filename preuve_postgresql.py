"""Export local d'une lecture SQL réelle pour les preuves du rapport."""
from html import escape
from pathlib import Path
from sqlalchemy import text
from database import engine

def tableau(titres, lignes):
    return '<table><thead><tr>'+''.join('<th>'+escape(str(v))+'</th>' for v in titres)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+escape(str(v))+'</td>' for v in ligne)+'</tr>' for ligne in lignes)+'</tbody></table>'

if __name__ == '__main__':
    with engine.connect() as db:
        connexion = db.execute(text('SELECT current_database(), current_user, inet_server_port(), version()')).one()
        colonnes = db.execute(text("SELECT table_name, column_name, data_type, is_nullable FROM information_schema.columns WHERE table_schema='public' AND table_name IN ('etudiants','etudiants_manuels') ORDER BY table_name, ordinal_position")).all()
        etudiants = db.execute(text('SELECT id, nom, prenom, age, email FROM etudiants ORDER BY id')).all()
        roles = db.execute(text('SELECT rolname FROM pg_roles WHERE rolcanlogin ORDER BY rolname')).all()
        bases = db.execute(text('SELECT datname FROM pg_database ORDER BY datname')).all()
    page = '''<!doctype html><meta charset="utf-8"><title>Vérification PostgreSQL — Sprints 4 et 5</title><style>body{font:18px Arial;margin:35px;color:#172c29;max-width:1150px}h1{font-size:29px}h2{font-size:22px}table{border-collapse:collapse;width:100%;margin:12px 0 25px}th,td{padding:9px;border:1px solid #ccd7d2;text-align:left}th{background:#eef4f1}code{font-size:16px}p{line-height:1.4}</style><h1>PostgreSQL : connexion et données enregistrées</h1>'''
    page += '<p>Lecture réelle avec SQLAlchemy, exportée pour le rapport. Données de démonstration fictives.</p>'
    page += tableau(['Base','Utilisateur','Port'],[connexion[:3]])
    page += '<h2>Étudiants présents dans PostgreSQL</h2><code>SELECT id, nom, prenom, age, email FROM etudiants ORDER BY id;</code>'
    page += tableau(['id','nom','prenom','âge','email'],etudiants)
    page += '<h2>Structure des tables : manuelle et ORM</h2>'+tableau(['Table','Colonne','Type','NULL autorisé'],colonnes)
    page += '<p>Bases : '+escape(', '.join(r[0] for r in bases))+'<br>Rôles de connexion : '+escape(', '.join(r[0] for r in roles))+'<br>Schéma : public.</p><p>'+escape(connexion[3])+'</p>'
    sortie = Path('../output/preuves/postgresql.html')
    sortie.parent.mkdir(parents=True,exist_ok=True)
    sortie.write_text(page,encoding='utf-8')
    print('Preuve SQL exportée :',sortie)
