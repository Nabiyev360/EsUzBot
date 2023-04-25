from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

units_keyboard = ReplyKeyboardMarkup()

for i in range(1,31):
    keyboard = KeyboardButton(text=f'📖Unit {i}')
    units_keyboard.add(keyboard)