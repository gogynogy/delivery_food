from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

give_contact = KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
give_location = KeyboardButton('Отправить свою локацию 🗺️', request_location=True)

show_me = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)


cancel = InlineKeyboardButton(f'Отменить заполнение', callback_data="cancel")
home = InlineKeyboardButton(f"Главное меню", callback_data="/start")

buyproducts = InlineKeyboardButton(f"")