
from clear import clear_screen
from database_setup import get_db_connection
import sqlite3


def delete_product():
    clear_screen()
    print ("Welcome to delete product")
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        product_name = input("Enter the product name to delete: ")
        # Check if the product exists in the database
        cursor.execute("SELECT * FROM Products WHERE name = ?", (product_name,))
        product = cursor.fetchone()
        if product:
            # If the product exists, confirm deletion
            confirm = input(f"Are you sure you want to delete {product_name}? (y/n): ")
            if confirm.lower() == 'y':
                # Delete the product from the database
                cursor.execute("DELETE FROM Products WHERE name = ?", (product_name,))
                connection.commit()
                print(f"{product_name} has been deleted from the inventory.")
            else:
                print("Deletion cancelled.")
        else:
            print("Product not found.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    else:
        if product and confirm.lower == 'y':
            print(f"The product: {product_name} was successfully deleted")
    finally:
        connection.close()