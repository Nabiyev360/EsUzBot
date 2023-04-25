from aiogram import types, Bot
from random import randint

from loader import dp, db, bot
from data.config import ADMINS
from setList import get_engWords
from keyboards.inline.viewButton import viewTranslate
from keyboards.inline.channelsKeyboard import channel_keyboard


@dp.message_handler(commands='random')
async def randomer(message: types.Message):
    # Majburiy a'zolik
    chek_list = []
    unfollow_channels = []
    for ch in db.get_channels():
        try:
            info = Bot.get_current()
            member = await info.get_chat_member(ch[0], message.from_user.id)
            if member.is_chat_member() == False:
                unfollow_channels.append(ch)
                chek_list.append(False)   #True yoki False qo'shadi
        except:
            await bot.send_message(
                chat_id=ADMINS[0], text = f"Bot @{ch[2]} kanaliga admin qilinmagan!")
            
    if False in chek_list:
        await message.answer(
            text = f"Assalomu alaykum😊. Botdan to'liq foydalanish uchun quyidagi kanallarga a'zo bo'ling va /start ni bosing",
            reply_markup=channel_keyboard(unfollow_channels))
    
    else:
        engWords = get_engWords()
        word = engWords[randint(0, len(engWords)-1)] # print(len(engWords))  ---> 1269
        await message.answer(word.title(), reply_markup=viewTranslate)