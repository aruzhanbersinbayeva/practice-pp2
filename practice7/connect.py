import psycopg2
from config import create
def connect():
    config=create()
    with psycopg2.connect(**config) as conn:
        with con.cursor() as cur:
            cur.exxecute("""
                CREATE TABLE IF NOT EXISTS phonebook(
                    username VARCHAR(50) PRIMARY KEY,
                    phone VARCHAR(20)
                )
            """)
        con.commit()
connect()