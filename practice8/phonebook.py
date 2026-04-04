from connect import connect  # connect.py с функцией connect()

# Подключаемся к базе
conn = connect()
cur = conn.cursor()

# -------------------------------
# 1️⃣ Вставка или обновление пользователя
cur.execute("CALL insert_or_update(%s, %s)", ("Alem", "87001234567"))
conn.commit()

# -------------------------------
# 2️⃣ Bulk insert (много пользователей)
names = ["Ali", "Dana", "Nina"]
phones = ["87001111111", "87002222222", "123"]  # последний короткий, будет Notice

cur.execute("CALL bulk_insert(%s, %s)", (names, phones))
conn.commit()

# -------------------------------
# 3️⃣ Поиск по шаблону
cur.execute("SELECT * FROM search_pattern(%s)", ("A%",))
rows = cur.fetchall()
print("Поиск по шаблону:")
for row in rows:
    print(row)

# -------------------------------
# 4️⃣ Пагинация
cur.execute("SELECT * FROM get_paginated(%s, %s)", (5, 0))
rows = cur.fetchall()
print("Первые 5 записей:")
for row in rows:
    print(row)

# -------------------------------
# 5️⃣ Удаление пользователя
cur.execute("CALL delete_user(%s)", ("Ali",))
conn.commit()

# -------------------------------
# Закрываем соединение
cur.close()
conn.close()