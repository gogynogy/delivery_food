from aiogram import types

from keyboard.user.but import home, contin_fruit
from keyboard.user.userCallBack import fruit_button, fruit_order
from loader import dp, bot
from messages.user_messages import start_fruit_message
from SQLBD import SQL

BD = SQL()


@dp.callback_query_handler(lambda c: c.data == "fruit")
async def start_fruit(call: types.callback_query):
    BD.check_fruit(call.message.chat.id)
    await bot.edit_message_text(text=start_fruit_message(call.message.chat.id),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=fruit_button(call.message.chat.id).add(home, contin_fruit))


@dp.callback_query_handler(fruit_order.filter())
async def how_much_is_the_fruit(call: types.callback_query, callback_data: dict):
    try:
        what = callback_data.get('what')
        BD.change_fruit_component(call.message.chat.id, what)
        await bot.edit_message_text(text=start_fruit_message(call.message.chat.id),
                                    chat_id=call.message.chat.id,
                                    message_id=call.message.message_id,
                                    reply_markup=fruit_button(call.message.chat.id).add(home, contin_fruit))
    except:
        pass
