import os
from flask import Flask, request
import telebot
import json
from dotenv import load_dotenv

from handle_start import handle_start
from handle_resume import handle_resume
from handle_jobs import handle_jobs
from models.user_status import UserStatusModel


load_dotenv()

TELEGRAM_API_KEY = os.environ.get("TELEGRAM_API_KEY")
WEBHOOK_HOST = os.environ.get("WEBHOOK_HOST")
WEBHOOK_URL = "https://{}/{}".format(WEBHOOK_HOST, TELEGRAM_API_KEY)


bot = telebot.TeleBot(TELEGRAM_API_KEY, threaded=False)
app = Flask(__name__)


@app.route("/", methods=["GET", "HEAD"])
def index():
    return "OK" if TELEGRAM_API_KEY and WEBHOOK_HOST else "Not OK"


@app.route("/{}".format(TELEGRAM_API_KEY), methods=["POST"])
def webhook():
    try:
        if request.headers.get("content-type") == "application/json":
            json_string = request.get_data().decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ""
        else:
            return "OK"
    except Exception as e:
        print(e)
        return "OK"


@bot.message_handler(commands=['start'])
def set_prompt(message):
    chat_dest = message.chat.id
    handle_start(bot, chat_dest)


@bot.message_handler(commands=['resume'])
def set_prompt(message):
    chat_dest = message.chat.id
    handle_resume(bot, chat_dest)


@bot.message_handler(commands=['jobs'])
def set_prompt(message):
    chat_dest = message.chat.id
    handle_jobs(bot, chat_dest)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    chat_dest = message.chat.id
    user_username = message.from_user.username
    bot.send_message(chat_dest, f"Hello, {user_username}!")
    return "", 200


if TELEGRAM_API_KEY and WEBHOOK_HOST:
    webhook_info = bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        # Set webhook
        bot.set_webhook(url=WEBHOOK_URL)
    UserStatusModel.create_table(read_capacity_units=1, write_capacity_units=1)
