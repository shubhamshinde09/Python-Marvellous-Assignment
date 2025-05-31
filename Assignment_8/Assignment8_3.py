import threading

def SumEven(l):
    sum = 0
    for i in range(0,len(l)+1):
        if i % 2 == 0:
            sum = sum + i
    print("The sum of even number from the list : ",sum)

def SumOdd(l):     
    sum = 0
    for i in range(0,len(l)+1):
        if i % 2 != 0:
            sum = sum + i
    print("The sum of odd number from the list : ",sum)

def main():
    print("Inside Main")

    print("Enter number of elements : ")
    size = int(input())

    data = []

    print("Enter the values : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    print("Entered elements are : ")
    for value in data:
        print(value)

    evenlist = threading.Thread(target=SumEven(data))
    oddlist = threading.Thread(target=SumOdd(data))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

    print("end of main")

if __name__ == "__main__":
    main()