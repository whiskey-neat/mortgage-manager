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

creating_new_product_text = """
------------------------------------------
:: Creating a New Product
------------------------------------------
"""

def get_user_option():
    user_option = input("Please select a menu option: ")
    if user_option.isdigit():
        user_option = int(user_option)
    return user_option


display_main_menu = True

while display_main_menu:
    print(main_menu_text)
    menu_option = get_user_option()

    # CHECKS MAIN MENU OPTION
    if menu_option <= 3:
        display_main_menu = False

        if menu_option == 1: # SELECTS MANAGE MORTGAGE PRODUCTS
            display_products_menu = True

            while display_products_menu:
                print(products_menu_text)
                menu_option = get_user_option()

                if menu_option <= 5:
                    display_products_menu = False

                    if menu_option == 1: # PRODUCTS SUBMENU: SELECTS ADD PRODUCT
                        print(creating_new_product_text)
                        product_name = input("Please input product name : ")
                        product_interest_rate = input("Please input the interest rate for this product : ")
                        product_details = [product_name, product_interest_rate]

                        print(f"""
                        ==================================================
                        Product Summary
                        ==================================================
                        Product name : {product_name}
                        Product rate : {product_interest_rate}
                        --------------------------------------------------
                        """)

                        product_details_confirmation = input("Please confirm the product's details (input 1) to "
                                                             "proceed with "
                                                             "product creation (or any key to quit : ")

                        print(f"""
                        Creating New Product
                        Generating new product........
                        Generated product name : {product_name}
                        Generated product rate : {product_interest_rate}
                        """)
                        input("Press enter to continue")

                    elif menu_option == 2: # PRODUCTS SUBMENU: VIEW PRODUCTS
                        print("You selected 2")

                    elif menu_option == 3: # PRODUCTS SUBMENU: AMEND PRODUCT
                        print("You selected 3")

                    elif menu_option == 4: # PRODUCTS SUBMENU: DELETE PRODUCT
                        print("You selected 4")

                    else: # RETURN TO MAIN MENU
                        display_main_menu = True

        elif menu_option == 2: # MANAGE MORTGAGE QUOTES
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



