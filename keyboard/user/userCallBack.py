from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from SQLBD import SQL
from menu import give_menu

BD = SQL()


def give_button(what):
    if what == 0:
        return "🛑"
    elif what == 1:
        return "✅"

salat_order = CallbackData('a', 'what')
def salat(user_id):
    menu = BD.check_salat(user_id)
    salat = {
        'Огурец':menu[2],
        'Томат':menu[3],
        'Лук':menu[4],
        'Салат':menu[5],
        'Морковь':menu[6],
        'Кешью':menu[7],
        'Сельдерей':menu[8],
    }
    return salat
def salat_button(user_id):
    buttons = InlineKeyboardMarkup(row_width=1)
    button_list = [InlineKeyboardButton(text=f"{give_button(salat(user_id)[parrot])} "
                                             f"{parrot} {give_button(salat(user_id)[parrot])}",
                                        callback_data=salat_order.new(what=parrot))
                   for parrot in salat(user_id)]
    return buttons.add(*button_list)


fruit_order = CallbackData('b', 'what')
def fruit(user_id):
    menu = BD.check_fruit(user_id)
    fruit = {
        'Банан':menu[2],
        'Манго':menu[3],
        'Папайя':menu[4],
        'Ананас':menu[5],
    }
    return fruit
def fruit_button(user_id):
    buttons = InlineKeyboardMarkup(row_width=1)
    button_list = [InlineKeyboardButton(text=f"{give_button(fruit(user_id)[mango])} "
                                             f"{mango} {give_button(fruit(user_id)[mango])}",
                                        callback_data=fruit_order.new(what=mango))
                   for mango in fruit(user_id)]
    return buttons.add(*button_list)


first_dishes = CallbackData('c', 'what')
def first_plate():
    buttons = InlineKeyboardMarkup(row_width=1)
    button_list = [InlineKeyboardButton(text=mango,
                                        callback_data=first_dishes.new(what=mango))
                   for mango in give_menu()[0]]
    return buttons.add(*button_list)

second_dishes = CallbackData('d', 'what')
def second_plate():
    buttons = InlineKeyboardMarkup(row_width=1)
    button_list = [InlineKeyboardButton(text=mango,
                                        callback_data=second_dishes.new(what=mango))
                   for mango in give_menu()[1]]
    return buttons.add(*button_list)

third_dishes = CallbackData('e', 'what')
def third_plate():
    buttons = InlineKeyboardMarkup(row_width=1)
    button_list = [InlineKeyboardButton(text=mango,
                                        callback_data=third_dishes.new(what=mango))
                   for mango in give_menu()[2]]
    return buttons.add(*button_list)

salat_topping = [
    'Оливковое масло',
    'Кёрд',
]

topping = CallbackData('f', 'what')
def topping_salat():
    buttons = InlineKeyboardMarkup(row_width=1)
    button_list = [InlineKeyboardButton(text=mango,
                                        callback_data=topping.new(what=mango))
                   for mango in salat_topping]
    return buttons.add(*button_list)

time_delivery = [
    '13pm - 15pm',
    '16pm - 17pm',
]
delivery_time = CallbackData('g', 'delivery_time')
def delivery_time_but():
    buttons = InlineKeyboardMarkup(row_width=1)
    button_list = [InlineKeyboardButton(text=mango,
                                        callback_data=delivery_time.new(delivery_time=mango))
                   for mango in time_delivery]
    return buttons.add(*button_list)