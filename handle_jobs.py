import random
from models.jobs import jobs

def make_stars(count):
    # Unicode star
    return "★" * int(count)

def format_job(job):
    stars = make_stars(job['Рейтинг'])
    return f"""
{job['Название']}{stars}

{job['О компании']}
{job['История компании']}

Адрес: {job['Город']}, {job['Адрес']}

Позиция: {job['Позиция']}
{job['Обязанности']}
    """

def handle_jobs(bot, chat_dest):
    # Get a random element from jobs
    job = random.choice(jobs)
    text = format_job(job)
    bot.send_message(chat_dest, text)