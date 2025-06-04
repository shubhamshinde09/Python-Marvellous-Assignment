i = 1

def Display(no):                                                                                   
    global i
    if(i <= no):
        print(i,end=" ")
        i = i + 1
        Display(no)

def main():
    print("Enter a number you want : ")
    a = int(input())
    Display(a)

if __name__ == "__main__":
    main()