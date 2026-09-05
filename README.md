# 🗑️ Telegram Bot Promemoria Rifiuti - Bastia Umbra

Bot Telegram per la notifica automatica della raccolta differenziata. Lo script verifica ogni giorno il calendario locale (`calendario.json`) e, se per il giorno successivo è prevista una raccolta, invia un messaggio di promemoria nel gruppo Telegram dedicato.

L'esecuzione è automatizzata e gratuita tramite le **GitHub Actions**.

---

## 📁 Struttura del Progetto

```text
.
├── .github/
│   └── workflows/
│       └── rifiuti.yml     # Workflow GitHub Actions per l'esecuzione pianificata
├── calendario.json         # Mappatura date e tipologie di rifiuto (YYYY-MM-DD)
├── main.py                 # Script Python principale per il controllo e l'invio notifiche
├── requirements.txt        # Dipendenze del progetto
└── README.md