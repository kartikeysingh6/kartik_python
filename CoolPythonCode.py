import telegram
import time
import random
from telegram import Bot

#Credentials
API_TOKEN = '6449063852:AAHxPuqY7_Ij9Zd_hRxgnuRz826Wtngb04U'
chat_id = '2054523449'

# Initialize the bot
bot = Bot(token=API_TOKEN)

def send_message(chat_id, message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully.")
    except telegram.error.TelegramError as e:
        print(f"An error occurred while sending the message: {e}")

while True:
    msg="Hello bhai from "+str(random.randint(0,100))
    send_message(chat_id, msg)
    time.sleep(5)
