import psycopg2
from config import create
def connect():
    config=create()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook(
                    username VARCHAR(50) PRIMARY KEY,
                    phone VARCHAR(20)
                )
            """)
    print("connected")
connect()