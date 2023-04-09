from flask import render_template
from models.user_status import UserStatusModel
#from model.jobs import jobs

def handle_apply(bot, chat_dest, company_code):
    user_status = UserStatusModel.get(chat_dest)
    print('user_status', user_status)
    #job = [job for job in jobs if job.company_code == company_code][0]
    user_status.job_history.append(company_code)
    text = render_template('apply.txt', user_status=user_status)
    bot.send_message(chat_dest, text)
    user_status.save()

