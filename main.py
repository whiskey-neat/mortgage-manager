def mortgage_manager_main():
    while True:
        # display the application main menu
        print("\n" + "-" * 40 + "\n:: Welcome to Mortgage Quotes System ::" + "\n" + "-" * 40)
        print("1. Manage Mortgage Products")
        print("2. Manage Quotes")
        print("3. Exit")

        menu_option = get_menu_option(3)

        if menu_option:
            break

    # go to appropriate submenu or exit
    if menu_option == 1:
        manage_products()
    elif menu_option == 2:
        manage_quotes()
    else:
        print("You exited.")


def get_menu_option(number):
    # # user chooses menu option
    option = input("\nPlease select a menu option: ")

    # check the option is valid
    if option.isdigit() and 1 <= int(option) <= number:
        # input is valid and turn to integer
        return int(option)
    else:
        # input is invalid. Display an error message and continue the loop
        print("\nPlease enter a value between 1 and", number)


# FUNCTIONS: MANAGING PRODUCTS

def manage_products():
    while True:
        # display the manage products menu
        print("\n" + "-" * 40 + "\n:: Mortgage Products ::" + "\n" + "-" * 40)
        print("1. Add Products")
        print("2. View Products")
        print("3. Amend Products")
        print("4. Delete Products")
        print("5. Return to Main Menu")

        menu_option = get_menu_option(5)

        if menu_option:
            break

    # go to selected option
    if menu_option == 1:
        add_products()
    elif menu_option == 2:
        view_products(product_list)
        input("Press enter to continue: ")
        # return to mortgage products menu
        manage_products()
    elif menu_option == 3:
        amend_products()
    elif menu_option == 4:
        delete_products()
    else:
        # return to main menu
        mortgage_manager_main()


def display_product_summary(summary_name, summary_rate):
    print("\n" + "=" * 40)
    print("Product Summary")
    print("=" * 40)
    print("Product Name :", summary_name)
    print("Product Rate :", summary_rate)
    print("-" * 40)


def add_products():
    print("\n:: Creating a New Product ::" + "\n" + "-" * 40)

    # product name
    product_name = input("Please input product name : ")

    # product rate
    while True:
        product_rate = input("Please input the interest rate for this product : ")

        if product_rate.isdigit():
            # product details are valid so can be stored
            new_product = [product_name, float(product_rate)]

            display_product_summary(new_product[0], new_product[1])

            # ask user whether they want to confirm creation or escape
            confirmation = input("\nPlease confirm the product's details (input 1) to proceed with product creation (or any key to quit): ")
            if confirmation == "1":
                # add the new product to the list of products
                product_list.append(new_product)
                # notify the user that the new product has been added
                print("\nCreating New Product")
                print("Generating new product" + "." * 8)
                print("Generated product name : ", new_product[0])
                print("Generated product rate : ", new_product[1])
                input("Press enter to continue")
                break
            else:
                break
        else:
            # product rate is invalid so display error message and continue loop
            print("Interest rate must be a number.\n")

    # return to manage products menu
    manage_products()


def view_products(products):
    print("\n" + "=" * 80 + "\nList of Products" + "\n" + "=" * 80)
    # loop through list of products
    for product in range(len(products)):
        print("No.", product + 1, ": ", end="")
        print(products[product][0], end="")
        print(" | Product rate :", products[product][1])
    print("-" * 80)


def get_product_selection(operation):
    while True:
        product_selection = input("Select the product number to " + operation + " : ")
        # check user enters valid product number
        if (not product_selection.isdigit()) or (int(product_selection) > len(product_list) or int(product_selection) == 0):
            # user input is invalid: print an error message and continue the loop
            print("Invalid input! ", end="")
        else:
            return int(product_selection)


def amend_products():
    print("\n:: Amend a Product ::" + "\n" + "-" * 40)
    view_products(product_list)

    # select product number to amend
    product = get_product_selection("amend")

    # select product from product index
    product_to_amend = product_list[product - 1]

    # amend product name
    print("\nProduct name : ", product_to_amend[0])
    product_name = input("New product name (press q/Q to escape) : ")
    if (product_name != "q") and (product_name != "Q"):
        # store the new product name
        product_to_amend[0] = product_name

    # amend product rate
    print("\nProduct rate : ", product_to_amend[1])
    while True:
        product_rate = input("New product rate (press q/Q to escape) : ")
        # if user doesn't escape
        if (product_rate != "q") and (product_rate != "Q"):
            try:
                # try to store new product rate
                product_to_amend[1] = float(product_rate)
                break
            except ValueError:
                print("Interest rate must be a number")
        else:
            break

    display_product_summary(product_to_amend[0], product_to_amend[1])
    input("Press enter to continue ")

    # save the amended details to the product list
    product_list[product - 1] = product_to_amend

    # return to manage products menu
    manage_products()


def delete_products():
    print("\n:: Delete a Product ::" + "\n" + "-" * 40)
    # display products to select
    view_products(product_list)

    # product_number = int(get_product_selection("delete"))
    # select product number to delete
    while True:
        product_selection = input("Select the product number to delete (enter q/Q to escape) : ")
        # if user wants to escape
        if (product_selection == "q") or (product_selection == "Q"):
            break
        # user input is valid
        elif (product_selection.isdigit()) and (int(product_selection) <= len(product_list)) and int(product_selection) > 0:
            break
        # user input is invalid
        else:
            print("Invalid input! ", end="")

    # if user does not escape
    if (product_selection != "q") and (product_selection != "Q"):

        if int(product_selection) <= len(product_list):
            product = int(product_selection) - 1
            print("Your are going to delete : ")
            print("Product name : ", product_list[product][0])
            print("Product rate : ", product_list[product][1])
            confirm = input("Input c/C to confirm delete (or press enter to skip) : ")

            # delete product if user confirms
            if (confirm == "c") or (confirm == "C"):
                product_list.pop(product)
                print("The record has been deleted!")
                input("Press enter to continue")

    manage_products()


# FUNCTIONS: MANAGING QUOTES

def manage_quotes():
    while True:
        # display the manage products menu
        print("\n" + "-" * 40 + "\n:: Mortgage Quotes ::" + "\n" + "-" * 40)
        print("1. Create a quote")
        print("2. View a list of quotes")
        print("3. Amend a quote")
        print("4. Return to Main Menu")

        menu_option = get_menu_option(4)

        # if input is valid break loop
        if menu_option:
            break

    # go to selected option
    if menu_option == 1:
        add_quotes()
    elif menu_option == 2:
        # if there are no quotes
        if len(quote_list) == 0:
            print("\n" + "-" * 30 + "\n  No quotes have been set up\n" + "-" * 30)
        else:
            view_quotes(quote_list)
            input("Press enter to continue: ")
        # return to mortgage products menu
        manage_quotes()
    elif menu_option == 3:
        amend_quotes()
    else:
        # return to main menu
        mortgage_manager_main()


def add_quotes():
    # print heading
    print("\n" + "=" * 40 + "\nCreate a Quote\n" + "=" * 40)

    # customer name
    customer_name = input("Please enter customer name : ")

    # loan amount
    while True:
        loan_amount = input("Please input loan amount : ")

        if loan_amount.isdigit() and int(loan_amount) > 0:
            loan_amount = float(loan_amount)
            break
        else:
            print("Loan amount must be a positive number.")

    # loan term
    while True:
        loan_term_years = input("Please input term of loan in years : ")

        if loan_term_years.isdigit() and int(loan_term_years) > 0:
            loan_term_years = int(loan_term_years)
            break
        else:
            print("Loan term must be a positive number.")

    # loan product
    print("\nThere are", len(product_list), "products:")
    view_products(product_list)
    # select product number to use
    product = get_product_selection("use")
    # select product from product index
    quote_product = product_list[product - 1]

    # conversions for repayments
    interest_rate = float((quote_product[1]) / 100) / 12
    loan_term_months = loan_term_years * 12
    # calculate repayments
    monthly_repayment_amount = loan_amount * interest_rate * ((1 + interest_rate) ** loan_term_months) / ((1 + interest_rate) ** loan_term_months - 1)
    total_repayable_amount = monthly_repayment_amount * loan_term_months

    # store quote details
    quote_details = [customer_name, loan_amount, loan_term_months, quote_product[0], quote_product[1], monthly_repayment_amount, total_repayable_amount]
    quote_list.append(quote_details)

    # display quote details
    print("{:<30} : {:<}".format("Your home loan product name", quote_product[0]))
    print("{:<30} : {:<}".format("Your home loan rate", quote_product[1]))
    print("{:<30} : {:<.2f}".format("Your monthly repayment will be", monthly_repayment_amount))
    print("{:<30} : {:<.2f}".format("Your total repayment will be", total_repayable_amount))
    input("Press enter to continue")

    # return to manage quotes menu
    manage_quotes()


def view_quotes(quotes):
    print("\n" + "=" * 80 + "\nList of Quotes" + "\n" + "=" * 80)
    # LOOP THROUGH LIST OF QUOTES
    for quote in range(len(quotes)):
        print("No.", quote + 1, )
        print("{:<20} {:^5} {}".format("Customer name", ":", quotes[quote][0]))
        print("{:<20} {:^5} {:<.2f}".format("Loan amount", ":", quotes[quote][1]))
        print("{:<20} {:^5} {} months ({:<.1f} years)".format("Loan term", ":", quotes[quote][2], quotes[quote][2] / 12))
        print("{:<20} {:^5} {}".format("Loan product name", ":", quotes[quote][3]))
        print("{:<20} {:^5} {}".format("Loan product rate", ":", quotes[quote][4]))
        print("{:<20} {:^5} {:<.2f}".format("Monthly repayment", ":", quotes[quote][5]))
        print("{:<20} {:^5} {:<.2f}".format("Total repayment", ":", quotes[quote][6]))
        print("-" * 80)


def get_quote_selection():
    while True:
        quote_selection = input("Select the quote number to amend (enter q/Q to escape) : ")
        # check if user wants to escape
        if (quote_selection == "q") or (quote_selection == "Q"):
            return quote_selection
        # if user enters a digit, and it is equal to or less than the length of the quote list and more than 0
        elif (quote_selection.isdigit()) and (int(quote_selection) <= len(quote_list)) and int(quote_selection) > 0:
            return quote_selection
        else:
            print("Invalid input! ", end="")


def amend_quotes():
    print("\n:: Amend a Quote ::" + "\n" + "-" * 40)
    view_quotes(quote_list)

    # select quote number to amend
    quote = get_quote_selection()

    if (quote != "q") and (quote != "Q"):
        # select quote from quote index
        quote_to_amend = quote_list[int(quote) - 1]

        # amend customer name
        print("\nCustomer name :", quote_to_amend[0])
        customer_name = input("Input the new customer name (input q/Q to escape) : ")
        if (customer_name != "q") and (customer_name != "Q"):
            quote_to_amend[0] = customer_name

        # amend loan amount
        print("\nLoan amount : ", quote_to_amend[1])
        while True:
            loan_amount = input("Input the new loan amount (input q/Q to escape) : ")

            if (loan_amount == "q") or (loan_amount == "Q"):
                break
            elif loan_amount.isdigit() and int(loan_amount) > 0:
                quote_to_amend[1] = float(loan_amount)
                break
            else:
                print("Loan amount must be a positive number")

        # amend loan term
        print("\nLoan term : ", quote_to_amend[2], " months", "({:<.1f} years)".format(quote_to_amend[2] / 12))
        while True:
            loan_term_years = input("Input the new loan term in years (input q/Q to escape) : ")

            if (loan_term_years == "q") or (loan_term_years == "Q"):
                break
            elif loan_term_years.isdigit() and int(loan_term_years) > 0:
                quote_to_amend[2] = int(loan_term_years) * 12
                break
            else:
                print("Loan term must be a positive number")

        # amend loan product
        print("\nLoan product name : ", quote_to_amend[3])
        view_products(product_list)
        while True:
            # select new loan product or allow the user to escape
            product_selection = input("Select the new product number (input q/Q to escape) : ")
            if (product_selection == "q") or (product_selection == "Q"):
                break
            # if user enters invalid number
            elif (not product_selection.isdigit()) or (int(product_selection) > len(product_list) or int(product_selection) == 0):
                print("Invalid input! ", end="")
            else:
                quote_product = product_list[int(product_selection) - 1]

                # set product name
                quote_to_amend[3] = quote_product[0]
                print("The amended product name is : ", quote_to_amend[3])
                # set product rate
                quote_to_amend[4] = quote_product[1]
                print("The amended product rate is : ", quote_to_amend[4])
                break

        # amend repayment figures
        interest_rate = (quote_to_amend[4] / 100) / 12
        loan_term_months = (quote_to_amend[2])
        monthly_repayment_amount = quote_to_amend[1] * interest_rate * ((1 + interest_rate) ** loan_term_months) / ((1 + interest_rate) ** loan_term_months - 1)
        total_repayable_amount = monthly_repayment_amount * loan_term_months

        # store repayment values
        quote_to_amend[5] = monthly_repayment_amount
        quote_to_amend[6] = total_repayable_amount
        input("Press enter to continue ")
    manage_quotes()


# ----------------------------------------
#               MAIN PROGRAM
# ----------------------------------------

# list of products
product_list = [
    ["Home Loan Flexi", 2.3],
    ["Santander Fresh Home Loan", 1.8],
    ["Barclays First-Time Mortgage", 1.98]
]

# list of quotes
quote_list = [
    ["Zairul", 120000, 15, "Home Loan Flexi", 2.3, 500, 160000]
]

mortgage_manager_main()
