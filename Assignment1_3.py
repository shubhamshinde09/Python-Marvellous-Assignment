
# which accepts two numbers from user and return addition of that two numbers.
#Write a program which contains one function named as Add() 


def Add(value1,value2):
    result = value1 + value2
    return result

def main():
    no1 = int(input("Enter first Number:"))
    no2 = int(input("Enter second Number:"))
    ans = Add(no1,no2)
    print("Addition is :",ans)

if __name__ == "__main__":
    main()
