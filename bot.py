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

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    update.message.reply_text("Willkommen zum Crypto-Bot! Starte hier: https://libertatem-money.github.io/Free-Cryptos/#")

if __name__ == "__main__":
    # Initialisiere den Updater mit dem Bot-Token
    updater = Updater(token=TOKEN, use_context=True)

    # Command handlers hinzufügen
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Zum Testen der täglichen Nachricht
    send_daily_message()

    # Polling starten, damit der Bot auf Nachrichten und Befehle reagiert
    updater.start_polling()
    print("Bot is polling for updates...")

    # Der Bot bleibt aktiv und wartet auf Nachrichten
    updater.idle()
