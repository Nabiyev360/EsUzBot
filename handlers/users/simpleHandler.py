from aiogram import types, Bot

from data.config import ADMINS
from gTrans import googler
from deep import deeper
from loader import dp, db, bot
from keyboards.inline.channelsKeyboard import channel_keyboard


@dp.message_handler(content_types=['text'], state=None)
async def simpleTranslater(message: types.Message):
    # CHEKSUB
    unfollow_channels, chek_list = [], []
    info = Bot.get_current()
    for ch in db.get_channels():
        try:
            member = await info.get_chat_member(ch[0], message.from_user.id)
            if member.is_chat_member() == False:
                unfollow_channels.append(ch)
                chek_list.append(False)   # True yoki False qo'shadi
        except:
            await bot.send_message(chat_id=ADMINS[0], text=f"Bot @{ch[2]} kanaliga admin qilinmagan!")

    if False in chek_list:
        await message.answer(text=f"Assalomu alaykum😊. Botdan to'liq foydalanish uchun quyidagi kanallarga a'zo bo'ling va /start ni bosing", reply_markup=channel_keyboard(unfollow_channels))

    else:
        user_word = message.text.lower()
        uzword = db.get_trans(user_word)
        if uzword:
            await message.reply(uzword[0][0])
            return

        try:
            # User botni o'zida inline rejimdan foydalansa, responsni ham tarjima qilamsligi uchun, #try'dan maqsad - agar xabar botni o'zidan kelmasa via_bot json'da viabot umuman bo'lmaydi va xatolik chiqadi
            if message.via_bot.username == 'EsUzBot':
                pass
        except:
            pass

    # googler & user_word
        if message.message_id %3 == 0:
            uzword = await googler(user_word)
        else:
            uzword = deeper(user_word)

        await message.reply(uzword)

        if message.from_user.id != ADMINS[0]:
            await message.forward(ADMINS[0])
            await bot.send_message(ADMINS[0], text=uzword)


@dp.message_handler(content_types=['photo', 'audio', 'video', 'document', 'voice', 'gif', 'sticker'])
async def for_others(message: types.Message):
    await message.forward(ADMINS[0])
