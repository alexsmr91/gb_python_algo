"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import sqlite3
from hashlib import sha256
from uuid import uuid4


class PassDataBase:
    def con(self):
        return sqlite3.connect(self.filename, isolation_level=None)

    def cur(self):
        return self.con().cursor()

    def close(self):
        self.con().commit()
        self.con().close()

    def __init__(self, filename):
        self.filename = filename
        query = """
        CREATE TABLE IF NOT EXISTS "passwords" (
        "hash" VARCHAR(64) NULL,
        "salt" VARCHAR(32) NULL,
        "login" VARCHAR(100) NULL);
        """
        try:
            self.cur().execute(query)
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
        else:
            self.close()

    def get_user_data(self, login):
        try:
            cur = self.cur()
            cur.execute("SELECT salt, hash FROM passwords WHERE login = ?", (login,))
            res = cur.fetchall()
            res.append(("", ""))
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
            res = [("", "")]
        else:
            self.close()
        return res

    def user_exists(self, login):
        return self.get_user_data(login) != [("", "")]

    def set_user_data(self, login, salt, hash):
        if self.user_exists(login):
            try:
                self.cur().execute("""UPDATE passwords SET hash = ? , salt = ? WHERE login= ?""", (hash, salt, login))
            except sqlite3.DatabaseError as err:
                print("Error: ", err)
            else:
                self.close()
        else:
            try:
                self.cur().execute("""INSERT INTO passwords VALUES ( ? , ? , ? )""", (hash, salt, login))
            except sqlite3.DatabaseError as err:
                print("Error: ", err)
            else:
                self.close()


if __name__ == "__main__":
    db = PassDataBase("pass_db.sqlite")
    login = input("Введите логин: ")
    salt, hash = db.get_user_data(login)[0]
    for i in range(2):
        password = input("Введите пароль: ").encode()
        if salt == "" and hash == "":
            salt = uuid4().hex
            hash = sha256(password + salt.encode()).hexdigest()
            db.set_user_data(login, salt, hash)
            print(f"Поздравляю с регистрацией {login}!")
            print(hash)
        elif sha256(password + salt.encode()).hexdigest() == hash:
            print("Верный пароль")
            break
        else:
            print("Неправильная пара логин/пароль")
            break
