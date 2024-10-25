import os
from telegram import Bot

# Token des Bots - stelle sicher, dass dieser in GitHub als Secret gespeichert ist
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Token aus den GitHub-Secrets abrufen
CHAT_ID = '-1002399056553'  # Deine Kanal-ID hier

bot = Bot(token=TOKEN)

def send_message():
    message = "Hello and welcome at Libertatem-MX, do you want to start earn money online?"  # Beispielnachricht
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_message()
