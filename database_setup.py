
import sqlite3, os

def get_db_connection():
    return sqlite3.connect("./database/database.db")

def create_folder():
    if not os.path.exists("database"):
            os.makedirs("database")

def create_table_product():
    try:
        connection = sqlite3.connect("./database/database.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                name TEXT,
                amount INTEGER,
                price REAL,
                tot REAL)''')
        connection.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

