from aiogram.types import CallbackQuery
from openpyxl import load_workbook

from loader import dp
from setList import get_engWords


@dp.callback_query_handler()
async def viewer(call: CallbackQuery):
    """Javobni ko'rsatuvchi funksiya"""
    rand_word = call.message.text
    wb = load_workbook(filename='words_db.xlsx')
    sheet = wb.active
    engWords = get_engWords()
    N = engWords.index(rand_word.lower()) + 1
    trans = sheet[f"B{N}"].value
    await call.message.edit_text(rand_word + '\n\n' + trans)