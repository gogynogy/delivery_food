from aiogram import types

from keyboard.user.but import home, contin_salat
from keyboard.user.userCallBack import salat_button, salat_order, topping_salat
from loader import dp, bot
from messages.user_messages import start_salat_message, choise_salat_topping
from SQLBD import SQL

BD = SQL()



@dp.callback_query_handler(lambda c: c.data == "salat")
async def StartSclad(call: types.callback_query):
    BD.check_salat(call.message.chat.id)
    await bot.edit_message_text(text=start_salat_message(call.message.chat.id),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=salat_button(call.message.chat.id).add(home, contin_salat))


@dp.callback_query_handler(salat_order.filter())
async def howmuchIsTheFish(call: types.callback_query, callback_data: dict):
    what = callback_data.get('what')
    BD.change_salat_component(call.message.chat.id, what)
    await bot.edit_message_text(text=start_salat_message(call.message.chat.id),
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=salat_button(call.message.chat.id).add(home, contin_salat))
    # except:
    #     pass


@dp.callback_query_handler(lambda c: c.data == "contin")
async def choise_topping(call: types.callback_query):
    await bot.edit_message_text(text=choise_salat_topping,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=topping_salat())