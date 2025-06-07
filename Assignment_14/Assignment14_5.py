# 5. BankAccount class
class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print(f"Account: {self.account_number}, Name: {self.name}, Balance: {self.balance}")


acc = BankAccount("123456", "Shubham", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display()