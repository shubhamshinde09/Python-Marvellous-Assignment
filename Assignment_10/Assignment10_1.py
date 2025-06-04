
CalculateSquare = lambda No : No ** 2

def main():
    print("Enter a number : ")
    num = int(input())
    s = CalculateSquare(num)

    print("Power of two of given number is : ",s)

if __name__ == "__main__":
    main()