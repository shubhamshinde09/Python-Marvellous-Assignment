#  2. BankAccount Class Program
class BankAccount:
    ROI = 10.5  # Class variable (Rate of Interest)

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Deposit(self, value):
        self.Amount += value

    def Withdraw(self, value):
        if value <= self.Amount:
            self.Amount -= value
        else:
            print("Insufficient balance!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest on current amount ({self.Amount}) at ROI {BankAccount.ROI}% is: {interest}")

    def Display(self):
        print(f"Name: {self.Name}, Amount: {self.Amount}")


# Creating objects and testing methods
acc1 = BankAccount("Shubham", 1000)
acc1.Deposit(500)
acc1.Withdraw(300)
acc1.CalculateInterest()
acc1.Display()

print("----")

acc2 = BankAccount("Anjali", 2000)
acc2.Deposit(1000)
acc2.Withdraw(500)
acc2.CalculateInterest()
acc2.Display()
