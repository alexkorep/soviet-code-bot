from flask import render_template
from models.user_status import UserStatusModel
from models.model_utils import get_experience

# Month names in Russian
MONTHS = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
INITIAL_YEAR = 84


def format_date(current_month):
    year = INITIAL_YEAR + current_month // 12
    month = current_month % 12
    return f"{MONTHS[month]} '{year}"


def handle_resume(bot, chat_dest):
    try:
        user_status = UserStatusModel.get(chat_dest)
    except UserStatusModel.DoesNotExist:
        user_status = UserStatusModel(chat_dest, current_month=0)

    current_date_str = format_date(user_status.current_month)
    experiences = get_experience(user_status)
    resume_text = render_template('resume.txt',
                                  current_date=current_date_str,
                                  technologies=user_status.technologies or [],
                                  experiences=experiences)
    bot.send_message(chat_dest, resume_text)

    user_status.current_month += 1
    user_status.save()

