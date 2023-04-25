from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

viewTranslate = InlineKeyboardMarkup()
viewTranslate.add(
    InlineKeyboardButton(text="👀 Tarjimani ko'rish", callback_data='wiev_translate')
)