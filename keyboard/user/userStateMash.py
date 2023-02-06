from aiogram.dispatcher.filters.state import StatesGroup, State


class buy_something(StatesGroup):
    what = State()
    count = State()

class UploadPhotoForm(StatesGroup):
    photo = State()

# готовый класс для загрузки фото! необходимо перенести хендлеры в hendlers
# @dp.callback_query_handler(lambda c: c.data == 'art')
# async def artpred(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await UploadPhotoForm.photo.set()
# @dp.message_handler(lambda message: message.photo is None, state=UploadPhotoForm.photo)
# async def process_photo_invalid(message: types.Message):
#     return await message.reply("Фотография не найдена в сообщении!")
# @dp.message_handler(lambda message: message.photo is not None, state=UploadPhotoForm.photo)
# async def process_photo(message: types.Message, state: FSMContext):
#     file_id = message.photo[-1].file_id  # file ID загруженной фотографии
#     # await bot.send_message(callback_query.from_user.id, 'XXXXXXX', reply_markup=KBB)
#     await bot.send_message(callback_query.from_user.id, "Фотография успешно загружена!")
#     await state.finish()