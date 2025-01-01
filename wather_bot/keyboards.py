from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def generate_button():
    murkup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton(text='Dunyo ob-xavolari ⛅')
    murkup.add(btn)
    return murkup
