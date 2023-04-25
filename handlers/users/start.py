from aiogram import types
from aiogram import Bot
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot
from data.config import ADMINS
from keyboards.inline.channelsKeyboard import channel_keyboard
from keyboards.inline.addGroupButton import add_button


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.chat.id
    full_name= message.chat.title
    username = message.from_user.username

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
        db.add_user(user_id, full_name, username)
        await message.answer(f"Salom, {message.from_user.full_name}!\n\nMarhamat inglizcha so'z yuboring yoki /inline_rejim dan foydalaning💁‍♂️\n🤩Men siz yuborgan so'z haqida to'liq ma'lumot beraman!", reply_markup=add_button)