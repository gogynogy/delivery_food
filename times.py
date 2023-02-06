from datetime import datetime


def give_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def give_weak_day():
    now = datetime.today().isoweekday()
    now = 3
    return now

def give_date():
    now = datetime.now()
    dt_string = now.strftime("%d/%m")
    return dt_string
