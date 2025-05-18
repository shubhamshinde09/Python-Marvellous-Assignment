def AdditionOfDigits(no):
                    total = 0
                    if no == 0:
                            return 0
                    while no != 0:
                            digit = no % 10
                            total = total + digit
                            no = no // 10
                    return total
                                           
num = int(input("Enter a number you want : "))

a = AdditionOfDigits(num)
print("The addition of digits of the given number is : ",a)