class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive!")
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance!")
        self.balance -= amount
        print("Withdrawn:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount(1000)

try:
    account.deposit(500)
    account.withdraw(2000)   # This will raise error
except ValueError as e:
    print("Error:", e)

account.check_balance()
