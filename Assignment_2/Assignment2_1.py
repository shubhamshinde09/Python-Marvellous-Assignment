import Arithmetic

print("Enter first num1: ")
num1 = int(input())

print("Enter second num2: ")
num2 = int(input())

addition = Arithmetic.Add(num1,num2)
print("Addition of num1 and num2 is ",addition)

subtraction = Arithmetic.Sub(num1,num2)
print("Subtraction of num1 and num2 is ",subtraction) 

multiplication = Arithmetic.Mul(num1,num2)
print("Multiplication of num1 and num2 is ",multiplication) 

division = Arithmetic.Div(num1,num2)
print("Dultiplication of num1 and num2 is ",division) 