n = 1 

def Display(no):
    global n
    if n <= no:
        print("* " * n)
        n = n + 1
        Display(no)

def main():
    print("Enter a number you want : ")
    num = int(input())
    Display(num)

if __name__ == "__main__":
    main()