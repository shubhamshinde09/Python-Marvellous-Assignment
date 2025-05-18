def AdditionOfFactors(factors):
                            addition = 0
                            for i in factors:
                                    addition = addition + i
                            return addition

def Factors(no):
                    fact = []
                    for n in range(1,no):
                            if no % n == 0:
                                fact.append(n)
                    return fact
                         
num = int(input("Enter a number you want : "))

a = Factors(num)
print("The factors of the given number is : ",a)

b = AdditionOfFactors(a)
print("The addition of factors of the given number is : ",b)
