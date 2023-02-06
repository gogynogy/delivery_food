from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from keyboard.user.but import start_order
from loader import dp
from messages.user_messages import start_message


@dp.message_handler(commands="help")
async def command_help(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(start_order)
    await message.answer(text=start_message,
                         reply_markup=markup)