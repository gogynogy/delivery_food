from aiogram.utils import executor

from SQLBD import SQL
from hendlers import dp
from utils.notify_admins import on_start_up_notify, on_finish_notify
from utils.setBotCommands import set_default_commands

SQL = SQL()

async def on_startup(dp):
    await on_start_up_notify()
    await set_default_commands(dp)
    print("бот запущен")
    SQL.checkDB()


async def on_shutdown(dp):
    await on_finish_notify()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
