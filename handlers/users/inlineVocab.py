from aiogram import types
from openpyxl.reader.excel import load_workbook

from loader import dp
from setList import get_engWords


@dp.message_handler(commands='inline_rejim')
async def bot_help(message: types.Message):
    text = ("Rasmda Botdan inline rejimda foydalanish ko'rsatilgan💁‍♂️")
    
    await message.answer_photo(photo="https://prnt.sc/1vu4pfd", caption=text)

@dp.inline_handler()
async def inline_vocab(query: types.InlineQuery):    
    letters = query.query.lower()
    find_list = []
    
    engWords = get_engWords()
    for eng in engWords:
        if eng[:len(letters)] == letters:
            find_list.append(eng)
    
    # DATA
    wb = load_workbook(filename="words_db.xlsx")
    sheet = wb.active
    
    # Result
    inline_results_python = []
    i=1
    for word in find_list:
        N = engWords.index(word) + 1        
        uzword = sheet[f'B{N}'].value
        
        inline_results_python.append(
            types.InlineQueryResultArticle(
                id = str(i),
                title = word.upper(),
                input_message_content = types.InputTextMessageContent(
                    message_text=f"{uzword}\n@EsUzbot"
                ),
                description=uzword
                
            )
        )
        i+=1
        
    await query.answer(inline_results_python[:50])
