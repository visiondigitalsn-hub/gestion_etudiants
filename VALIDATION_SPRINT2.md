# Sprint 2 - Vérifications exécutées

Les scripts verifier.py et verifier_sprint2.py ont été exécutés : toutes les assertions ont réussi.

| Cas | Résultat observé |
| --- | --- |
| Fall, Mamadou, 23, email fourni | HTTP 200, données retournées, téléphone null |
| Âge « vingt trois » | HTTP 422, erreur sur body.age, fonction non exécutée |
| Email absent | HTTP 422, erreur sur body.email, fonction non exécutée |
| Ali avec téléphone | HTTP 200, téléphone conservé |
| Ali sans téléphone | HTTP 200, téléphone null |
| Téléphone explicitement null | HTTP 200 |
| Âge chaîne numérique « 23 » | HTTP 200, conversion en entier 23 |
| Email sans arobase | HTTP 200, car email est str selon l’énoncé |

OpenAPI décrit les quatre champs obligatoires, le téléphone non obligatoire acceptant null et la nouvelle route POST. Les routes GET du sprint 1 fonctionnent toujours. Swagger répond HTTP 200.

Les tests automatiques ne remplacent pas les essais manuels via Swagger. Les captures sont à prendre par l’étudiant.

## Rejouer
```powershell
.\env\Scripts\python.exe -m pip install -r requirements-test.txt
.\env\Scripts\python.exe verifier.py
.\env\Scripts\python.exe verifier_sprint2.py
```
