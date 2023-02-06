import asyncio
import sqlite3
from times import give_time, give_date
from utils.notify_admins import info_admin

class SQL:
    def __init__(self):
        """Initializing Database Connection"""
        self.conn = sqlite3.connect("fooddelivery.db")
        self.cursor = self.conn.cursor()

    def checkDB(self):
        """проверяет наличие базы данных"""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `Users` (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid TEXT,
            user_name TEXT,
            Count INT NOT NULL DEFAULT 1,
            LastTime TEXT,
            Info TEXT,
            contact TEXT
            )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `Salat` (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid TEXT,
            Огурец INT NOT NULL DEFAULT 0,
            Томат INT NOT NULL DEFAULT 0,
            Лук INT NOT NULL DEFAULT 0,
            Салат INT NOT NULL DEFAULT 0,
            Морковь INT NOT NULL DEFAULT 0,
            Кешью INT NOT NULL DEFAULT 0,
            Сельдерей INT NOT NULL DEFAULT 0,
            Топпинг TEXT
            )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `Fruits` (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid TEXT,
            Банан INT NOT NULL DEFAULT 0,
            Манго INT NOT NULL DEFAULT 0,
            Папайя INT NOT NULL DEFAULT 0,
            Ананас INT NOT NULL DEFAULT 0
            )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'Orders' (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Date TEXT,
            userid TEXT,
            Salat TEXT,
            First TEXT,
            Second TEXT,
            Drink TEXT,
            Comment TEXT
            )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'WorkOrders' (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Date TEXT,
            userid TEXT,
            First TEXT,
            Second TEXT,
            Drink TEXT
            )""")
        self.conn.commit()

    def check_account(self, message):
        """checks if the id exists in the database"""
        try:
            self.cursor.execute("SELECT userid FROM Users WHERE userid = (?)", (message.chat.id,))
            if not self.cursor.fetchone():
                if message.chat.username:
                    username = message.chat.username
                else:
                    username = message.chat.first_name
                self.cursor.execute(f"INSERT INTO Users (userid, user_name, LastTime) VALUES (?, ?, ?)",
                                    (message.chat.id, username, give_time()))
            else:
                self.cursor.execute('''UPDATE Users SET Count = (Count + 1) WHERE userid = ?''',
                                    (message.chat.id,))
                self.cursor.execute('''UPDATE Users SET LastTime = (?) WHERE userid = ?''',
                                    (give_time(), message.chat.id))
                return True
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite addSQL, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def check_salat(self, userid):
        try:
            self.cursor.execute("SELECT * FROM Salat WHERE userid = (?)", (userid, ))
            list = self.cursor.fetchone()
            if list is None:
                self.cursor.execute("INSERT INTO Salat (userid) VALUES (?)", (userid, ))
                return list
            else:
                return list
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite create_salad, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def change_salat_component(self, userid, salat_component):
            try:
                self.cursor.execute(f"SELECT {salat_component} FROM Salat WHERE userid = {userid}")
                num = self.cursor.fetchone()[0]
                if num == 1:
                    self.cursor.execute(f"UPDATE Salat SET {salat_component} = 0 WHERE userid = {userid}")
                else:
                    if sum(self.check_salat(userid)[2:-1]) < 5:
                        self.cursor.execute(f"UPDATE Salat SET {salat_component} = 1 WHERE userid = {userid}")
                    else:
                        return
            except sqlite3.Error as error:
                text = f'Ошибка при работе с SQLite change_salat_component, {error}'
                asyncio.create_task(info_admin(text))
            finally:
                self.conn.commit()

    def chenge_salat_topping(self, userid, topping):
        try:
            self.cursor.execute(f"UPDATE Salat SET Топпинг = (?) WHERE userid = ?", (topping, userid))
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite chenge_salat_topping, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def give_topping(self, userid):
        try:
            self.cursor.execute(f"SELECT Топпинг FROM Salat WHERE userid = {userid}")
            topping = self.cursor.fetchone()
            return ', '.join(topping)
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite give_topping, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def give_salat_words(self, userid):
        salat = self.check_salat(userid)
        salats = {
            'Огурец': salat[2],
            'Томат': salat[3],
            'Лук': salat[4],
            'Салат': salat[5],
            'Морковь': salat[6],
            'Кешью': salat[7],
            'Сельдерей': salat[8],
        }
        list = []
        for i in salats:
            if salats[i] == 1:
                list.append(i)
        if list == []:
            return None
        str = ", ".join(list)
        return str

    def check_fruit(self, userid):
        try:
            self.cursor.execute("SELECT * FROM Fruits WHERE userid = (?)", (userid, ))
            list = self.cursor.fetchone()
            if list is None:
                self.cursor.execute("INSERT INTO Fruits (userid) VALUES (?)", (userid, ))
                return list
            else:
                return list
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite check_fruit, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def change_fruit_component(self, userid, fruit_component):
            try:
                self.cursor.execute(f"SELECT {fruit_component} FROM Fruits WHERE userid = {userid}")
                num = self.cursor.fetchone()[0]
                if num == 1:
                    self.cursor.execute(f"UPDATE Fruits SET {fruit_component} = 0 WHERE userid = {userid}")
                else:
                    if sum(self.check_fruit(userid)[2:]) < 2:
                        self.cursor.execute(f"UPDATE Fruits SET {fruit_component} = 1 WHERE userid = {userid}")
                    else:
                        return
            except sqlite3.Error as error:
                text = f'Ошибка при работе с SQLite change_fruit_component, {error}'
                asyncio.create_task(info_admin(text))
            finally:
                self.conn.commit()

    def give_fruit_words(self, userid):
        fruit = self.check_fruit(userid)
        fruits = {
            'Банан': fruit[2],
            'Манго': fruit[3],
            'Папайя': fruit[4],
            'Ананас': fruit[5],
        }
        list = []
        for i in fruits:
            if fruits[i] == 1:
                list.append(i)
        if list == []:
            return None
        str = ", ".join(list)
        return str

    def change_work_order(self, userid, order, what):
        try:
            self.cursor.execute(f"SELECT * FROM WorkOrders WHERE userid = {userid}")
            if self.cursor.fetchone() == None:
                self.cursor.execute("INSERT INTO WorkOrders (userid) VALUES (?)", (userid, ))
            self.cursor.execute(f"UPDATE WorkOrders SET {order} = '{what}' WHERE userid = {userid}")
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite change_work_order, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def give_work_order(self, userid):
        try:
            self.cursor.execute(f"SELECT * FROM WorkOrders WHERE userid = {userid}")
            return self.cursor.fetchone()
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite give_work_order, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()


    def delete_work_order(self, userid):
        try:
            self.cursor.execute("SELECT * FROM WorkOrders WHERE userid = (?)", (userid, ))
            if self.cursor.fetchone():
                self.cursor.execute("DELETE FROM WorkOrders WHERE userid = ?", (userid,))
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite delete_work_order, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()


    def create_order(self, userid):
        try:
            self.cursor.execute(f"SELECT * FROM WorkOrders WHERE userid = {userid}")
            menu = self.cursor.fetchone()
            if menu is not None:
                fruits = self.give_fruit_words(userid)
                salat = self.give_salat_words(userid)
                if not menu[4]:
                    self.cursor.execute("INSERT INTO Orders (Date, userid, Salat, First, Second, Drink) VALUES "
                                        "(?, ?, ?, ?, ?, ?)", (give_date(), userid, salat, menu[3], fruits, menu[5]))
                else:
                    self.cursor.execute("INSERT INTO Orders (Date, userid, Salat, First, Second, Drink) VALUES "
                                        "(?, ?, ?, ?, ?, ?)", (give_date(), userid, salat, menu[3], menu[4], menu[5]))
                self.cursor.execute("DELETE FROM WorkOrders WHERE userid = ?", (userid,))
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite create_order, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def add_order(self, time, userid):
        try:
            self.cursor.execute(f"UPDATE Orders SET Comment = '{time}' WHERE userid = {userid} and Date = {give_date()}")
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite add_order, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def give_order(self, userid):
        try:
            self.cursor.execute(f"SELECT * FROM Orders WHERE userid = ? AND Date = ?", (userid, give_date()))
            return self.cursor.fetchall()
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite give_order, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def watch_activity(self):
        try:
            self.cursor.execute("SELECT * FROM Users ORDER BY LastTime")
            text = "\n".join([f'{user[0]}) @{user[2]} обращений {user[3]}\n'
                              f'последнее обращение {user[4]}' for user in (self.cursor.fetchall())])
            return text
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite watch_activity, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()

    def clear_bucket(self, id):
        try:
            self.cursor.execute("DELETE FROM Orders WHERE TelegramNikName = ?", (id, ))
        except sqlite3.Error as error:
            text = f'Ошибка при работе с SQLite clearBucket, {error}'
            asyncio.create_task(info_admin(text))
        finally:
            self.conn.commit()