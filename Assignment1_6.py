
#Write a program which accept number from user and check whether that number is positive or negative or zero.


def chknum(num):
    if num > 0:
        print("positive number")
    elif num == 0:
        print("number is zero")
    else:
        print("negative number")

def main():
    no = int(input("enter number :"))
    chknum(no)

if __name__ == "__main__":
    main()
