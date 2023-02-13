from aiogram import types
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from data.config import admins
from hendlers.users.fruit import start_fruit
from keyboard.user.but import home, order_done, give_location, give_contact, cancel, cancel_kb, write_customer
from keyboard.user.userCallBack import first_plate, first_dishes, second_plate, second_dishes, third_plate, \
    third_dishes, topping, delivery_time, delivery_time_but
from loader import dp, bot

from SQLBD import SQL
from menu import give_menu
from messages.user_messages import start_order_message, second_order_message, third_order_message, ask_location, \
    ask_contact, give_salat, give_fruit, give_order_text, admin_order_text, what_time_delivered
from times import give_weak_day
from utils.notify_admins import gosha

BD = SQL()

@dp.callback_query_handler(topping.filter())
async def continue_order(call: types.callback_query, callback_data: dict):
    topping = callback_data.get('what')
    BD.delete_work_order(call.message.chat.id)
    BD.chenge_salat_topping(call.message.chat.id, topping)
    await bot.edit_message_text(text=start_order_message,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=first_plate().add(home))


@dp.callback_query_handler(first_dishes.filter())
async def select_second_plate(call: types.callback_query, callback_data: dict):
    first = callback_data.get('what')
    BD.change_work_order(call.message.chat.id, 'First', first)
    if give_menu()[1] == []:
        await start_fruit(call)
    else:
        await bot.edit_message_text(text=second_order_message,
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=second_plate().add(home))


@dp.callback_query_handler(second_dishes.filter())
async def select_second_plate(call: types.callback_query, callback_data: dict):
    if callback_data != []:
        first = callback_data.get('what')
        BD.change_work_order(call.message.chat.id, 'Second', first)
    await bot.edit_message_text(text=third_order_message,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=third_plate().add(home))


@dp.callback_query_handler(lambda c: c.data == "contin_fruit")
async def finish_fruit(call: types.callback_query):
    await select_second_plate(call, callback_data=[])

@dp.callback_query_handler(third_dishes.filter())
async def select_third_plate(call: types.callback_query, callback_data: dict):
    first = callback_data.get('what')
    BD.change_work_order(call.message.chat.id, 'Drink', first)
    markup = InlineKeyboardMarkup(row_width=1)
    await bot.edit_message_text(text=give_order_text(call.message.chat.id),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=markup.add(home, order_done))


@dp.callback_query_handler(lambda c: c.data == "order_done")
async def time_of_delivery(call: types.callback_query):
    BD.create_order(call.message.chat.id)
    await bot.edit_message_text(text=what_time_delivered,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=delivery_time_but())


@dp.callback_query_handler(delivery_time.filter())
async def location(call: types.callback_query, callback_data: dict):
    delivery_tim = callback_data.get('delivery_time')
    BD.add_order(delivery_tim, call.message.chat.id)
    await bot.send_message(text=ask_location,
                            chat_id=call.message.chat.id,
                            reply_markup=ReplyKeyboardMarkup(one_time_keyboard=True).add(give_location))


@dp.message_handler(content_types=["location"])
async def location(message: types.Message):
    if message.location is not None:
        await bot.send_message(text='Локация принята',
                               chat_id=message.chat.id,
                               reply_markup=ReplyKeyboardRemove())
        await bot.send_message(text='Заказ принят',
                               chat_id=message.chat.id,
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(home))
        for admin in admins:
            await bot.send_message(chat_id=admin,
                                   text=admin_order_text(message),
                                   reply_markup=InlineKeyboardMarkup(row_width=1).add(write_customer(message)))
        await bot.send_location(gosha,
                                message.location.latitude,
                                message.location.longitude)
    if not message.chat.username:
        await bot.send_message(chat_id=message.chat.id,
                               text='Привет, у тебя отсутствует юзернейм, или мы не можем'
                                    ' написать тебе изза настроек приватности.\n\n'
                                    'напиши: @matrix77777',
                               reply_markup=InlineKeyboardMarkup(row_width=1).add(home))