from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

from SQLBD import SQL

BD = SQL()
invent = InlineKeyboardButton("Устроить инвентуру", callback_data="invent")
NewPosition = InlineKeyboardButton("Добавить позицию", callback_data="NewPosition")
NewProduct = InlineKeyboardButton("Добавить Купленное", callback_data="NewProduct")
show_activity = InlineKeyboardButton("Посмотреть активность", callback_data="show_activity")


menu = InlineKeyboardButton("Меню", callback_data="Menuadmin")
cancelfake = InlineKeyboardButton(f'отмена!!!', callback_data="cancelfake")
home = InlineKeyboardButton(f"Главное меню", callback_data="Mainmenu")
order = InlineKeyboardButton(f"Сделать заказ", callback_data="Order")
give_location = KeyboardButton('Отправить свою локацию', request_location=True)
show_all_sklad = InlineKeyboardButton('Show all storage', callback_data='show_all_sklad')


def cancelOperation():
    """Кнопка закрывания текущего действия"""
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(f'Отменить заполнение', callback_data="canceladmin")]])


