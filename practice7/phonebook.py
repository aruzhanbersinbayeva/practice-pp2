username = input("Enter name: ")
phone = input("Enter phone: ")
cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING", (username, phone))
conn.commit()

cur.execute("UPDATE phonebook SET phone=%s WHERE username=%s", (new_phone, username))
conn.commit()

cur.execute("SELECT * FROM phonebook WHERE username LIKE 'A%'")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("DELETE FROM phonebook WHERE username=%s", (username,))
conn.commit()