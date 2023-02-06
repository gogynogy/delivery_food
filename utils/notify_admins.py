from data.config import admins
from loader import bot


gosha = 498332094


async def write_admin(message):
    for admin in admins:
        await bot.send_message(admin, message)

async def on_start_up_notify():
    await bot.send_message(gosha, "бот запущен")

async def on_finish_notify():
    await bot.send_message(gosha, "бот наебнулся")


async def info_admin(text):
    await bot.send_message(gosha, text)