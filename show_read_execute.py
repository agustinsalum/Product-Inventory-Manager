from clear import clear_screen

def execute_option(option, options):
    options[option][1]()
    input()
    clear_screen()

def display_menu(options):
    print('Select an option:')
    for key in sorted(options):
        print(f' {key}) {options[key][0]}')

def read_option(options):
    while (a := input('Option: ')) not in options:
        print('Incorrect option, please try again.')
        input()
        clear_screen()
        display_menu(options)
    return a
