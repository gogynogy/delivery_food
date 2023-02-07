from aiogram import types

from keyboard.user.userCallBack import salat, fruit
from SQLBD import SQL
from menu import price

BD = SQL()

start_message = 'Привет 👋🏻\nПо будням мы доставляем Бизнес-ланчи разной тематики по всей Unawatuna 🏝\nС 13:00- 15:00 и' \
                '16:00 - 17:00 ⏰\nЗаказы готовятся на следующий день ➡️\nЗакажи сегодня меню на завтра.\nМеню👨🏻‍🍳' \
                'Составной салат, выбор из двух разных горячих блюд и десерт с напитком на  выбор.\n' \
                'В меню входят вегетарианские позиции 🥗\nМеню на неделю:\n😵‍💫 Похмельный понедельник\n' \
                '🌮 Тако тьюсдей\n🥟 Пельменная среда\n🍝 Паста четверг\n🍛 Рисовая пятница\n' \
                'Стоимость комплекта меню 4800 рупий с доставкой.\n' \
                'Оплата наличными рупиями или рублями онлайн на карту Тинькофф.'
start_order_message = 'Выбери основное блюдо:'
second_order_message = 'Выбери второе блюдо:'
choise_salat_topping = 'Выбери топпинг для салата:'
third_order_message = 'Что ты будешь пить?'
what_time_delivered = 'Выбери интервал доставки:'
ask_contact = 'ask contact'
ask_location = 'Поделись своей локацией:'
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
        texts = f'Заказ №{n}\n' \
                f'Салат: {order[3]}\n' \
                f'Основное блюдо: {order[4]}\n' \
                f'Дополнительное блюдо: {order[5]}\n' \
                f'Пить: {order[6]}\n\n'
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
        texts = f'Заказ №{n}\n' \
                f'Салат: {order[3]}\n' \
                f'Основное блюдо: {order[4]}\n' \
                f'Дополнительное блюдо: {order[5]}\n' \
                f'Пить: {order[6]}\n\n'
        text += ''.join(texts)
        del_time = order[7]
    cost = price * n
    text += f'Общая сумма: {cost} LKR.\nВремя доставки {del_time}'
    return text


def start_salat_message(user_id):
    salat = give_salat(user_id)
    if salat == None:
        return "Собери свой салат"
    return f'Собери свой салат:\n{salat}\nМаксимум 5 компонентов'

def start_fruit_message(user_id):
    fruit = give_fruit(user_id)
    if fruit == []:
        return "Собери свой фруктовый стаканчик"
    return f'Собери свой фруктовый стаканчик:\n{fruit}\nМаксимум 2 компонента'

def give_order_text(id):
    mainmenu = BD.give_work_order(id)
    if not mainmenu[4]:
        text = f'Салат: {give_salat(id)}, {BD.give_topping(id)}\n' \
               f'Основное блюдо: {mainmenu[3]}\n' \
               f'Дополнительное блюдо: {give_fruit(id)}\n' \
               f'Пить: {mainmenu[5]}'
    else:
        text = f'Салат: {give_salat(id)}, {BD.give_topping(id)}\n' \
               f'Основное блюдо: {mainmenu[3]}\n' \
               f'Дополнительное блюдо: {mainmenu[4]}\n' \
               f'Пить: {mainmenu[5]}'
    return text
