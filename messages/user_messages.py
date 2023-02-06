from aiogram import types

from keyboard.user.userCallBack import salat, fruit
from SQLBD import SQL
from menu import price

BD = SQL()

choise_salat_topping = 'choise_salat_topping'
start_message = 'Привет 👋🏻 С понедельника по пятницу мы доставляем Бизнес-ланчи разной тематики по всей Unawatuna 🏝\n' \
                'С 13:00- 15:00 и 16:00 - 17:00 ⏰\nМеню👨🏻‍🍳:\nСалат, горячие блюда и десерт с напитком на выбор.' \
                'Стоимость комплекта меню 4800 рупий.\nОплата наличными рупиями или рублями онлайн на карту Тиньков'
start_order_message = 'order message1'
second_order_message = 'order message2'
third_order_message = 'order message3'
what_time_delivered = 'what time delivered?'
ask_contact = 'ask contact'
ask_location = 'ask location'
weekend_message = 'weekend message'

def give_salat(user_id):
    salats = salat(user_id)
    list = []
    for i in salats:
        if salat(user_id)[i] == 1:
            list.append(i)
    if list == []:
        return None
    str = ", ".join(list)
    return str

def give_fruit(user_id):
    salats = fruit(user_id)
    list = []
    for i in salats:
        if fruit(user_id)[i] == 1:
            list.append(i)
    if list == []:
        return None
    str = ", ".join(list)
    return str


def start_message_if_order(id):
    orders = BD.give_order(id)
    text = 'your order all ready exist:\n\n'
    n = 0
    for order in orders:
        n += 1
        texts = f'order №{n}\n' \
                f'salat: {order[3]}\n' \
                f'first: {order[4]}\n' \
                f'second: {order[5]}\n' \
                f'drink: {order[6]}\n\n'
        text += ''.join(texts)
    return text


def admin_order_text(message: types.Message):
    orders = BD.give_order(message.chat.id)
    text = ' '
    if message.chat.username:
        text = f'@{message.chat.username} \n'
    n = 0
    for order in orders:
        n += 1
        texts = f'order №{n}\n' \
                f'salat: {order[3]}\n' \
                f'first: {order[4]}\n' \
                f'second: {order[5]}\n' \
                f'drink: {order[6]}\n\n'
        text += ''.join(texts)
        del_time = order[7]
    cost = price * n
    text += f'total cost: {cost} LKR.\ndelivery time {del_time}'
    return text


def start_salat_message(user_id):
    salat = give_salat(user_id)
    if salat == None:
        return "Собери свой ебучий салат"
    return f'Собери свой ебучий салат:\n{salat}\nМаксимум 5 компонентов'

def start_fruit_message(user_id):
    fruit = give_fruit(user_id)
    if fruit == []:
        return "Собери свой ебучий фруктовый стаканчик"
    return f'Собери свой ебучий фруктовый стаканчик:\n{fruit}\nМаксимум 2 компонента'

def give_order_text(id):
    mainmenu = BD.give_work_order(id)
    if mainmenu[4] == None:
        text = f'salat: {give_salat(id)}, {BD.give_topping(id)}\n' \
               f'first: {mainmenu[3]}\n' \
               f'fruits: {give_fruit(id)}\n' \
               f'drink: {mainmenu[5]}'
    else:
        text = f'salat: {give_salat(id)}, {BD.give_topping(id)}\n' \
               f'first: {mainmenu[3]}\n' \
               f'second: {mainmenu[4]}\n' \
               f'drink: {mainmenu[5]}'
    return text

def give_text_from_order(order):
    text = f'salat: {order[3]}\n' \
           f'first: {order[4]}\n' \
           f'second: {order[5]}\n' \
           f'drink: {order[6]}'
    return text
