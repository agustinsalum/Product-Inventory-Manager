import os

def clear_screen():
    if os.name == "nt": # Windows
        os.system("cls")
    else:
        os.system("clear") # Unix/Linux/MacOS