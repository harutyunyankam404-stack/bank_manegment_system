
from account import BankAccount
import json


class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, owner, account_number, balance=0):

        if account_number in self.accounts:
            print("Account already exists!")
            return

        if balance < 0:
            print("Initial balance cannot be negative!")
            return

        account = BankAccount(owner, balance)

        self.accounts[account_number] = account

        print(f"Account created for {owner}")

    def get_account(self, account_number):

        if account_number in self.accounts:
            return self.accounts[account_number]

        print("Account not found!")
        return None

    def show_all_accounts(self):

        if not self.accounts:
            print("No accounts available!")
            return

        for account_number, account in self.accounts.items():

            print(f"Account number: {account_number}")
            print(f"Owner: {account.owner}")
            print(f"Balance: {account.balance} AMD")
            print("-" * 30)

    def delete_account(self, account_number):

        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully!")

        else:
            print("Account not found!")

    def save_to_file(self):

        data = {}

        for account_number, account in self.accounts.items():

            data[account_number] = {
                "owner": account.owner,
                "balance": account.balance,
                "transactions": account.transactions
            }

        try:
            with open("accounts.json", "w", encoding="utf-8") as file:

                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            print("All accounts saved successfully!")

        except OSError as error:
            print("File saving error:", error)

    def load_from_file(self):

        try:
            with open("accounts.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                print("Invalid account data!")
                return

            loaded_accounts = {}

            for account_number, account_data in data.items():

                if not isinstance(account_data, dict):
                    print(f"Invalid data for account {account_number}")
                    continue

                owner = account_data.get("owner")
                balance = account_data.get("balance")
                transactions = account_data.get("transactions", [])

                if not isinstance(owner, str):
                    continue

                if not isinstance(balance, (int, float)) or balance < 0:
                    continue

                if not isinstance(transactions, list):
                    continue

                account = BankAccount(owner, balance)
                account.transactions = transactions

                loaded_accounts[account_number] = account

            self.accounts = loaded_accounts

            print("Accounts loaded successfully!")

        except FileNotFoundError:
            print("File not found! No saved accounts.")

        except json.JSONDecodeError:
            print("JSON file is damaged or invalid!")

        except OSError as error:
            print("File loading error:", error)
