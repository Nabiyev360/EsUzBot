from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Botga inglizcha so'z yuboring. U sizga so'zning o'zbekcha tarjimasi, tavsifi va misollarni keltiradi.\n\nBuyruqlar: ",
            "/start - Botni ishga tushirish",
            "/random - Yordam",
            "/inline_rejim - Inline rejim uchun yo'riqnoma",
            "Dasturchi: @nabiyevdev")
    
    await message.answer("\n".join(text))