#Write a program which accept number from user and print that number of "*" on screen.

def printstar(num):
    print("using for loop")
    i = 0
    for i in range(num):
        print("*" , end = "")
    
    print()  #moves to next line so print next setence on next line
    
    print("using while loop")
    k = 0
    while k < num:
        k = k + 1
        print("*" , end = "")
    
def main():
    no = int(input("enter number:"))
    printstar(no)

if __name__ == "__main__":
    main()
