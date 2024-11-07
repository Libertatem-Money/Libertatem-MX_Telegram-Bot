import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Token des Bots
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Token aus den GitHub-Secrets abrufen
CHAT_ID = '-1002399056553'  # Deine Kanal-ID hier

bot = Bot(token=TOKEN)

# Funktion für die tägliche Nachricht im Kanal
def send_daily_message():
    """Send a daily message to the chat."""
    message = "Good morning! Check out this page to collect free cryptos: https://libertatem-money.github.io/Free-Cryptos/#"
    bot.send_message(chat_id=CHAT_ID, text=message)

# Funktion für den /start Befehl
def start(update: Update, context: CallbackContext) -> None:
    welcome_message = "Willkommen! Ich bin dein persönlicher Bot. Mit /help erhältst du weitere Informationen über meine Funktionen."
    update.message.reply_text(welcome_message)

# Hauptfunktion des Bots
def main():
    # Bot-Updater und Dispatcher einrichten
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # /start-Befehl hinzufügen
    dispatcher.add_handler(CommandHandler("start", start))

    # Bot starten
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    send_daily_message()  # Tägliche Nachricht senden
    main()  # Hauptfunktion starten, damit der Bot auf /start reagieren kann
