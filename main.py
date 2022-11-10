def main_menu():
    print("\n------------------------------------------")
    print(":: Welcome to Mortgage Quotes System ::")
    print("------------------------------------------")
    print("1. Manage Mortgage Products")
    print("2. Manage Quotes")
    print("3. Quit")
    try:
        option = int(input("\nPlease select a menu option: "))
        if (option > 3) or (option < 0):
            print("\nEnter a value between 1 and 3")
            main_menu()
        elif option == 1:
            manage_products_menu()
        elif option == 2:
            manage_quotes_menu()
        else:
            print("You exited")
            exit()
    except ValueError:
        print("\nEnter a value between 1 and 3")
        main_menu()


# MANAGE MORTGAGE PRODUCTS
def manage_products_menu():
    print("\n------------------------------------------")
    print(":: Mortgage Products ::")
    print("------------------------------------------")
    print("1. Add Products")
    print("2. View Products")
    print("3. Amend Products")
    print("4. Delete Product")
    print("5. Return to Main Menu")
    products = [["Home Loan Flexi", 2.3], ["Santander Fresh Home Loan", 1.8], ["Barclays First-Time Mortgage", 1.98]]
    try:
        option = int(input("\nPlease select a menu option: "))
        if (option > 5) or (option < 0):
            print("\nEnter a value between 1 and 5")
            manage_products_menu()
        elif option == 1:
            print(":: Creating a New Product ::")
            print("--------------------------------------")
            new_product_name = input("Please input product name : ")
            try:
                new_product_rate = float(input("Please input the interest rate for this product :"))
            except ValueError:
                print("\nEnter a number")
            print("===================================================")
            print("Product Summary")
            print("===================================================")
            print("Product Name :", new_product_name)
            print("Product Rate :", new_product_rate)
            print("---------------------------------------------------")
            confirmation = input("Please confirm the product's details (input 1) to proceed with product creation (or any key to quit) :")
            if confirmation == 1:
                new_product = new_product_name, new_product_rate
                products.extend(new_product)
                print(products)
            else:
                manage_products_menu()

            # manage_products_menu()
        elif option == 2:
            view_products(products)
        elif option == 3:
            amend_product()
        elif option == 4:
            delete_product()
        else:
            main_menu()
    # IF USER ENTERS SOMETHING UNEXPECTED
    except ValueError:
        print("\nEnter a value between 1 and 5")
        manage_products_menu()


# MANAGE MORTGAGE PRODUCTS SUBMENU FUNCTIONS

# def add_product():


def view_products(existing_products):
    print("\n================================================================================")
    print("List of Products")
    print("================================================================================")
    product_num = 1
    for product, interest_rate in existing_products:
        print("No.", product_num, ":", product, "| Product rate :", interest_rate)
        product_num += 1
    print("--------------------------------------------------------------------------------")
    input("Press enter to continue")


def amend_product():
    print("THIS IS PRODUCT SUB-MENU")


def delete_product():
    print("THIS IS PRODUCT SUB-MENU")


# MANAGE MORTGAGE QUOTES

def manage_quotes_menu():
    print("\n------------------------------------------")
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
