#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.


def divisibleBy5(value):
    if value % 5 == 0:
        return True
    else:
        return False

def main():
    no = int(input("enter number :"))
    print(divisibleBy5(no))
if __name__ == "__main__":
    main()
