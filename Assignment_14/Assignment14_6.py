# 6. Calculator class
class Calculator:
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b): return a / b if b != 0 else "Division by zero"


calc = Calculator()
x, y = 20, 5
print("Add:", calc.add(x, y))
print("Sub:", calc.sub(x, y))
print("Mul:", calc.mul(x, y))
print("Div:", calc.div(x, y))