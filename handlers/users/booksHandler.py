from aiogram import types

from loader import dp
from keyboards.default.unitsKeyboard import units_keyboard

@dp.message_handler(state=None)
async def change_unit(message: types.Message):
    if "🔰Essential English Words" in message.text:
        for i in range(1,7):
            if message.text == f"🔰Essential English Words {i}":
                await message.answer(f"Unitni tanlang", reply_markup=units_keyboard)