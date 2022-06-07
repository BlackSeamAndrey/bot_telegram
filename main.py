import telebot
from telebot import types
import requests
import sqlite3

# import Body


url = "https://hotels4.p.rapidapi.com/locations/v2/search"
querystring = {"query": "new york", "locale": "en_US", "currency": "USD"}
headers = {
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com",
    "X-RapidAPI-Key": "80e04d9c9cmsh263e9134b1a1a78p1b6168jsn7270db6f4459"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)


bot = telebot.TeleBot('5075533051:AAE0rIxhHTYolZt4VcdcISfJbTO3x2RQUkE')


conn = sqlite3.connect('C:/Users/Андрей/Desktop/python/bot_telegram/SQL_bot.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, command: str, city: str, hotel: str):
    cursor.execute('INSERT INTO personal (user_id, command, city, hotel) VALUES (?, ?, ?, ?)',
                   (user_id, command, city, hotel))
    conn.commit()


class body:
    def city(self, message):
        global comma
        bot.send_message(message.chat.id, 'Введите количество отелей, которые необходимо вывести '
                                          'в результате (не больше 5)')
        bot.register_next_step_handler(message, Body.show_hotels)

        cursor.execute(f'UPDATE personal SET command = "{comma}" WHERE user_id = 1')
        conn.commit()

    def show_hotels(self, message):
        try:
            hotels = int(message.text)
            if hotels > 5:
                bot.send_message(message.chat.id, 'Введите цифру меньше (не больше 5)')
                bot.register_next_step_handler(message, Body.show_hotels)
            elif hotels < 1:
                bot.send_message(message.chat.id, 'Введите цифру больше (не больше 5)')
                bot.register_next_step_handler(message, Body.show_hotels)
            else:
                # bot.send_message(message.chat.id, 'Держи')
                bot.send_message(message.from_user.id, 'Выводить фотографий?')
                bot.register_next_step_handler(message, Body.photo)
        except Exception:
            bot.send_message(message.from_user.id, 'Натуральными цифрами')
            bot.register_next_step_handler(message, Body.show_hotels)

    def photo(self, message):
        if str.lower(message.text) == 'да':
            bot.send_message(message.chat.id,
                             'Введите количество фотографий (не больше 3)')
            bot.register_next_step_handler(message, Body.hotels_photo)
        # else:

    def hotels_photo(self, message):
        try:
            hotel_photo = int(message.text)
            if hotel_photo > 3:
                bot.send_message(message.chat.id, 'Введите цифру меньше (не больше 3)')
                bot.register_next_step_handler(message, Body.hotels_photo)
            elif hotel_photo < 1:
                bot.send_message(message.chat.id, 'Введите цифру больше (не больше 3)')
                bot.register_next_step_handler(message, Body.hotels_photo)
            else:
                bot.send_message(message.chat.id, '"Фотографии"')
        except Exception:
            bot.send_message(message.from_user.id, 'Натуральными цифрами, пожалуйста')
            bot.register_next_step_handler(message, Body.hotels_photo)


Body = body()


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать')
    bot.send_message(message.chat.id, 'Напиши /help чтобы узнать команды')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '  Команды\n '
                                      '/help — помощь по командам бота\n'
                                      '/lowprice — вывод самых дешёвых отелей в городе\n'
                                      '/highprice — вывод самых дорогих отелей в городе\n'
                                      '/bestdeal — вывод отелей, наиболее подходящих по цене и расположению от центра\n'
                                      '/history — вывод истории поиска отелей')


@bot.message_handler(commands=['lowprice'])
def low_price(message):
    bot.send_message(message.from_user.id, 'Введите город, где будет проводиться поиск')
    comma = message.text

    # cursor.execute(f'UPDATE personal SET command = "{comma}" WHERE user_id = 1')
    # conn.commit()

    bot.register_next_step_handler(message, Body.city)


@bot.message_handler(commands=['highprice'])
def low_price(message):
    bot.send_message(message.from_user.id, 'Введите город, где будет проводиться поиск')
    bot.register_next_step_handler(message, Body.city)


@bot.message_handler(commands=['bestdeal'])
def low_price(message):
    bot.send_message(message.from_user.id, 'Введите город, где будет проводиться поиск')
    # bot.register_next_step_handler(message, Body.city)


@bot.message_handler(commands=['history'])
def low_price(message):
    pass


bot.polling(none_stop=True)
