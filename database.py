import sqlite3

conn = sqlite3.connect('C:/Users/Андрей/Desktop/python/bot_telegram/SQL_bot.db', check_same_thread=False)
cursor = conn.cursor()


# while True:
com = input('Что делаем? ')
if com == 'INSERT':
    cursor.execute('INSERT INTO personal (user_id, command, city, hotel) VALUES (1, 2, 3, 4)',)
elif com == 'UPDATE':
    num = int(input('Число: '))
    cursor.execute(f'UPDATE personal SET city = {num} WHERE user_id = 1')
elif com == 'DROP':
    cursor.execute('DROP TABLE')

conn.commit()
