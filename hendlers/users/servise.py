from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup

import keyboard.user.but as but
from hendlers.users.start import begin
from loader import dp, bot


@dp.callback_query_handler(lambda c: c.data == "cancel", state="*")  #закрывает текущее действие
async def cancel(call: types.callback_query, state: FSMContext):
    await state.finish()
    await bot.edit_message_text(f"Заполнение прекращено",
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=InlineKeyboardMarkup(row_width=1).add(but.bucket).add(but.menu))
