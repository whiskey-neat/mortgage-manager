main_menu_text = """
------------------------------------------
:: Welcome to Mortgage Quotes System ::
------------------------------------------
1. Manage Mortgage Products
2. Manage Quotes
3. Quit
"""

products_menu_text = """
------------------------------------------
:: Mortgage Products ::
------------------------------------------
1. Add Product
2. View Product
3. Amend Product
4. Delete Product
5. Return Product
"""

quotes_menu_text = """
------------------------------------------
:: Manage Quotes ::
------------------------------------------
1. Create a quote
2. View a list of quotes
3. Amend a quote
4. Return to Main Menu
"""

def get_user_option():
    user_option = input("Please select a menu option: ")
    if user_option.isdigit():
        user_option = int(user_option)
    return user_option

def main_menu_option(user_option):



display_main_menu = True

while display_main_menu:
    print(main_menu_text)
    menu_option = get_user_option()

    # CHECKS MAIN MENU OPTION
    if menu_option <= 3:
        display_main_menu = False

        if menu_option == 1: # MANAGE MORTGAGE PRODUCTS
            display_products_menu = True

            while display_products_menu:
                print(products_menu_text)
                menu_option = get_user_option()

                if menu_option <= 5:
                    display_products_menu = False

                    if menu_option == 1: # ADD PRODUCT

                    elif menu_option == 2: # VIEW PRODUCTS

                    elif menu_option == 3: # AMEND PRODUCT

                    elif menu_option == 4: # DELETE PRODUCT

                    else: # RETURN TO MAIN MENU
                        display_main_menu = True

        elif menu_option == 2: # MANAGE MORTAGGE QUOTES
            display_quotes_menu = True

            # Displays Sub-Menu
            while display_quotes_menu:
                print(quotes_menu_text)
                menu_option = get_user_option()

        # QUIT THE APPLICATION
        else:
            print("You exited.")
    else:
        print("\nEnter a valid option")



