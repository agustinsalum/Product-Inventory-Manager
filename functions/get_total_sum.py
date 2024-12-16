
from clear import clear_screen
from database_setup import get_db_connection
import sqlite3

def get_total_sum():
    clear_screen()
    print("Welcome to get the total sum of all products")
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Get the sum of the 'tot' column
        cursor.execute("SELECT SUM(tot) FROM Products")
        # Get the result of the query
        total_sum = cursor.fetchone()[0]

        if total_sum is not None:
            print(f"The total sum of all products is: ${total_sum}")
        else:
            print("No products found in the inventory.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()