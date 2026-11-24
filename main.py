
from bank import Bank


bank = Bank("Armenian Bank")

# Բեռնում ենք նախկինում պահպանված հաշիվները
bank.load_from_file()


while True:

    print("\n========== ARMENIAN BANK ==========")

    print("1. Create account")
    print("2. Show all accounts")
    print("3. Find account")
    print("4. Deposit money")
    print("5. Withdraw money")
    print("6. Show transaction history")
    print("7. Delete account")
    print("8. Save accounts")
    print("9. Exit")

    print("===================================")

    choice = input("Choose an option: ")

    if choice == "1":

        owner = input("Enter owner name: ")
        account_number = input("Enter account number: ")

        try:
            balance = float(input("Enter initial balance: "))

            bank.create_account(
                owner,
                account_number,
                balance
            )

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "2":

        bank.show_all_accounts()

    elif choice == "3":

        account_number = input("Enter account number: ")

        account = bank.get_account(account_number)

        if account:
            print("Owner:", account.owner)
            print("Balance:", account.balance, "AMD")

    elif choice == "4":

        account_number = input("Enter account number: ")

        account = bank.get_account(account_number)

        if account:
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "5":

        account_number = input("Enter account number: ")

        account = bank.get_account(account_number)

        if account:
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "6":

        account_number = input("Enter account number: ")

        account = bank.get_account(account_number)

        if account:
            account.show_transactions()

    elif choice == "7":

        account_number = input("Enter account number: ")

        bank.delete_account(account_number)

    elif choice == "8":

        bank.save_to_file()

    elif choice == "9":

        bank.save_to_file()

        print("Thank you for using Armenian Bank!")
        break

    else:

        print("Invalid choice! Please try again.")
