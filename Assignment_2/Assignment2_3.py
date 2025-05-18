def Factorial(no):
                    fact = 1
                    for n in range(no , 0, -1):
                            fact = fact * n
                    return fact
                            
num = int(input("Enter a number you want : "))

a = Factorial(num)
print("The factorial of the given number is : ",a)