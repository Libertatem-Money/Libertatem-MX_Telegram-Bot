import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Token des Bots
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Token aus den GitHub-Secrets abrufen
CHAT_ID = '-1002399056553'  # Deine Kanal-ID hier

bot = Bot(token=TOKEN)

def send_daily_message():
    """Send a daily message to the chat."""
    message = "Good morning! Check out this page to collect free cryptos: https://libertatem-money.github.io/Free-Cryptos/#"
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_daily_message()  # Dies wird für Tests ausgeführt, wenn das Skript lokal ausgeführt wird
