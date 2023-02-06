from aiogram.dispatcher.filters.state import StatesGroup, State


class buySomething(StatesGroup):
    what = State()
    count = State()
    price = State()
    outPrice = State()
    category = State()

class addPosition(StatesGroup):
    what = State()
    outPrice = State()