def main_menu():
    print("\n------------------------------------------")
    print(":: Welcome to Mortgage Quotes System ::")
    print("------------------------------------------")
    print("1. Manage Mortgage Products")
    print("2. Manage Quotes")
    print("3. Quit")


def get_user_input(number):
    while True:
        try:
            user_option = int(input("\nPlease select a menu option: "))
        except ValueError:
            print("\nEnter a value between 1 and", number, "\n")
            continue
        if (user_option > number) or (user_option <= 0):
            print("\nEnter a value between 1 and", number, )
            continue
        else:
            break
    return user_option


def manage_products_menu():
    # DISPLAY SUB MENU TITLE AND OPTIONS
    print("\n------------------------------------------")
    print(":: Mortgage Products ::")
    print("------------------------------------------")
    print("1. Add Products")
    print("2. View Products")
    print("3. Amend Products")
    print("4. Delete Product")
    print("5. Return to Main Menu")


def manage_quotes_menu():
    # DISPLAY SUB MENU TITLE AND OPTIONS
    print("\n------------------------------------------")
    print(":: Mortgage Quotes ::")
    print("------------------------------------------")
    print("1. Create a quote")
    print("2. View a list of quotes")
    print("3. Amend a quote")
    print("4. Return to Main Menu")


def create_product():
    print("\n:: Creating a New Product ::")  # DISPLAY CREATE A NEW PRODUCT MENU
    print("--------------------------------------")
    new_product_name = input("Please input product name : ")  # ASK USER FOR A NEW PRODUCT NAME
    while True:
        try:
            new_product_rate = float(input("Please input the interest rate for this product : "))  # ASK USER FOR PRODUCT INTEREST RATE
        except ValueError:  # CHECK USER ENTERED A VALID NUMBER
            print("\nInterest rate must be a number.")
            continue
        if new_product_rate < 0:
            print("\nInterest rate cannot be negative.")
            continue
        else:
            break
    # AFTER USER HAS ENTERED PRODUCT DETAILS
    # GIVE USER A SUMMARY OF WHAT THEY HAVE ENTERED
    print("\n===================================================")
    print("Product Summary")
    print("===================================================")
    print("Product Name :", new_product_name)
    print("Product Rate :", new_product_rate)
    print("---------------------------------------------------")

    confirmation = input("\nPlease confirm the product's details (input 1) to proceed with product creation (or any key to quit) :")
    if confirmation == "1":
        new_product = [new_product_name, new_product_rate]
    else:
        manage_products_menu()
    print("\nCreating New Product")
    print("Generating new product........")
    print("Generated product name : ", new_product_name)
    print("Generated product rate", new_product_rate)
    input("Press enter to continue")
    return new_product

def view_products(existing_products):
    # SUBMENU HEADING
    print("\n================================================================================")
    print("List of Products")
    print("================================================================================")
    product_num = 1
    # LOOP THROUGH LIST AND DISPLAY EACH SUBLIST ON A NEW LINE
    for product, interest_rate in existing_products:
        print("No.", product_num, ":", product, "| Product rate :", interest_rate)
        product_num += 1
    print("--------------------------------------------------------------------------------")
    input("Press enter to continue")
    manage_products_menu()  # GO BACK TO MANAGE MORTGAGE PRODUCTS SUBMENU


#  --DISPLAY MAIN MENU--
display_main_menu = True
while display_main_menu:
    main_menu()
    main_menu_option = get_user_input(3)  # MAIN MENU: GET USER INPUT
    # if main_menu_option:
    #     display_main_menu = False

    #  --DISPLAY MANAGE MORTGAGE PRODUCTS--
    if main_menu_option == 1:
        display_products_menu = True
        product_list = [["Home Loan Flexi", 2.3], ["Santander Fresh Home Loan", 1.8], ["Barclays First-Time Mortgage", 1.98]]
        while display_products_menu:
            manage_products_menu()
            manage_products_option = get_user_input(5)
            # if manage_products_option:
            #     display_products_menu = False

            #  SUB-OPTION 1: ADD A NEW PRODUCT
            if manage_products_option == 1:
                new_product = create_product()
                product_list.append(new_product)
                print(product_list)

            #  SUB-OPTION 2: VIEW A LIST OF PRODUCTS
            elif manage_products_option == 2:
                view_products(product_list)

            #  SUB-OPTION 3: AMEND A PRODUCT
            elif manage_products_option == 3:
                print("\nThis is where you amend products")

            #  SUB-OPTION 4: DELETE A PRODUCT
            elif manage_products_option == 4:
                print("\nThis is where you delete products")

            #  SUB-OPTION 5: RETURN TO MAIN MENU
            else:
                pass

    #  --MANAGE MORTGAGE QUOTES--
    elif main_menu_option == 2:
        manage_quotes_menu()

    # OPTION 3: QUIT
    else:
        print("You exited")
