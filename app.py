import os
from flask import Flask, request, render_template
import telebot
from dotenv import load_dotenv


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

def handle_page(page, chat_dest):
    text = render_template(f"{page}.txt")
    bot.send_message(chat_dest, text)

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_dest = message.chat.id
    handle_page('start', chat_dest)

@bot.message_handler(regexp='p(.*)')
def apply_handler(message):
    page = message.text.replace('/', '')
    chat_dest = message.chat.id
    handle_page(page, chat_dest)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    chat_dest = message.chat.id
    handle_page('404', chat_dest)


if TELEGRAM_API_KEY and WEBHOOK_HOST:
    webhook_info = bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        # Set webhook
        bot.set_webhook(url=WEBHOOK_URL)
