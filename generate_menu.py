from show_read_execute import display_menu, read_option, execute_option

def generate_menu(options, exit_option):
    option = None
    while option != exit_option:
        display_menu(options)
        option = read_option(options)
        execute_option(option, options)
        print()
