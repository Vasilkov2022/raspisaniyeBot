import telebot
import time
from telebot import types
from tinydb import TinyDB, Query
db = TinyDB('db.json')

token = '5482406574:AAEEGCpP6aEyWf79YnGRO7ohUvW8lG6DM0M'
bot = telebot.TeleBot(token, parse_mode=None)
for i in db.all():
    k = list(i.keys())[0]
    bot.send_message(i[k], k)
print(db.all())

@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    # table = db.table('User')
    db.insert({message.chat.username: message.chat.id})




@bot.message_handler(commands=['timer'])
def timer(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('3')
    itembtn2 = types.KeyboardButton('5')
    itembtn3 = types.KeyboardButton('10')
    itembtn4 = types.KeyboardButton('other')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Choose timer duration:", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def btn_handler(message):
    print(message)
    if message.text == ['3', '5', '10']:
        time.sleep(float(message.text))
    if message.text == 'other':
        bot.send_message(message.chat.id, "Set a timer")
    if isinstance(message.text, float):
        print('done')
        time.sleep(float(message.text))



bot.infinity_polling()