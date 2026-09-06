# 🗑️ Telegram Bot Promemoria Rifiuti - Bastia Umbra

Bot Telegram per la notifica automatica della raccolta differenziata nel comune di Bastia Umbra. Lo script verifica ogni giorno il file locale (`calendario.json`) e, se per il giorno successivo è prevista una raccolta, invia un messaggio di promemoria nel gruppo Telegram dedicato.

L'esecuzione è interamente automatizzata e gratuita tramite **GitHub Actions**.

---

## 📁 Struttura del Progetto

```text
.
├── .github/
│   └── workflows/
│       └── rifiuti.yml     # Workflow GitHub Actions per l'esecuzione pianificata
├── calendario.json         # Mappatura date e tipologie di rifiuto
├── main.py                 # Script Python per il controllo e l'invio notifiche
├── requirements.txt        # Dipendenze del progetto
└── README.md
```

---

## 📅 Origine e Struttura di `calendario.json`

I dati sui ritiri si basano sui calendari ufficiali per il comune di Bastia Umbra forniti da Gesenu, reperibili sul sito ufficiale [Gesenu - Calendari Bastia Umbra](https://www.gesenu.it/pagine/calendari-raccolta-bastia-umbra).

### Gestione del file JSON
Si preferisce fornire il file `calendario.json` già strutturato e compilato offline/manualmente rispetto all'estrazione dinamica via codice. Nei documenti PDF rilasciati da Gesenu, le tipologie di rifiuto (Carta e Cartone, Plastica e Lattine, Secco Residuo) sono identificate esclusivamente dal colore di sfondo delle celle: il parsing automatico dei colori o il rendering grafico del PDF risultano complessi e soggetti ad errori a seguito di modifiche al layout o aggiornamenti della pagina web.

### Struttura del file
Il file `calendario.json` consiste in una mappa chiave-valore:
* **Chiave**: Data del ritiro nel formato ISO `YYYY-MM-DD`.
* **Valore**: Descrizione del rifiuto da esporre (con eventuale emoji rappresentativa).

```json
{
  "2026-08-20": "Secco Residuo🔘",
  "2026-09-03": "Plastica e Lattine⚪",
  "2026-09-16": "Carta e Cartone🔵",
}
```

---

## ⚙️ Configurazione Secret su GitHub

Per consentire allo script di inviare notifiche al gruppo Telegram senza esporre credenziali nel codice, imposta i seguenti **Repository Secrets** su GitHub:

* **`TELEGRAM_BOT_TOKEN`**: Il token API rilasciato da `@BotFather`.
* **`TELEGRAM_CHAT_ID`**: L'ID numerico della chat o del gruppo Telegram (comprensivo del segno meno per i gruppi, es. `-100XXXXXXXXXX`).

---

## 🚀 Esecuzione in Locale

Per testare lo script sul proprio computer:

1. **Installazione dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Esecuzione con variabili d'ambiente**:
   * **Linux / macOS**:
     ```bash
     export TELEGRAM_BOT_TOKEN="il_tuo_token"
     export TELEGRAM_CHAT_ID="il_tuo_chat_id"
     python main.py
     ```
   * **Windows (PowerShell)**:
     ```powershell
     $env:TELEGRAM_BOT_TOKEN="il_tuo_token"
     $env:TELEGRAM_CHAT_ID="il_tuo_chat_id"
     python main.py
     ```

---

## ⏰ Automazione tramite GitHub Actions

Il workflow `.github/workflows/rifiuti.yml` esegue lo script ogni giorno alle **17:17 UTC** (pari alle 18:17 con ora solare / 19:17 con ora legale in Italia).

### Esecuzione Manuale (Test)
1. Apri la scheda **Actions** del repository su GitHub.
2. Seleziona **Notifica Rifiuti Telegram**.
3. Clicca su **Run workflow** per avviare l'esecuzione immediata.