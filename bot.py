from telegram import Bot

TOKEN = 8090320858:AAHVvx-MenwiG9s0XLeeBLIMfKLadgbs05A  # Ersetze durch dein Token
CHAT_ID = libertatemmx_bot  # Ersetze durch deine Chat-ID oder Kanal-ID

bot = Bot(token=TOKEN)

def send_message():
    message = "Dies ist ein geplanter Beitrag!"  # Deine Nachricht hier
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_message()
