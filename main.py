def main_menu():
    print("------------------------------------------")
    print(":: Welcome to Mortgage Quotes System ::")
    print("------------------------------------------")
    print("1. Manage Mortgage Products")
    print("2. Manage Quotes")
    print("3. Quit")
    try:
        option = int(input("\nPlease select a menu option: "))
        if (option > 3) or (option < 0):
            print("\nEnter a value between 1 and 3\n")
            main_menu()
        elif option == 1:
            manage_products_menu()
        elif option == 2:
            manage_quotes_menu()
        else:
            print("You exited")
            exit()
    except ValueError:
        print("\nEnter a value between 1 and 3\n")
        main_menu()


# MANAGE MORTGAGE PRODUCTS
def manage_products_menu():
    print("------------------------------------------")
    print(":: Mortgage Products ::")
    print("------------------------------------------")
    print("1. Add Products")
    print("2. View Products")
    print("3. Amend Products")
    print("4. Delete Product")
    print("5. Return to Main Menu")
    try:
        option = int(input("\nPlease select a menu option: "))
        if (option > 5) or (option < 0):
            print("\nEnter a value between 1 and 5\n")
            manage_products_menu()
        elif option == 1:
            add_product()
        elif option == 2:
            view_products()
        elif option == 3:
            amend_product()
        elif option == 4:
            delete_product()
        else:
            main_menu()
    # IF USER ENTERS SOMETHING UNEXPECTED
    except ValueError:
        print("\nEnter a value between 1 and 5\n")
        manage_products_menu()


# MANAGE MORTGAGE PRODUCTS SUBMENU FUNCTIONS

def add_product():
    print("THIS IS PRODUCT SUB-MENU")


def view_products():
    print("THIS IS PRODUCT SUB-MENU")


def amend_product():
    print("THIS IS PRODUCT SUB-MENU")


def delete_product():
    print("THIS IS PRODUCT SUB-MENU")


# MANAGE MORTGAGE QUOTES

def manage_quotes_menu():
    print("------------------------------------------")
    print(":: Mortgage Quotes ::")
    print("------------------------------------------")
    print("1. Create a quote")
    print("2. View a list of quotes")
    print("3. Amend a quote")
    print("4. Return to Main Menu")
    try:
        option = int(input("\nPlease select a menu option: "))
        if (option > 4) or (option < 0):
            print("\nEnter a value between 1 and 5\n")
            manage_quotes_menu()
        elif option == 1:
            create_quote()
        elif option == 2:
            view_quotes()
        elif option == 3:
            amend_quote()
        else:
            main_menu()

    except ValueError:
        print("\nEnter a value between 1 and 5\n")
        manage_quotes_menu()


# MANAGE MORTGAGE QUOTES SUBMENU FUNCTIONS

def create_quote():
    print("THIS IS QUOTE SUB-MENU")


def view_quotes():
    print("THIS IS QUOTE SUB-MENU")


def amend_quote():
    print("THIS IS QUOTE SUB-MENU")


main_menu()



