import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Liest das Token aus den GitHub-Secrets
CHAT_ID = "-1002399056553"  # Ersetze durch deine Chat-ID

bot = Bot(token=TOKEN)

def send_message():
    message = "Dies ist ein geplanter Beitrag!"  # Deine Nachricht hier
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_message()
