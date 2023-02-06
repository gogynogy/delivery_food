from aiogram import types
from aiogram.types import InlineKeyboardMarkup

import keyboard.admin.but as admin_but
import keyboard.user.but as user_but
from SQLBD import SQL
from data.config import admins
from loader import bot
from loader import dp
from messages.admin_messages import admin_start
from messages.user_messages import start_message, weekend_message, start_message_if_order
from times import give_weak_day

BD = SQL()

@dp.message_handler(commands="start")  # /start command processing
async def begin(message: types.Message):
    BD.check_account(message)
    markup = InlineKeyboardMarkup(row_width=1)
    if message.chat.id in admins:
        markup.add(admin_but.show_activity, user_but.start_order)
        await bot.send_message(chat_id=message.chat.id,
                               text=admin_start,
                               reply_markup=markup)
    else:
        if give_weak_day() == 5 or give_weak_day() == 6:
            markup.add(user_but.home)
            await bot.send_message(chat_id=message.chat.id,
                                   text=weekend_message,
                                   reply_markup=markup)
        else:
            if not BD.give_order(message.chat.id):
                markup.add(user_but.start_order)
                text = start_message
            else:
                markup.add(user_but.more_order)
                text = start_message_if_order(message.chat.id)
            await bot.send_message(chat_id=message.chat.id,
                                   text=text,
                                   reply_markup=markup)

@dp.callback_query_handler(lambda c: c.data == "Mainmenu")
async def startAgain(call: types.callback_query):
    BD.check_account(call.message)
    markup = InlineKeyboardMarkup(row_width=1)
    if call.message.chat.id in admins:
        markup.add(admin_but.show_activity, user_but.start_order)
        await bot.edit_message_text(chat_id=call.message.chat.id,
                                    text=admin_start,
                                    message_id=call.message.message_id,
                                    reply_markup=markup)
    else:
        if give_weak_day() == 5 or give_weak_day() == 6:
            markup.add(user_but.home)
            await bot.edit_message_text(chat_id=call.message.chat.id,
                                        text=weekend_message,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)
        else:
            if not BD.give_order(call.message.chat.id):
                markup.add(user_but.start_order)
                text = start_message
            else:
                markup.add(user_but.more_order)
                text = start_message_if_order(call.message.chat.id)
            await bot.edit_message_text(chat_id=call.message.chat.id,
                                        text=text,
                                        message_id=call.message.message_id,
                                        reply_markup=markup)