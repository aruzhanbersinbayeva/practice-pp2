# phonebook.py
from connect import connect

# подключаемся к базе
conn = connect()
cur = conn.cursor()

# -------------------------------
# 1 Вставка или обновление пользователя
cur.execute("CALL insert_or_update(%s, %s)", ("Aruzhan", "87001234567"))
conn.commit()  # обязательно сохранить изменения

# -------------------------------
# 2 Bulk insert (много пользователей)
names = ["Ali", "Dana"]
phones = ["87001111111", "87002222222"]

cur.execute("CALL bulk_insert(%s, %s)", (names, phones))
conn.commit()

# -------------------------------
# 3 Поиск по шаблону
cur.execute("SELECT * FROM search_pattern(%s)", ("ru",))
rows = cur.fetchall()
print("Поиск по шаблону:")
for row in rows:
    print(row)

# -------------------------------
# 4 Пагинация
cur.execute("SELECT * FROM get_paginated(%s, %s)", (5, 0))
rows = cur.fetchall()
print("Первые 5 записей:")
for row in rows:
    print(row)

# -------------------------------
# 5 Удаление пользователя
cur.execute("CALL delete_user(%s)", ("Ali",))
conn.commit()

# -------------------------------
# Закрываем соединение
cur.close()
conn.close()