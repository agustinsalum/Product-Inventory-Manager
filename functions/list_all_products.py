
from clear import clear_screen
from database_setup import get_db_connection
import sqlite3


def list_all_products():
    clear_screen()
    print ("Welcome to list all products")
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        # Execute a query to get all products from the database
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()
        if products:
            # If there are products in the inventory, display them
            print("\nFull Inventory List:")
            for product in products:
                print ("")
                print(f"Name: {product[0]} ; Amount: {product[1]} ; Price: {product[2]} ; Tot: {product[3]}")
        else:
            print("No products found in the inventory.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()