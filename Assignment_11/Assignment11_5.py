def countZero(num):
    if num == 0:
        return 1

    if num < 10:
        return 0  # single-digit number that's not zero

    # If last digit is zero
    if num % 10 == 0:
        return 1 + countZero(num // 10)
    else:
        return countZero(num // 10)

def main():
    print("Enter a number you want : ")
    a = int(input())
    ret = countZero(a)
    print("The count of zeros is : ", ret)

if __name__ == "__main__":
    main()