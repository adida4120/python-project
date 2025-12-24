import random


def create_account(accounts1):
    """
            This function takes a dictionary of accounts (accounts1) and creates a new account.
            It Performs verification of user inputs, including checking the ID, names, date of birth, and email address.
            Parameters:
            accounts1 (dict): A dictionary of accounts in the format {key: value}.
            Returns:
            tuple: A tuple including the details of the new created account and the dictionary with all accounts .
            """
    while True:
        # proper checks of the ID, including checking whether it already exists in the system
        try:
            id1 = input("Enter your id:")
            if len(id1) < 9:
                print("The ID must be at least 9 characters long. Please try again.")
                continue
            id1 = int(id1)
            if id1 > 0:
                id_exists = False
                for account in accounts1.values():
                    if account['id'] == id1:
                        id_exists = True
                        print("This ID already exists in the system. Please try again.")
                        break
                if id_exists:
                    continue
                else:
                    break
            else:
                # Handle invalid ID
                print("You've entered a negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    while True:
        first_name = input("Enter first name:")
        # Validate the first name using ASCII value
        valid_input = True
        for char in first_name:
            if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or ord(char) == 32):
                valid_input = False
                break
        if valid_input:
            break
        else:
            # print an error message first name
            print("Invalid input. Please enter letters or spaces only for the first name.")

    while True:
        # Validate the last name using ASCII value
        last_name = input("Enter last name:")
        valid_input = True
        for char in last_name:
            if not ((65 <= ord(char) <= 90) or (97 <= ord(char) <= 122) or ord(char) == 32):
                valid_input = False
                break
        if valid_input:
            break
        else:
            # print an error message first name
            print("Invalid input. Please enter letters and spaces only for the last name.")

    while True:
        # Validate date of birth
        birth_day_list = input("Enter birth day (dd/mm/yyyy):")
        if check_bd(birth_day_list):
            break

    while True:
        # Validate the email
        email = input("Enter email:")
        if check_email(email):
            break
        else:
            # print an error message for invalid email
            print("Invalid email. Please enter again.")
    # Generate a random account number
    number_account = random.randint(1000, 9999)
    account_key = f"account_{id1}"
    # Add the new account to the accounts dictionary
    accounts1[account_key] = {'id': id1, 'first_name': first_name, 'last_name': last_name,
                              'birth_day': birth_day_list, 'email': email,
                              'number_account': number_account, 'total_balance_in_the_bank': 0}
    print("Account successfully created!")
    print("Account details:")
    print(accounts1[account_key])
    return accounts1[account_key], accounts1


def check_bd(birth_day_list):
    """
        Checks if the provided date of birth is valid.

        Parameters:
        birth_day_list (str): A string representing the date of birth in the format 'dd/mm/yyyy'.

        Returns:
        bool: True if the date of birth is valid, False if not.
        """
    # Split the date of birth string into day, month, and year
    birth_day_list = birth_day_list.split("/")
    if len(birth_day_list) != 3:
        print("invalid date of birth, please enter again with slash (/)!")
        return False
    try:
        # Checking that the user is more than 16 years old
        if (1 <= int(birth_day_list[0]) <= 31 and 1 <= int(birth_day_list[1]) <= 12 and
                2008 >= int(birth_day_list[2]) >= 1900):
            return True
        else:
            print("invalid date of birth")
            return False
    except ValueError:
        # Handle invalid date of birth

        print("invalid date of birth")
        return False


pass


def check_email(email):
    """
            Checks if the given email address is valid.

            Parameters:
            email (str): The email address to be checked.

            Returns:
            bool: True if the email address is valid, False otherwise.
            """
    if '@' in email and '.' in email:
        # Checking if '@' is not the first character
        if email.index('@') > 0:
            # Checking if the email ends with 'com.'
            if email.lower().endswith('.com'):
                return True
    return False


def deposit_money(accounts1):
    """
           Deposits money into a bank account.

           Parameters:
           accounts1 (dict): A dictionary including the account information.

           Returns:
           None
           """
    # asking form the user deposit amount and account number
    deposit_amount1 = int(input("how much money would you like to deposit?"))
    number_account1 = int(input("please enter your account number:"))
    # Check if the account number exists in the dictionary.
    for account_key, account_info in accounts1.items():
        # Update the total balance in the bank account.
        if account_info['number_account'] == number_account1:
            # Print deposit confirmation and updated account details
            account_info["total_balance_in_the_bank"] += deposit_amount1
            print("Deposit accepted")
            print("Account number", number_account1)
            print("ID number", account_info['id'])
            print("Updated balance in the bank", account_info["total_balance_in_the_bank"])
            return
    # If the account number is not found ,print an error message.
    print("The account does not exist")


pass


def withdraw_money(accounts1):
    """
            Withdraws money from a bank account.

            Parameters:
            accounts1 (dict): A dictionary containing account information.

            Returns:
            None
            """
    # asking form the user withdraw amount and account number
    withdrawal_amount1 = int(input("How much money would you like to withdraw?"))
    number_account1 = int(input("Please enter your account number:"))
    # Authenticate user and check if the account number exists
    if authenticate_user(accounts1, number_account1):
        for account_key, account_info in accounts1.items():
            if account_info['number_account'] == number_account1:
                # Check if withdrawal amount is in the allowed limit
                if account_info["total_balance_in_the_bank"] - withdrawal_amount1 >= -1000:
                    # Update total balance in the bank account
                    account_info["total_balance_in_the_bank"] -= withdrawal_amount1
                    # Print withdrawal confirmation and updated account details
                    print("Withdrawal successful")
                    print("Account number:", number_account1)
                    print("ID number:", account_info['id'])
                    print("Updated balance in the bank:", account_info["total_balance_in_the_bank"])
                    return
                else:
                    # If withdrawal amount exceeds the allowed limit, print an error message
                    print("Withdrawal amount exceeds the allowed limit (up to -1000)")
                    return
                    # If the account number is not found in the dictionary, print an error message
        print("Account not found")
    else:
        print("Authentication failed")


def check_balance(accounts1):
    """
       Checks the balance and account details for a given account number.

       Parameters:
       accounts1 (dict): A dictionary containing account information.

       Returns:
       None
       """
    # asking the user to enter the account number
    number_account1 = int(input("please enter your account number : "))
    # Check if the input is an integer
    if isinstance(number_account1, int):
        # find the account with the given account number
        for account_key, account_info in accounts1.items():
            # Check if the account number matches
            if 'number_account' in account_info and account_info['number_account'] == number_account1:
                # Print account details including the balance
                print("here is your account details:")
                print("update balance in your account", account_info["total_balance_in_the_bank"])
                print("name: ", account_info['first_name'])
                print("last name:", account_info["last_name"])
                print("id:", account_info["id"])
                print(" birth date:", account_info["birth_day"])
                print("email:", account_info["email"])

                return
                # If the account number is not found in the dictionary, print an error message
    print("The account does not exist in the system")


def display_all_accounts(accounts1):
    """
       Displays details of all accounts in the provided dictionary.

       Parameters:
       accounts1 (dict): A dictionary containing account information.

       Returns:
       None
       """
    if not accounts1:
        # Check if the dictionary is empty
        print("No accounts to display.")
        return
    # checking over the accounts dictionary and print details for each account
    for account_key, account_info in accounts1.items():
        print(
            f"Account Number: {account_info['number_account']}, Name: {account_info['first_name']} "
            f"{account_info['last_name']}"f", Balance: {account_info['total_balance_in_the_bank']}")


pass


def close_account(accounts1):
    """
       Closes a bank account.

       Parameters:
       accounts1 (dict): A dictionary containing account information.

       Returns:
       None
       """
    try:
        number_account1 = int(input("Please enter the account number to close: "))
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Invalid input. Please enter a valid account number.")
        return
    # Authenticate the user with the provided account number
    if authenticate_user(accounts1, number_account1):
        for account_key, account_info in list(accounts1.items()):
            if account_info['number_account'] == number_account1:
                # Check if the account has a positive balance
                if account_info["total_balance_in_the_bank"] > 0:
                    print(f"Balance amount is: {account_info['total_balance_in_the_bank']}")
                del accounts1[account_key]
                # Remove the account from the dictionary
                print("Your account has been successfully closed.")
                return
        print("Account number does not exist.")
        # If the account number is not found in the dictionary, print an error message
    else:
        print("Authentication failed, account closure cannot be proceeded.")
        # If authentication fails, print an error message


def total_bank_balance(accounts1):
    """
        Calculates the total balance of all accounts in the bank.

        Parameters:
        accounts1 (dict): A dictionary containing account information.

        Returns:
        None
        """
    if not accounts1:
        # Check if the dictionary is empty
        print("there are no customers in the bank at the moment")
        return
    # Calculate the total balance by summing up the balances of all accounts
    total_balance = sum(account_info['total_balance_in_the_bank'] for account_info in accounts1.values())
    # Print the total balance
    print(f"the total balance in the bank is: {total_balance}")


pass


def authenticate_user(accounts1, number_account1):
    """
        Authenticates a user based on their account number.

        Parameters:
        accounts1 (dict): A dictionary containing account information.
        number_account1 (int): The account number to authenticate.

        Returns:
        bool: True if the account is authenticated or False if not .
        """
    # checking over the accounts dictionary to find the account with the given account number
    for account_key, account_info in accounts1.items():
        if account_info['number_account'] == number_account1:
            return True
    # If the account number is not found in the dictionary, print an error message
    print("this account number is not authenticate ")
    return False


def menu():
    """
        Displays the Bank Management System menu and ask the user for their choice.

        Returns:
        str: The user's choice from the menu (as a string).
        """
    print("Bank Management System Menu:")
    print("1. Create a new account")
    print("2. Deposit money into an account")
    print("3. Withdraw money from an account")
    print("4. Check the balance of an account")
    print("5. Close an account")
    print("6. Display all account holders")
    print("7. Check the total balance in the bank")
    print("8. Exit the system")
    # return the choice of the user
    return input("Enter your choice (1-8): ")


def main():
    """
        Main function for the Bank Management System.

        Returns:
        None
        """
    accounts = {}
    while True:
        # Get user's choice from the menu
        choice = menu()
        # Use match case to handle user's choice
        match choice:
            case '1':
                # Create a new account
                create_account(accounts)
            case '2':
                # Deposit money into an account
                deposit_money(accounts)
            case '3':
                # Withdraw money from an account
                withdraw_money(accounts)
            case '4':
                # Check the balance of an account
                check_balance(accounts)
            case '5':
                # Close an account
                close_account(accounts)
            case '6':
                # Display all account holders
                display_all_accounts(accounts)
            case '7':
                # Check the total balance in the bank
                total_bank_balance(accounts)
            case '8':
                # Exit the system
                print("Exiting the system")
                break
            case _:
                # Handle invalid choice
                print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == '__main__':
    main()
