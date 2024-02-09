class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. Current balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeds available balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. Current balance: {self.balance}")
owner = int(input())
account = BankAccount(owner)
amount = int(input())