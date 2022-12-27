# APPLICATION MAIN MENU
def print_main_menu():
    print("\n" + "-" * 40 + "\n:: Welcome to Mortgage Quotes System ::" + "\n" + "-" * 40)
    print("1. Manage Mortgage Products")
    print("2. Manage Quotes")
    print("3. Quit")


# MANAGE PRODUCTS MENU
def print_manage_products_menu():
    print("\n" + "-" * 40 + "\n:: Mortgage Products ::" + "\n" + "-" * 40)
    print("1. Add Products")
    print("2. View Products")
    print("3. Amend Products")
    print("4. Delete Product")
    print("5. Return to Main Menu")


# MANAGE QUOTES MENU
def print_manage_quotes_menu():
    print("\n" + "-" * 40 + "\n:: Mortgage Quotes ::" + "\n" + "-" * 40)
    print("1. Create a quote")
    print("2. View a list of quotes")
    print("3. Amend a quote")
    print("4. Return to Main Menu")


def user_menu_choice(number):
    # CHOOSE WHICH MENU SHOULD BE RE-DISPLAYED WHEN VALIDATING INPUT
    def display_current_menu():
        if display_main_menu:
            print_main_menu()
        elif display_products_menu:
            print_manage_products_menu()
        elif display_quotes_menu:
            print_manage_quotes_menu()

    while True:
        try:
            user_menu_option = int(input("\nPlease select a menu option: "))
        except ValueError:
            print("\nEnter a value between 1 and", number)
            display_current_menu()
            continue
        if (user_menu_option > number) or (user_menu_option <= 0):
            print("\nEnter a value between 1 and", number)
            display_current_menu()
            continue
        else:
            return user_menu_option


def create_new_product():
    print("\n:: Creating a New Product ::" + "\n" + "-" * 40)
    # ENTER A PRODUCT NAME
    new_product_name = input("Please input product name : ")
    while True:
        # ENTER A PRODUCT RATE
        new_product_rate = input("Please input the interest rate for this product : ")
        try:
            new_product_rate = float(new_product_rate)
            if new_product_rate < 0:
                print("\nInterest rate cannot be negative.")
            else:
                new_product = [new_product_name, new_product_rate]
                return new_product
        except ValueError:
            print("\nInterest rate must be a number.")
            continue


def product_summary(summary_name, summary_rate):
    print("\n" + "=" * 40)
    print("Product Summary")
    print("=" * 40)
    print("Product Name :", summary_name)
    print("Product Rate :", summary_rate)
    print("-" * 40)


def get_confirmation():
    user_confirmation = input("\nPlease confirm the product's details (input 1) to proceed with product creation (or any key to quit) ")
    if user_confirmation == "1":
        return True
    else:
        return False


def view_products(products):
    print("\n" + "=" * 80 + "\nList of Products" + "\n" + "=" * 80)
    # LOOP THROUGH LIST OF PRODUCTS
    for product in range(len(products)):
        print("No.", product + 1, ": ", end="")
        print(products[product][0], end="")
        print(" | Product rate :", products[product][1])
    print("-" * 80)


def amend_product_details():
    print("\n:: Amend a Product ::" + "\n" + "-" * 40)
    view_products(product_list)
    # USER SELECTS PRODUCT TO CHANGE
    user_product_selection = input("Select the product number to amend : ")
    # CHECK USER INPUTS VALID OPTION
    while (not user_product_selection.isdigit()) or (int(user_product_selection) > len(product_list)) or (int(user_product_selection) == 0):
        print("Invalid input! ", end="")
        user_product_selection = input("Select the product number to amend : ")

    user_product_selection = int(user_product_selection)
    product_to_amend = product_list[user_product_selection - 1]

    # AMEND PRODUCT NAME
    print("Product name : ", product_to_amend[0])
    amended_product_name = input("New product name (press q/Q to escape) : ")
    if (amended_product_name != "q") and (amended_product_name != "Q"):
        product_to_amend[0] = amended_product_name

    # AMEND PRODUCT RATE
    print("Product rate : ", product_to_amend[1])
    while True:
        try:
            amended_product_rate = input("New product rate (press q/Q to escape) : ")
            # IF USER DOESN'T ENTER q/Q
            if (amended_product_rate != "q") and (amended_product_rate != "Q"):
                # CHECK USER HASN'T ENTERED A NEGATIVE NUMBER
                if int(amended_product_rate) < 0:
                    print("Interest rate cannot be negative.")
                # ELSE IF VALID INPUT
                else:
                    try:
                        # UPDATE THE PRODUCT BEING AMENDED
                        product_to_amend[1] = float(amended_product_rate)
                        break
                    except ValueError:
                        print("\nInterest rate must be a number.")
                        break
            else:
                break
        except ValueError:
            print("Interest rate must be a number.")

    product_summary(product_to_amend[0], product_to_amend[1])
    input("Press enter to continue")
    product_list[user_product_selection - 1] = product_to_amend


# **********************************************************************************

# LIST OF PRODUCTS
product_list = [["Home Loan Flexi", 2.3], ["Santander Fresh Home Loan", 1.8], ["Barclays First-Time Mortgage", 1.98]]

# DISPLAY APPLICATION MAIN MENU
display_main_menu = True
while display_main_menu:
    print_main_menu()
    menu_option = user_menu_choice(3)
    if menu_option:
        display_main_menu = False

    # DISPLAY MANAGE PRODUCTS MENU
    if menu_option == 1:
        display_products_menu = True
        while display_products_menu:
            print_manage_products_menu()
            menu_option = user_menu_choice(5)
            if menu_option:
                display_products_menu = False

            # OPTION 1: CREATE A NEW PRODUCT
            if menu_option == 1:
                # CREATE A NEW PRODUCT
                created_product = create_new_product()
                # DISPLAY A SUMMARY OF NEW PRODUCT
                product_summary(created_product[0], created_product[1])
                # CONFIRM THE SUMMARY IS CORRECT
                confirmation = get_confirmation()
                # IF PRODUCT IS CONFIRMED CORRECT -> APPEND TO PRODUCT LIST
                if confirmation:
                    product_list.append(created_product)
                    # INDICATE PRODUCT CREATION TO USER
                    print("\nCreating New Product")
                    print("Generating new product" + "." * 8)
                    print("Generated product name : ", created_product[0])
                    print("Generated product rate", created_product[1])
                    input("Press enter to continue")
                # GO BACK TO MANAGE PRODUCTS MENU
                display_products_menu = True

            # OPTION 2: VIEW PRODUCTS
            elif menu_option == 2:
                view_products(product_list)
                input("Press enter to continue")
                display_products_menu = True

            # OPTION 3: AMEND A PRODUCT
            elif menu_option == 3:
                amend_product_details()
                print("\nafter update")
                view_products(product_list)

            # OPTION 4: DELETE A PRODUCT
            elif menu_option == 4:
                print("This is where you delete products")

            # OPTION 5: RETURN TO MAIN MENU
            else:
                display_main_menu = True

    # DISPLAY MANAGE QUOTES MENU
    elif menu_option == 2:
        display_quotes_menu = True
        while display_quotes_menu:
            print_manage_quotes_menu()
            menu_option = user_menu_choice(4)
            if menu_option:
                display_quotes_menu = False

            # OPTION 1: CREATE A QUOTE
            if menu_option == 1:
                print("This is where you create quotes")

            # OPTION 2: VEW QUOTES
            elif menu_option == 2:
                print("This is where you view quotes")

            # OPTION 3: AMEND QUOTES
            elif menu_option == 3:
                print("This is where you amend quotes")

            # OPTION 4: RETURN TO MAIN MENU
            else:
                display_main_menu = True

    # QUIT THE APPLICATION
    else:
        print("You exited.")
