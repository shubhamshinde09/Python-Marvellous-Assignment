def IsPrime(no):
                    if no <= 1:
                            return False
                    for n in range(2,no):
                            if no % n == 0:
                                return False
                            if no == 2:
                                return True
                    return True

num = int(input("Enter a number you want : "))

if IsPrime(num):
    print("It is a prime number")
else:
    print("It is not a prime number")