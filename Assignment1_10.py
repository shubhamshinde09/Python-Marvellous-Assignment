#Write a program which accept name from user and display length of its name.

def chklen(username):
    print("using len()")
    lenght = 0
    lenght = len(username)
    print("length of name is :",lenght)
    
    print()
    
    print("using for loop")
    length1 = 0
    for i in username:
        length1 = length1 + 1
    print("length of name is :",length1)
    
    print()

    print("using while loop")
    leng = 0
    k = 0
    while k < len(username):
        leng = leng + 1
        k = k + 1
    print("length of name is :",leng)

 

def main():
    uname = input("enter name :")

    chklen(uname)
    
if __name__ == "__main__":
    main()
