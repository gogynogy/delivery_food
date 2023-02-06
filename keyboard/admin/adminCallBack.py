from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from SQLBD import SQL

BD = SQL()

start_work = CallbackData('p', 'what')

def makeButtonBuhloAdmin():
    buttons = InlineKeyboardMarkup(row_width=1)
    from converter.simple import SimpleConverter
    button_list = [InlineKeyboardButton(text=f"{name[2]} шт. {name[1]}", callback_data=start_work # {int(name[4]) * int(name[2])} LKR
                                        .new(what=name[1])) for name in BD.giveBuhloListAdmin()]
    return buttons.add(*button_list)