Fact = 1

def Factorial(num):
    global Fact

    if(num >= 1):
        Fact = Fact * num
        num  = num - 1
        Factorial(num)
        
    return Fact

def main():
    print("Enter a number you want : ")
    a = int(input())
    ret = Factorial(a)
    print("The factorial of given number is : ",ret)

if __name__ == "__main__":
    main()