from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

books_keyboard = ReplyKeyboardMarkup()

for i in range(1,7):
    keyboard = KeyboardButton(text=f'🔰Essential English Words {i}')
    books_keyboard.add(keyboard)