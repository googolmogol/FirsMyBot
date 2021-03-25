from datetime import datetime
from threading import Thread

import telebot
import schedule
import time

bot = telebot.TeleBot("801359509:AAHjuBl_1xRdDHHTTacpT3Q1TSiXl_qQiCw")

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Привет', 'Пока')
chat_id = ''
chat_id_list = []
user_var = None
week = False
lock_is = True


@bot.message_handler(commands=['start'])
def send_welcome(message1):
    global chat_id, user_var
    chat_id = message1.chat.id
    print(message1.from_user.first_name)
    if chat_id not in chat_id_list:
        chat_id_list.append(chat_id)

    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="Хаб с материалами", url="https://drive.google.com/drive"
                                                                              "/folders"
                                                                              "/16c2M4x1JY1PdvjVngOBrNG29B5Pn5p0o"
                                                                              "?usp=sharing")

    markup.add(button)
    bot.send_message(message1.chat.id,
                     '<strong>Здарова студентам!</strong>\N{Victory Hand}\nЯ бот, который будет уведомлять о парах'
                     '\N{Robot Face}\n ', parse_mode="HTML", reply_markup=markup)


def job(day, time_lesson):
    global lock_is
    lesson = ''
    if datetime.weekday == 0:
        lock_is = True

    if week:
        if day == 'monday':
            lesson = "<strong>Пара: </strong>Машинне навчання.\n\n<strong>Викладач: </strong>професор Романюк " \
                     "В.В.\n\nБажаю хорших знань!"
        elif day == 'tuesday' and time_lesson == "11:30":
            lesson = "<strong>Пара: </strong>Інженерія програмних систем для паралельних та розподілених " \
                     "систем.\n\n<strong>Викладач: </strong>доцент Вороной С.М.\n\nБажаю хорших знань! "
        elif day == 'tuesday' and time_lesson == "15:40":
            lesson = "<strong>Пара: </strong>Сучасні технології баз даних.\n\n<strong>Викладач: </strong>Гладких " \
                     "В.М.\n\nБажаю хорших знань! "
        elif day == 'wednesday':
            lesson = "<strong>Пара: </strong>Алгоритми та технології побудови рекомендаційних " \
                     "систем.\n\n<strong>Викладач: </strong>старший викладач Височіненко М.С.\n\nБажаю хорших знань!"
        elif day == 'thursday':
            lesson = "<strong>Вітаю, сьогодні у Вас вікно!!!</strong>"
        elif day == 'friday':
            lesson = "<strong>Пара: </strong>Методологія підтримки прийняття рішень в інженерії програмного " \
                     "забезпечення.\n\n<strong>Викладач: </strong>професор Романюк " \
                     "В.В.\n\nБажаю хорших знань!"
    else:
        if day == 'monday':
            lesson = "<strong>Вітаю, сьогодні у Вас вікно!!!</strong>"
        elif day == 'tuesday' and time_lesson == "13:15":
            lesson = "<strong>Пара: </strong>Інженерія програмних систем для паралельних та розподілених " \
                     "систем.\n\n<strong>Викладач: </strong>доцент Вороной С.М.\n\nБажаю хорших знань! "
        elif day == 'tuesday' and time_lesson == "15:40":
            lesson = "<strong>Пара: </strong>Методологія підтримки прийняття рішень в інженерії програмного " \
                     "забезпечення.\n\n<strong>Викладач: </strong>професор Романюк " \
                     "В.В.\n\nБажаю хорших знань!"
        elif day == 'wednesday' and time_lesson == "14:10":
            lesson = "<strong>Пара: </strong>Сучасні технології баз даних.\n\n<strong>Викладач: </strong>Гладких " \
                     "В.М.\n\nБажаю хорших знань! "
        elif day == 'wednesday' and time_lesson == "17:10":
            lesson = "<strong>Пара: </strong>Алгоритми та технології побудови рекомендаційних " \
                     "систем.\n\n<strong>Викладач: </strong>старший викладач Височіненко М.С.\n\nБажаю хорших знань! "
        elif day == 'thursday':
            lesson = "<strong>Пара: </strong>Моделювання та верифікація програмного забезпечення.\n\n<strong>" \
                     "Викладач: </strong>кандитат технічних наук, доцент Іларіонов О.Є.; доктор технічних наук " \
                     "професор Комарова Л.О.\n\nБажаю хорших знань!"
        elif day == 'friday':
            lesson = "<strong>Пара: </strong>Машинне навчання.\n\n<strong>Викладач: </strong>професор Романюк " \
                     "В.В.\n\nБажаю хорших знань!"

    print("Chat_id_list:", chat_id_list)

    for k in chat_id_list:
        msg = "Вітаю, за 10 хвилин розпочннеться пара! Підготуйтеся, згодом надішлю посилання."
        try:
            bot.send_message(k, msg)
        except:
            print("The user has stopped the bot")
            chat_id_list.remove(k)

    print(chat_id)
    button_generation(lesson, "https://github.com/illuhakupchenko/Pybot/blob/master/bot.py")


def button_generation(text, url):
    markup = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text="Посилання на пару", url=url)

    markup.add(button)
    for member in chat_id_list:
        try:
            bot.send_message(member, text, parse_mode="HTML", reply_markup=markup)
        except:
            print("The user has stopped the bot")
            chat_id_list.remove(member)


#  https://qna.habr.com/q/394496
def checker_schedule():
    global week, lock_is
    if datetime.weekday == 6 and lock_is:
        if not week:
            week = True
            lock_is = False
        else:
            week = False
            lock_is = False

    if week:
        schedule.every().monday.at("18:40").do(job, "monday", "18:40")
        schedule.every().tuesday.at("11:30").do(job, "tuesday", "11:30")
        schedule.every().tuesday.at("15:40").do(job, "tuesday", "15:40")
        schedule.every().wednesday.at("14:10").do(job, "wednesday", "14:10")
        schedule.every().thursday.at("09:00").do(job, "thursday", "09:00")
        schedule.every().friday.at("15:40").do(job, "friday", "15:40")
    else:
        schedule.every().monday.at("09:00").do(job, "monday", "09:00")
        schedule.every().tuesday.at("13:15").do(job, "tuesday", "13:15")
        schedule.every().tuesday.at("14:10").do(job, "tuesday", "14:10")
        schedule.every().wednesday.at("14:10").do(job, "wednesday", "14:10")
        schedule.every().wednesday.at("17:10").do(job, "wednesday", "17:10")
        schedule.every().thursday.at("14:10").do(job, "thursday", "14:10")
        schedule.every().friday.at("15:40").do(job, "friday", "15:40")

    while True:
        if chat_id != '':
            schedule.run_pending()
            time.sleep(1)


# https://bit.ly/3dnzZbh
#  обязательно нужен новый поток, чтобы не было споров цикла бота и schedule

Thread(target=checker_schedule).start()


def start_bot():
    bot.polling(none_stop=True)


Thread(target=start_bot).start()
