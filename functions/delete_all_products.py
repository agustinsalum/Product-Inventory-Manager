from clear import clear_screen
from database_setup import get_db_connection
import sqlite3

def delete_all_products():
    clear_screen()
    print("Welcome to delete all products")
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        # Confirm deletion of all data
        confirm = input("Are you sure you want to delete all products? This action cannot be undone. (y/n): ")
        if confirm.lower() == 'y':
            cursor.execute("DELETE FROM Products")
            connection.commit()
            print("All products have been deleted from the inventory.")
        else:
            print("Deletion cancelled.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()