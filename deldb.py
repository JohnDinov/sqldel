import sqlite3

connection = sqlite3.connect("user.db") # Подключаемся к базе данных
cursor = connection.cursor() # Создаём курсор управления


def delete_info():
    info = input("""Какое значение:
            * name
            * surname
            * id
            * balance
            * role
""")
    newinfo = input("Новое значение: ")
    rowid = input("rowid")

    cursor.execute(f"UPDATE users SET {info} = ? WHERE rowid = ?", (newinfo, rowid))
    connection.commit()
    print("Данные изменены")

    connection.close()

delete_info()