def main_menu():
    print("\n------------------------------------------")
    print(":: Welcome to Mortgage Quotes System ::")
    print("------------------------------------------")
    print("1. Manage Mortgage Products")
    print("2. Manage Quotes")
    print("3. Quit")


# MANAGE PRODUCTS MENU
def manage_products_menu():
    print("\n------------------------------------------")
    print(":: Mortgage Products ::")
    print("------------------------------------------")
    print("1. Add Products")
    print("2. View Products")
    print("3. Amend Products")
    print("4. Delete Product")
    print("5. Return to Main Menu")


# MANAGE QUOTES SUBMENU
def manage_quotes_menu():
    print("\n------------------------------------------")
    print(":: Mortgage Quotes ::")
    print("------------------------------------------")
    print("1. Create a quote")
    print("2. View a list of quotes")
    print("3. Amend a quote")
    print("4. Return to Main Menu")


def user_menu_choice(number):
    while True:
        try:
            user_option = int(input("\nPlease select a menu option: "))
        except ValueError:
            print("\nEnter a value between 1 and", number)
            display_current_menu()
            continue
        if (user_option > number) or (user_option <= 0):
            print("\nEnter a value between 1 and", number)
            display_current_menu()
            continue
        else:
            break
    return user_option


# CHOOSE WHICH MENU SHOULD BE DISPLAYED WHEN VALIDATING INPUT
def display_current_menu():
    if display_main_menu:
        main_menu()
    elif display_products_menu:
        manage_products_menu()
    elif display_quotes_menu:
        manage_quotes_menu()


def create_product():
    print("\n:: Creating a New Product ::")  # DISPLAY CREATE A NEW PRODUCT MENU
    print("--------------------------------------")
    new_product_name = input("Please input product name : ")  # ASK USER FOR A NEW PRODUCT NAME
    while True:
        try:
            new_product_rate = float(input("Please input the interest rate for this product : "))  # ASK USER FOR PRODUCT INTEREST RATE
            if new_product_rate < 0:
                print("\nInterest rate cannot be negative.")
                continue
        except ValueError:  # CHECK USER ENTERED A VALID NUMBER
            print("\nInterest rate must be a number.")
            continue
        else:
            break
    # # AFTER USER HAS ENTERED PRODUCT DETAILS
    # # GIVE USER A SUMMARY OF WHAT THEY HAVE ENTERED

    # print("\n===================================================")
    # print("Product Summary")
    # print("===================================================")
    # print("Product Name :", new_product_name)
    # print("Product Rate :", new_product_rate)
    # print("---------------------------------------------------")
    #
    created_product = product_summary(new_product_name, new_product_rate)
    return created_product


def get_confirmation():
    user_confirmation = input("\nPlease confirm the product's details (input 1) to proceed with product creation (or any key to quit) :")
    if user_confirmation == "1":
        return True
    else:
        return False


def view_products(products):
    # SUBMENU HEADING
    print("\n================================================================================")
    print("List of Products")
    print("================================================================================")
    product_num = 1
    # LOOP THROUGH LIST AND DISPLAY EACH SUBLIST ON A NEW LINE
    for product_name, interest_rate in products:
        print("No.", product_num, ":", product_name, "| Product rate :", interest_rate)
        product_num += 1
    print("--------------------------------------------------------------------------------")
    # input("Press enter to continue")
    # manage_products_menu()  # GO BACK TO MANAGE MORTGAGE PRODUCTS SUBMENU


def product_summary(summary_name, summary_rate):
    # AFTER USER HAS ENTERED PRODUCT DETAILS
    # GIVE USER A SUMMARY OF WHAT THEY HAVE ENTERED
    print("\n===================================================")
    print("Product Summary")
    print("===================================================")
    print("Product Name :", summary_name)
    print("Product Rate :", summary_rate)
    print("---------------------------------------------------")

    summary_of_product = [summary_name, summary_rate]
    return summary_of_product

#  --DISPLAY MAIN MENU--
display_main_menu = True
while display_main_menu:
    main_menu()
    main_menu_option = user_menu_choice(3)  # MAIN MENU: GET USER INPUT
    if main_menu_option:  # IF VALID INPUT
        display_main_menu = False  # STOP SHOWING MAIN MENU

    #  --DISPLAY MANAGE MORTGAGE PRODUCTS--
    if main_menu_option == 1:
        display_products_menu = True
        product_list = [["Home Loan Flexi", 2.3], ["Santander Fresh Home Loan", 1.8], ["Barclays First-Time Mortgage", 1.98]]
        while display_products_menu:
            manage_products_menu()
            manage_products_option = user_menu_choice(5)
            if manage_products_option:  # IF VALID INPUT
                display_products_menu = False  # STOP SHOWING MANAGE PRODUCTS MENU

            #  MANAGE PRODUCTS: ADD A NEW PRODUCT
            if manage_products_option == 1:
                new_product = create_product()  # GET INPUT FOR NEW PRODUCT
                confirmation = get_confirmation()
                if confirmation:  # IF CONFIRMED
                    product_list.append(new_product)  # ADD NEW PRODUCT
                    print("\nCreating New Product")
                    print("Generating new product........")
                    print("Generated product name : ", new_product[0])
                    print("Generated product rate", new_product[1])
                    input("Press enter to continue")
                else:
                    pass
                display_products_menu = True

            #  MANAGE PRODUCTS: VIEW A LIST OF PRODUCTS
            elif manage_products_option == 2:
                view_products(product_list)
                input("Press enter to continue")
                display_products_menu = True

            #  MANAGE PRODUCTS: AMEND A PRODUCT
            elif manage_products_option == 3:
                view_products(product_list)
                product_number = int(input("Select the product number to amend : "))
                product_index = product_number - 1
                print("Product name: ", product_list[product_index][0])

                #   USER INPUTS NEW PRODUCT NAME
                user_amended_product_name = input("New product name? (press q/Q to escape): ")
                if user_amended_product_name in ["q", "Q"]:
                    amended_product_name = product_list[product_index][0]


                # USER INPUTS NEW PRODUCT INTEREST RATE
                # amended_product_rate = (input("Please input the interest rate for this product : "))
                while True:
                    user_amended_product_rate = (input("Please input the interest rate for this product : "))
                    try:
                        if user_amended_product_rate in ["q", "Q"]:
                            amended_product_rate = product_list[product_index][1]
                        else:
                            try:
                                amended_product_rate = float(user_amended_product_rate)
                                if amended_product_rate < 0:
                                    print("\nInterest rate cannot be negative.")
                                    continue
                            except ValueError:  # CHECK USER ENTERED A VALID NUMBER
                                print("\nInterest rate must be a number.")
                                continue
                    except ValueError:
                        print("There is an error")
                    else:
                        break

                amended_product = product_summary(amended_product_name, amended_product_rate)
                # Returns [product_name, product_rate]
                confirmation = get_confirmation()
                if confirmation:
                    product_list[product_index] = amended_product
                display_products_menu = True

            # MANAGE PRODUCTS: DELETE A PRODUCT
            elif manage_products_option == 4:
                print("\nThis is where you delete products")

            #  MANAGE PRODUCTS: RETURN TO MAIN MENU
            else:
                display_main_menu = True

    #  --MANAGE MORTGAGE QUOTES--
    elif main_menu_option == 2:
        display_quotes_menu = True
        while display_quotes_menu:
            manage_quotes_menu()
            manage_quotes_option = user_menu_choice(4)
            if manage_quotes_option:
                display_quotes_menu = False

            # MANAGE QUOTES: ADD A NEW QUOTE
            if manage_quotes_option == 1:
                print("You are creating a quote")
                display_quotes_menu = True
            # MANAGE QUOTES: VIEW A LIST OF QUOTES
            elif manage_quotes_option == 2:
                print("You are viewing quotes")
                display_quotes_menu = True
            # MANAGE QUOTES: AMEND A QUOTE
            elif manage_quotes_option == 3:
                print("You are amending quotes")
                display_quotes_menu = True
            # MANAGE QUOTES: RETURN TO MAIN MENU
            else:
                display_main_menu = True

    # MAIN MENU: QUIT
    else:
        print("You exited")
