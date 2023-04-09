import random
from flask import render_template
from models.jobs import jobs
from models.user_status import UserStatusModel
from models.model_utils import get_job_score_for_user

def make_stars(count):
    # Unicode star
    return "★" * int(count)

def handle_jobs(bot, chat_dest):
    user_status = UserStatusModel.get(chat_dest)

    # Get a random element from jobs
    job = random.choice(jobs)
    print('job', job)
    stars = make_stars(job.rating)
    user_score = get_job_score_for_user(job, user_status)
    text = render_template('job.txt', job=job, stars=stars, user_score=user_score)
    bot.send_message(chat_dest, text)