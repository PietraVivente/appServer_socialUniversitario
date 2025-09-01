La cartella contiene il codice sorgente per il server dell'app

Il codice è stato creato seguendo la struttura del micro-framework : FLASK
La creazione e dichiarazione dei db è affidata a : Flask-SQLAlchemy
La gestione dei db a : Flask-Migrate

Dichiarazione e documentazione delle API : Flask-Smorest
Validazione degli input : Marshmallow

Le variabili di ambiente sono contenute nel file '.env' non committato sul github mentre le diverse configurazioni sono gestite nel file config.py

La visione del db richiede l'estensione di vsCode 'SQLite Viewer'

Per testare il codice in localhost, scaricare le dipendenze dal file '/app/requirements.txt' con il comando 'pip install -r requirements.txt' e lanciare il comando 'python app/debug_run.py'