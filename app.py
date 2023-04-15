import os
from flask import Flask, request
import telebot
import json
from dotenv import load_dotenv

from views.handle_start import handle_start
from views.handle_resume import handle_resume
from views.handle_jobs import handle_jobs
from views.handle_apply import handle_apply

from models.game_state import GameState
from services.callstack import print_exceptions


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
@print_exceptions
def start_handler(message):
    chat_dest = message.chat.id
    handle_start(bot, chat_dest)


@bot.message_handler(regexp='apply_(.*)')
@print_exceptions
def apply_handler(message):
    company_code = message.text.replace('/apply_', '')
    print('company_code', company_code)
    chat_dest = message.chat.id
    handle_apply(bot, chat_dest, company_code)


@bot.message_handler(commands=['resume'])
@print_exceptions
def resume_handler(message):
    chat_dest = message.chat.id
    handle_resume(bot, chat_dest)


@bot.message_handler(commands=['jobs'])
@print_exceptions
def jobs_handler(message):
    chat_dest = message.chat.id
    handle_jobs(bot, chat_dest)


@bot.message_handler(content_types=["text"])
@print_exceptions
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
    GameState.create_table(read_capacity_units=1, write_capacity_units=1)
