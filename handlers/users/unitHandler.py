from aiogram import types

from loader import dp
from dictionary import words


@dp.message_handler(state=None)
async def simpleTranslater(message: types.Message):
    user_word = message.text.lower()
    uzword = words.get(user_word, "Bunday so'z mavjud emas")
    
    await message.answer(uzword)