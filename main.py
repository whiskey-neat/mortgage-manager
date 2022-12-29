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
        # GET USER INPUT
        try:
            user_menu_option = int(input("\nPlease select a menu option: "))
        # INPUT VALIDATION AGAINST NON-NUMBER CHARACTERS
        except ValueError:
            print("\nEnter a value between 1 and", number)
            display_current_menu()
            continue
        # VALIDATE NUMBER
        if (user_menu_option > number) or (user_menu_option <= 0):
            print("\nEnter a value between 1 and", number)
            display_current_menu()
            continue
        else:
            return user_menu_option


def create_new_product():
    print("\n:: Creating a New Product ::" + "\n" + "-" * 40)

    # PRODUCT NAME
    new_product_name = input("Please input product name : ")

    # PRODUCT RATE
    while True:
        new_product_rate = input("Please input the interest rate for this product : ")
        try:
            new_product_rate = float(new_product_rate)
            if new_product_rate < 0:
                print("\nInterest rate cannot be negative.")
            else:
                new_product = [new_product_name, new_product_rate]  # IF VALID -> SAVE NEW PRODUCT DETAILS TO VARIABLE
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


def view_quotes(quotes):
    print("\n" + "=" * 80 + "\nList of Quotes" + "\n" + "=" * 80)
    # LOOP THROUGH LIST OF PRODUCTS
    for quote in range(len(quotes)):
        print("No.", quote + 1, )
        print("{:<20} {:^5} {:<20s}".format("Customer name", ":", quotes[quote][0]))
        print("{:<20} {:^5} {:<.2f}".format("Loan amount", ":", quotes[quote][1]))
        print("{:<20} {:^5} {:<20}".format("Loan term", ":", quotes[quote][2]))
        print("{:<20} {:^5} {:<20}".format("Loan product name", ":", quotes[quote][3]))
        print("{:<20} {:^5} {:<20}".format("Loan product rate", ":", quotes[quote][4]))
        print("{:<20} {:^5} {:<.2f}".format("Monthly repayment", ":", quotes[quote][5]))
        print("{:<20} {:^5} {:<.2f}".format("Total repayment", ":", quotes[quote][6]))
        print("-" * 80)


def product_selection(operation):
    # USER SELECTS PRODUCT TO CHANGE
    user_product_selection = input("Select the product number" + operation + " : ")
    # CHECK USER INPUTS VALID OPTION
    while (not user_product_selection.isdigit()) or (int(user_product_selection) > len(product_list)) or (int(user_product_selection) == 0):
        print("Invalid input! ", end="")
        user_product_selection = input("Select the product number" + operation + " : ")
    return int(user_product_selection)


def get_quote_selection():
    user_quote_selection = input("Select the quote number to amend (enter q/Q to escape) : ")
    while True:
        # check if user wants to escape
        if (user_quote_selection == "q") or (user_quote_selection == "Q"):
            return user_quote_selection
        # if user enters a digit, and it is equal to or less than the length of the quote list and more than 0
        elif (user_quote_selection.isdigit()) and (int(user_quote_selection) <= len(user_quote_selection)) and int(user_quote_selection) > 0:
            return user_quote_selection
        else:
            print("Invalid input! ", end="")
            user_quote_selection = input("Select the quote number to amend (enter q/Q to escape) : ")


def amend_product_details():
    # USER SELECTS PRODUCT TO AMEND
    user_product_selection = (product_selection(" to amend"))
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


def amend_quotes(quote_being_amended):
    # AMEND QUOTE NAME
    print("\nCustomer name :", quote_being_amended[0])
    amended_customer_name = input("Input the new customer name (input q/Q to escape) : ")
    if (amended_customer_name != "q") and (amended_customer_name != "Q"):
        quote_being_amended[0] = amended_customer_name

    # AMEND LOAN AMOUNT
    print("\nLoan amount : ", quote_being_amended[1])
    while True:
        amended_loan_amount = input("Input the new loan amount (input q/Q to escape) : ")
        # if user doesn't enter q/Q
        if (amended_loan_amount != "q") and (amended_loan_amount != "Q"):
            # check for negative numerical value
            if int(amended_loan_amount) < 0:
                print("Loan amount cannot be negative.")
            # else the input is valid
            else:
                try:
                    # update the quote with the new loan amount
                    quote_being_amended[1] = float(amended_loan_amount)
                    break
                except ValueError:
                    print("\nLoan amount must be a number.")
                    break
        # if user enters q/Q
        else:
            break

    # AMEND LOAN TERM
    print("\nLoan term : ", quote_being_amended[2])
    while True:
        amended_loan_term_years = input("Input the new loan term in year (input q/Q to escape) : ")
        # if the user doesn't enter q/Q
        if (amended_loan_term_years != "q") and (amended_loan_term_years != "Q"):
            # check user has not entered negative number
            if int(amended_loan_term_years) < 0:
                print("Loan term cannot be negative.")
            # else the input is valid
            else:
                try:
                    # update the selected quote with the new loan term
                    quote_being_amended[2] = int(amended_loan_term_years)
                    break
                except ValueError:
                    print("\nLoan term must be a number.")
                    break
        # if user enters q/Q
        else:
            break

    # AMEND LOAN PRODUCT
    print("\nLoan product name : ", quote_being_amended[3])
    view_products(product_list)

    # SELECT AMENDED PRODUCT FOR QUOTE

    # SELECT NEW PRODUCT OR ESCAPE
    amended_product_selection = input("Select the new product number (input q/Q to escape) : ")
    while True:
        if (amended_product_selection == "q") or (amended_product_selection == "Q"):
            break
        elif (amended_product_selection.isdigit()) and (int(amended_product_selection) <= len(amended_product_selection)) and int(
                amended_product_selection) > 0:
            amended_product = int(amended_product_selection)
            amended_quote_product = product_list[amended_product - 1]

            # SETS AMENDED QUOTE PRODUCT NAME
            quote_being_amended[3] = amended_quote_product[0]
            print("The amended product name is : ", quote_being_amended[3])
            # SETS AMENDED QUOTE PRODUCT RATE
            quote_being_amended[4] = amended_quote_product[1]
            print("The amended product rate is : ", quote_being_amended[4])
            print(type(quote_being_amended[4]))
            break
        else:
            print("Invalid input! ", end="")
            amended_product_selection = input("Select the new product number (input q/Q to escape) : ")

    # CALCULATE VARIABLES NEEDED FOR REPAYMENT FORMULAS
    interest_rate = (quote_being_amended[4] / 100) / 12
    loan_term_months = int(quote_being_amended[2])

    # CALCULATE REPAYMENT VALUES
    monthly_repayment_amount = quote_being_amended[1] * interest_rate * ((1 + interest_rate) ** loan_term_months) / ((1 + interest_rate) **
                                                                                                                     loan_term_months - 1)
    total_repayable_amount = monthly_repayment_amount * loan_term_months

    quote_being_amended[5] = monthly_repayment_amount
    quote_being_amended[6] = total_repayable_amount


def delete_a_product():
    # # USER SELECTS PRODUCT TO DELETE
    # user_product_selection = input("Select the product number to delete : ")
    # # CHECK USER INPUTS VALID OPTION
    # while (not user_product_selection.isdigit()) or (int(user_product_selection) > len(product_list)) or (int(user_product_selection) == 0):
    #     print("Invalid input! ", end="")
    #     user_product_selection = input("Select the product number to amend : ")

    user_product_selection = product_selection(" to delete")
    if user_product_selection <= len(product_list):
        print("You are going to delete : ")
        print("Product name : ", product_list[user_product_selection - 1][0])
        print("Product rate : ", product_list[user_product_selection - 1][1])
        confirm = input("Input c/C to confirm delete (or press enter to skip) : ")

        if (confirm == "c") or (confirm == "C"):
            product_list.pop(user_product_selection - 1)
            print("The record has been deleted!")
            input("Press enter to continue")


def create_new_quote():
    print("\n" + "=" * 40)
    print("Create a Quote")
    print("=" * 40)

    # ENTER A CUSTOMER NAME
    customer_name = input("Please enter customer name : ")

    # ENTER A PRODUCT RATE
    while True:
        loan_amount = input("Please input loan amount : ")
        try:
            loan_amount = float(loan_amount)
            if loan_amount < 0:
                print("\nLoan amount cannot be negative.")
            else:
                break
        except ValueError:
            print("\nLoan amount must be a number.")
            continue

    # ENTER TERM OF LOAN IN YEARS
    while True:
        loan_term_years = input("Please input term of loan in year : ")
        try:
            loan_term_years = int(loan_term_years)
            if loan_term_years < 0:
                print("Loan term cannot be negative amount of time.")
            else:
                break
        except ValueError:
            print("Term of loan must be number of years")

    # VIEW PRODUCTS TO USE FOR QUOTE
    print("\nThere are", len(product_list), "products:")
    view_products(product_list)

    # SELECT WHICH PRODUCT TO USE FOR QUOTE
    user_product_selection = product_selection("")
    quote_product = product_list[user_product_selection - 1]

    # CALCULATE REPAYMENTS OF NEW LOAN
    interest_rate = float((quote_product[1]) / 100) / 12
    loan_term_months = loan_term_years * 12
    monthly_repayment_amount = loan_amount * interest_rate * ((1 + interest_rate) ** loan_term_months) / ((1 + interest_rate) ** loan_term_months - 1)
    total_repayable_amount = monthly_repayment_amount * loan_term_months

    # DISPLAY QUOTE DETAILS TO USER
    print("{:<30} : {:<}".format("Your home loan product name", quote_product[0]))
    print("{:<30} : {:<}".format("Your home loan rate", quote_product[1]))
    print("{:<30} : {:<.2f}".format("Your monthly repayment will be", monthly_repayment_amount))
    print("{:<30} : {:<.2f}".format("Your total repayment will be", total_repayable_amount))
    input("Press enter to continue")

    new_quote_details = [customer_name, loan_amount, loan_term_months, quote_product[0], quote_product[1], monthly_repayment_amount,
                         total_repayable_amount]
    return new_quote_details


# *****************************************************************************

# LIST OF PRODUCTS
product_list = [
    ["Home Loan Flexi", 2.3],
    ["Santander Fresh Home Loan", 1.8],
    ["Barclays First-Time Mortgage", 1.98]
]

# LIST OF QUOTES
quote_list = [
    ["Zairul", 120000, 15, "Home Loan Flexi", 2.3, 500, 160000]
]

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
                print("\n:: Amend a Product ::" + "\n" + "-" * 40)
                view_products(product_list)
                amend_product_details()
                display_products_menu = True

            # OPTION 4: DELETE A PRODUCT
            elif menu_option == 4:
                print("\n:: Delete a Product ::" + "\n" + "-" * 40)
                view_products(product_list)
                delete_a_product()
                display_products_menu = True

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
                created_quote = create_new_quote()
                quote_list.append(created_quote)
                display_quotes_menu = True

            # OPTION 2: VEW QUOTES
            elif menu_option == 2:
                if len(quote_list) == 0:
                    print("\n" + "-" * 30 + "\n  No quotes have been setup" + "\n" + "-" * 30)
                else:
                    view_quotes(quote_list)
                    input("\nPress enter to return to Manage Quotes Menu")
                display_quotes_menu = True

            # OPTION 3: AMEND QUOTES
            elif menu_option == 3:
                print("\n:: Amend a Quote ::" + "\n" + "-" * 40)
                view_quotes(quote_list)
                quote_selection = get_quote_selection()
                # if user does not want to skip
                if (quote_selection != "q") and (quote_selection != "Q"):
                    # convert selected quote number to quote_list index number
                    quote_to_amend = quote_list[int(quote_selection) - 1]
                    # amend the selected quote
                    amend_quotes(quote_to_amend)
                input("Press enter to continue: ")
                display_quotes_menu = True

            # OPTION 4: RETURN TO MAIN MENU
            else:
                display_main_menu = True

    # QUIT THE APPLICATION
    else:
        print("You exited.")
