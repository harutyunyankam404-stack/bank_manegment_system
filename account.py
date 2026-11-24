import json
from datetime import datetime

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.transactions = []


    def deposit(self, amount):
      if amount > 0:
        self.__balance += amount

        now = datetime.now()
    
        self.transactions.append(
            f"Deposited: {amount} AMD"
        )

        print("Deposit successful!")
      else:
        print("Amount must be positive!")

    @property
    def balance(self):
        return self.__balance
  
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive!")

        elif amount > self.__balance:
          print("Insufficient funds!")
 
        else:
          self.__balance -= amount
          print(f"{amount} AMD withdrawn successfully!")
        
        now = datetime.now()
        self.transactions.append( f"Withdrawn: {amount} AMD | {now}")

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def save_to_file(self):
        data = {
            "owner": self.owner,
            "balance": self.__balance,
            "transactions": self.transactions
    }

        with open("accounts.json", "w", encoding="utf-8") as file:
          json.dump(data, file, indent=4, ensure_ascii=False)

    print("Account saved successfully!")      

    def load_from_file(self):
        try:
            with open("accounts.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                self.owner = data["owner"]
                self.__balance = data["balance"]
                self.transactions = data["transactions"]

                print("Account loaded successfully!")

        except FileNotFoundError:
            print("File not found!")