import threading
import os

def sCapital(n):
    print("PID of sCapital is : ",os.getpid())
    print("Name of Process Thread is  : ",threading.current_thread().name)
    count = 0
    for i in n:
        if i.isupper():
            count = count + 1  
    print("The number of capital character is : ",count)

def sSmall(n):
    print("PID of sSmall is : ",os.getpid())
    print("Name of Process Thread is  : ",threading.current_thread().name)
    count = 0
    for i in n:
        if i.islower():
            count = count + 1  
    print("The number of small character is : ",count)

def sDigit(n):
    print("PID of sDigit is : ",os.getpid())
    print("Name of Process Thread is  : ",threading.current_thread().name)
    count = 0
    for i in n:
        if i.isdigit():
            count = count + 1  
    print("The number of digit is : ",count)
        
def main():
    print("Enter a string : ")
    string = input()

    small = threading.Thread(target=sCapital, args = (string,), name="CapitalThread")
    capital = threading.Thread(target=sSmall, args = (string,), name="SmallThread")
    digit = threading.Thread(target=sDigit, args = (string,), name="DigitThread")

    small.start()
    small.join()

    capital.start()
    capital.join()

    digit.start()
    digit.join()

    print("exit from main")

if __name__ == "__main__":
    main()