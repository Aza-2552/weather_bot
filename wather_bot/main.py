from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove
from keyboards import *
import requests

TOKEN = '7318857104:AAEio9fi4EuwLYHVADYJLxcd0bg3b2Z-mM8'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Salom! 👋  Man OB-XAVO 🌤 bot man\n'
                              'Tugmani bosing 👇', reply_markup=generate_button())

@bot.message_handler(regexp='Dunyo ob-xavolari ⛅')
def ask_city(message: Message):
    chart_id = message.chat.id
    msg = bot.send_message(chart_id, 'Shaxar nomini kiriting 🌆: ',
                           reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, answer_to_user)

def answer_to_user(message: Message):
    chart_id = message.chat.id
    text = message.text
    bot.send_message(chart_id, f'Siz kiritgan shaxar: {text}')

    KEY = '6418b539e0697f54de8a3df65ebe9444'
    params = {
        'appid': KEY,
        'units': 'metric',
        'lang': 'uz',
        'q': text
    }
    data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params).json()
    print(data)




bot.polling(none_stop=True)

