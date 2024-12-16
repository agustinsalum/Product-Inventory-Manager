
from generate_menu import generate_menu
from database_setup import create_folder, create_table_product

from functions.register_product import register_product
from functions.delete_product import delete_product
from functions.list_all_products import list_all_products
from functions.delete_all_products import delete_all_products
from functions.get_total_sum import get_total_sum
from functions.exit_program import exit_program

def main_menu():
    create_folder()
    create_table_product()
    options = {
    '1': ('Register Product', register_product),       # Add new products to the inventory
    '2': ('Delete Product', delete_product),           # Delete products from the inventory
    '3': ('Inventory List', list_all_products),        # Generate a full inventory list
    '4': ('Delete All Products', delete_all_products), # Remove all products from the inventory
    '5': ('Get total', get_total_sum),                     # Get the total of the products
    '6': ('Exit', exit_program)
    }
    generate_menu(options, list(options.keys())[-1]) # We get the last key of the dictionary
