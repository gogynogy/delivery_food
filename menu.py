from times import give_weak_day

monday = [
    ['Куриный суп', 'Суп веганский чечевичный'],
    [],
    ['Кола', 'Фанта', 'Спрайт', 'Кокос', 'Вода']
]

tuesday = [
    ['Такко с курицей', 'Такко с тофу', 'Такко с сыром', 'Ассорти из трех такко'],
    [],
    ['Кола', 'Фанта', 'Спрайт', 'Кокос', 'Вода']
]

wednesday = [
    ['Пельмени', 'Веганские вареники'],
    ['Блинчики с шоколадом', 'Блинчики со сгущенкой'],
    ['Кола', 'Фанта', 'Спрайт', 'Кокос', 'Вода']
]

thursday = [
    ['Паста болоньезе', 'Паста карбонара', 'Паста с маслом и чесноком'],
    [],
    ['Кола', 'Фанта', 'Спрайт', 'Кокос', 'Вода']
]

friday = [
    ['Рис с курицей', 'Веганский рис с овощами'],
    [],
    ['Кола', 'Фанта', 'Спрайт', 'Кокос', 'Вода']
]

def give_menu():
    day = give_weak_day()
    day += 1
    if day == 1:
        return monday
    elif day == 2:
        return tuesday
    elif day == 3:
        return wednesday
    elif day == 4:
        return thursday
    elif day == 5:
        return friday

price = 4800