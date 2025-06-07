class Arithmetic:
    def __init__(self, value1, value2):
        self.Value1 = value1
        self.Value2 = value2

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Division by zero is not allowed."

    def Display(self):
        print(f"Value1: {self.Value1}, Value2: {self.Value2}")

# Creating an instance and calling methods
obj = Arithmetic(10, 5)
obj.Display()
print("Addition:", obj.Addition())
print("Subtraction:", obj.Subtraction())
print("Multiplication:", obj.Multiplication())
print("Division:", obj.Division())