class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        print(self.balance)

account = BankAccount(100)
account.deposit(50)
account.withdraw(20)
account.check_balance()