def SumOfDigit(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + SumOfDigit(num // 10)

def main():
    print("Enter a number you want : ")
    a = int(input())
    ret = SumOfDigit(a)
    print("The sum of digits is : ", ret)

if __name__ == "__main__":
    main()