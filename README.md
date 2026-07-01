# Progetto Eventi Cinematografici - Esame di Full-Stack Web Applications

### Autore
* **Nome e Cognome:** Matilde Giuliani
* **Matricola:** 7133890

---

## 1. Descrizione principale
L'applicazione gestisce un sistema di eventi cinematografici. Permette agli utenti di visualizzare i diversi eventi con le rispettive informazioni e prenotare i posti per determinati eventi.

### Funzionalità principali:
* **Utente Anonimo:** Può registrarsi, consultare l'elenco degli eventi disponibili.
* **Utente Attendee:** Può effettuare il login, prenotare un posto per un evento, visualizzare lo storico delle proprie prenotazioni e cancellarle.
* **Utente Organizzatore/Amministratore:** Può gestire gli eventi, creare/modificare gli eventi.

---
## 2. Tipo di progetto e framework
###
* **Tipologia:** Full-Stack Web Application
* **Framework Backend:** Django
* **Frontend:** HTML5, CSS, Bootstrap
---
##  3.Funzionalità implementate per Ruolo

### 3.1 Spettatore (Attendee)
* **Visualizzazione:** Consultazione dell'elenco completo degli eventi in programmazione ordinati per data (`EventListView`).
* **Dettaglio Spettacolo:** Visualizzazione della descrizione, orario e location (`EventDetailView`).
* **Prenotazione Posti:** Possibilità di prenotare o annullare un posto per uno specifico spettacolo (`BookEventView`, `CancelRegistrationView`).
* **Area Personale:** Dashboard del profilo per monitorare le proprie prenotazioni attive (`ProfileView`).

### 3.2 Organizzatore / Gestore (Organizer)
* **Permessi:** Permessi esclusivi di inserimento evento (`EventCreateView`), modifica dettagli (`EventUpdateView`) ed eliminazione dello spettacolo (`EventDeleteView`).
* **Vincolo di Proprietà:** Un organizzatore può modificare o eliminare unicamente gli spettacoli da lui stesso inseriti.
* **Lista degli Spettatori:** Visualizzazione della lista dei partecipanti prenotati per i propri eventi direttamente nella pagina di dettaglio.
---
## 4. Database e Dati Demo (Demo Data)
###
Il progetto include un database relazionale configurato in **SQLite** (file `db.sqlite3`). 

Il database è stato pre-popolato tramite fixture (`initial_data.json`) con dati realistici relativi a eventi e profili utente.
## 5. Credenziali Account di Test
###
Utilizzare le seguenti credenziali:

* **Profilo Spettatore (Attendee):**
  * **Username:** `Matilde`
  * **Password:** `ghzl5viak0!/&`

* **Profilo Amministratore (Organizer):**
  * **Username:** `admin_demo1`
  * **Password:** `admin8120`
  
* **Profilo Organizzatore(Organizer):**
  * **Username:** `Isabella`
  * **Password:** `biqrAb-xuzra4-kukweg`
## 6. Local Setup Instructions
###
## Link del progetto online
Il sito è raggiungibile al seguente indirizzo:(https://progettodjango-production-43ca.up.railway.app)

## Create virtual environment
-su macOS/linux: 
python3 -m venv .venv
source .venv/bin/activate
-su windows: 
python -m venv .venv
.venv\Scripts\activate
## Install Requirements:
pip install -r requirements.txt
## Apply migrations:
python manage.py migrate
## Run server:
python manage.py runserver
```bash
git clone [https://github.com/Matilde1ae/progetto_django.git]

