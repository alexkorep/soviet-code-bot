from flask import render_template
from models.user_status import UserStatusModel
from models.tools import tools

# Month names in Russian
MONTHS = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
INITIAL_YEAR = 84


def format_date(current_month):
    year = INITIAL_YEAR + current_month // 12
    month = current_month % 12
    return f"{MONTHS[month]} '{year}"


# def get_technologies_str(technologies):
#     """
#         - Язык прогаммирования Звезда - начальный уровень
#         - Инструмент Завод - начальный уровень
#         - База данных Архив - начальный уровень
#     """
#     print('tools', tools)
#     print('technologies', technologies)
#     result = []
#     for technology in technologies:
#         for tool in tools:
#             if tool['Код'] == technology:
#                 result.append(tool['Название'])
#     return '\n'.join(result)


# def build_resume_text(current_month, technologies):
#     # Build the resume text

#     # Current date in format January '99, in Russian
#     current_date_str = format_date(current_month)

#     technologies_str = get_technologies_str(technologies)

#     text = f"""
# Имя: Джонсон, Александ Вильямович
# Контакты: 
# - Телефон: (555) 123 45 67
# - Э-почта: джонсон.александр@центрпочта.ком

# Желаемая позиция: Младший программист

# Опыт работы: отсутствует

# Образование:
# - Чикагский Советский Университет Компьютерных Наук, диплом по направлению "Программное обеспечение", '84 год

# Знания языков и технологий:
# {technologies_str}

# Хобби: 
# - Филателия
# - Киберспорт

# Текущая дата: {current_date_str}
# """
#     return text


def handle_resume(bot, chat_dest):
    try:
        user_status = UserStatusModel.get(chat_dest)
    except UserStatusModel.DoesNotExist:
        user_status = UserStatusModel(chat_dest, current_month=0)
    
    current_date_str = format_date(user_status.current_month)
    resume_text = render_template('resume.txt',
                                  current_date=current_date_str,
                                  technologies=user_status.technologies or [])
    bot.send_message(chat_dest, resume_text)
    user_status.current_month += 1
    # user_status.job_history = []
    # user_status.technologies = []
    user_status.save()
