# Connect to the Telegram account by Access Token on 1403/09/05
# 
# Verbinden Sie sich mit dem Telegram-Konto per Access Token am 1403/09/05

import os, logging, telebot, requests

if (os.name == "nt"):
    _ = os.system("cls")

print("Telegram Bot account controller by Python Starting...\r\n\r\n")
print("To terminate the Telegram Bot controler (Press Ctrl+C): ", end='')

TELEGRAM_TOKEN = "7824110175:AAGmttzZDz60DcFGCaWdsieCs3ymeUhhtLY" # PyTelgrambot bot token
TELEGRAM_TOKEN1 = "7195803806:AAEdFmM-o-SGQiRTdjQTPC9WKAWl1XiSTE8" # Mein_zweiter_Telegram_BOT bot token
TELEGRAM_TOKEN2 = "6784756694:AAE2yrA4lIQNod0vSmWqVdT5UpRNaoAkqs8" # Mein-erster-Telegram-Bot bot token

URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

logging.basicConfig(
    filename="bot_output.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! بات فعال است.")
    logging.info(f"User {message.chat.id} started the bot.")

@bot.message_handler(commands=['help'])
def start(message):
    response = """
    راهنمای بات:
    - /Start : شروع بات
    - /Help : نمایش راهنما
    - /Settings : فعالیت های بات
    
    امیدواریم که کمک‌کننده باشد!
    """
    bot.reply_to(message, response)
    logging.info(f"User {message.chat.id} use /Help command.")

@bot.message_handler(commands=['settings', '/settings'])
def get_log(message):
    try:
        logging.info(f"User {message.chat.id} use /Settings command.")
        
        with open("bot_output.log", "r") as log_file:
            logs = log_file.read()[-4000:]
            if logs:
                bot.reply_to(message, f"Log:\n{logs}")
            else:
                bot.reply_to(message, "Log file is empty.")
    except Exception as e:
        bot.reply_to(message, f"Error reading log file: {e}")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    logging.info(f"User {message.chat.id} use {message.text} command.")

@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol = message.text.upper()
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    if (response.status_code == 400):
        bot.reply_to(message, "Your price is not True.")
    
    if (response.status_code == 200):
        data = response.json()
        print(type(data))
    logging.info(f"User {message.chat.id} message {message.text} price.")

try:
    bot.infinity_polling()
except Exception as e:
    print(f"OP Error: {e}")

print("\r\nTelegram Bot account controller by Python Terminated.")
