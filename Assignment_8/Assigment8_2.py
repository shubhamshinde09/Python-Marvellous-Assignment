import threading

def SumEvenFactor(no):
    sum = 0
    for i in range(2,no+1,2):
        if no % i == 0:
            sum = sum + i
    print("Addition of  even factors of given number : ",sum)

def SumOddFctor(no):
    sum = 0
    for i in range(1,no+1,2):
        if no % i == 0:    
            sum = sum + i
    print("Addition of odd factors of given number :",sum)

def main():
    print("Demonstration o(f parallel execution")

    evenfactor = threading.Thread(target=SumEvenFactor, args=(12,))
    oddfactor = threading.Thread(target=SumOddFctor, args=(12,))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

    print("exit from main")

if __name__ == "__main__":
    main()