#Write a program which display first 10 even numbers on screen.


def main():
    print("using for loop and range")
    print("first 10 even number are :")
    for i in range(2,21,2):
        print(i)
    
    print()
    
    print("using while loop")
    print("first 10 even number are :")
    count = 0
    no = 2
    while count < 10 :
        print(no)
        no =  no + 2
        count =  count + 1 
    
    print()
    
    print("using while loop and if ")
    print("first 10 even number are :")
    cnt = 0
    num = 1
    while cnt < 10:
        if num % 2 == 0 :
            print(num)
            cnt = cnt + 1 
        num = num + 1 

if __name__ == "__main__":
    main()
