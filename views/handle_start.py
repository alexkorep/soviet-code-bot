from flask import render_template


def handle_start(bot, chat_dest):
    message = render_template('start.txt')
    bot.send_message(chat_dest, message)
