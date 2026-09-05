import json
import os
import requests
from datetime import datetime, timedelta

# GitHub Actions inietterà queste variabili per sicurezza
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def main():
    # Calcola la data di domani nel formato "YYYY-MM-DD"
    domani = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    # Legge il nostro database locale
    with open("calendario.json", "r", encoding="utf-8") as f:
        calendario = json.load(f)
        
    # Se per domani c'è un ritiro programmato, manda il messaggio
    if domani in calendario:
        rifiuto = calendario[domani]
        testo = f"♻️ *Promemoria Rifiuti*\n\nDomani tocca a: **{rifiuto}**.\nRicordati di mettere fuori il bidone stasera!👋🏻"
        
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": testo, "parse_mode": "Markdown"}
        )

if __name__ == "__main__":
    main()