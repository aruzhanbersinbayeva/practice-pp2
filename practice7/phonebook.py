import psycopg2
from config import create
def get_conn():
    return psycopg2.connect(**create())

# --- CREATE TABLE ---
def create_table():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook(
                    username VARCHAR(50) PRIMARY KEY,
                    phone VARCHAR(20)
                )
            """)
    print("Table created")

# --- INSERT ---
def insert():
    name = input("Enter username: ")
    phone = input("Enter phone: ")
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO phonebook(username, phone) VALUES (%s, %s)",
                (name, phone)
            )
    print("Added")

# --- SHOW (SELECT) ---
def show():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            rows = cur.fetchall()
            for row in rows:
                print(row)

# --- UPDATE ---
def update():
    name = input("Enter username: ")
    new_phone = input("New phone: ")
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE phonebook SET phone=%s WHERE username=%s",
                (new_phone, name)
            )
    print("Updated ")

# --- DELETE ---
def delete():
    name = input("Enter username: ")
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM phonebook WHERE username=%s",
                (name,)
            )
    print("Deleted")

# --- SEARCH ---
def search():
    word = input("Search: ")
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE username ILIKE %s OR phone LIKE %s",
                (f"%{word}%", f"{word}%")
            )
            rows = cur.fetchall()
            for row in rows:
                print(row)

# --- MENU ---
def menu():
    while True:
        print("\n1.Create 2.Insert 3.Show 4.Update 5.Delete 6.Search 7.Exit")
        choice = input("Choose: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert()
        elif choice == "3":
            show()
        elif choice == "4":
            update()
        elif choice == "5":
            delete()
        elif choice == "6":
            search()
        elif choice == "7":
            break
        else:
            print("Try again!")

menu()
