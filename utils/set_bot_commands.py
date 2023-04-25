from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("inline_rejim", "Inline rejim haqida ma'lumot"),
            types.BotCommand("random", "Tasodifiy so'z"),
            types.BotCommand("help", "Yordam"),
        ]
    )
