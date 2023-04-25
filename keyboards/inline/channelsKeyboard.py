from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def channel_keyboard(unfollow_channels):
    keyboard = InlineKeyboardMarkup()
    for channel in unfollow_channels:
        keyboard.add(
            InlineKeyboardButton(text=channel[1], url=f'https://t.me/{channel[2]}/'))
    return keyboard