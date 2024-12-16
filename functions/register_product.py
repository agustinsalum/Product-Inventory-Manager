
from clear import clear_screen
from database_setup import get_db_connection
import sqlite3

def register_product():
    clear_screen()
    print ("Welcome to product entry!")
    print ("")
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        # Get user input
        name = input("Name: ")
        try:
            tot = 0 
            amount = int(input("Amount: "))   
            price = float(input("Price: "))
            tot = price * amount  
            # Insert data into the database
            cursor.execute("""
                        INSERT INTO Products (name, amount, price ,tot) 
                        VALUES (?, ?, ?, ?)
                        """, (name, amount, price, tot))
            # Save changes and close connection
            connection.commit()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    else:
        print(f"The product: {name} was successfully created")
    finally:
        connection.close()