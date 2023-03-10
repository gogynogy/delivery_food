from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from aiogram import types


from SQLBD import SQL
BD = SQL()

menu = InlineKeyboardButton("Меню", callback_data="Menu")



bucket = InlineKeyboardButton("Моя корзина", callback_data="bucket")
cancel = InlineKeyboardButton(f'Галя, у нас отмена!!!', callback_data="cancel")
home = InlineKeyboardButton(f"Главное меню", callback_data="Mainmenu")
more_order = InlineKeyboardButton(f"Добавить еще одну порцию", callback_data="salat")
start_order = InlineKeyboardButton('Сделать заказ', callback_data="salat")
fruit = InlineKeyboardButton('fruit stakan', callback_data="fruit")
contin_salat = InlineKeyboardButton('Продолжить', callback_data="contin")
contin_fruit = InlineKeyboardButton('Продолжить', callback_data="contin_fruit")
order_done = InlineKeyboardButton('Сделать заказ', callback_data="order_done")


give_location = KeyboardButton('Отправить свою локацию', request_location=True)
give_contact = KeyboardButton('Отправить свой контакт', request_contact=True)
cancel_kb = InlineKeyboardButton(f'Галя, у нас отмена!!!', callback_data="cancel")

def write_customer(message: types.Message):
    button_url = f'tg://openmessage?user_id={message.chat.id}'
    return InlineKeyboardButton(text=f'написать {message.chat.first_name}',
                                url=button_url)


def cancelOperation():
    """Кнопка закрывания текущего действия"""
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(f'Галя, у нас отмена!!!', callback_data="cancel")]])
