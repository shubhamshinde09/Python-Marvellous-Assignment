
CalculateMultiplication = lambda x,y : x * y

def main():
    print("Enter first number : ")
    num1 = int(input())

    print("Enter second number : ")
    num2 = int(input())

    s = CalculateMultiplication(num1,num2)

    print("Multiplication of num1 and num2 is : ",s)

if __name__ == "__main__":
    main()
