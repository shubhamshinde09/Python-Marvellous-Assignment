def Display(no):
    for i in range(no):
        for j in range(i+1):        
            print("*",end=" ")
        print()

def main():
    print("Enter a number you want : ")
    num = int(input())
    Display(num)

if __name__ == "__main__":
    main()