import threading

def EvenNum():
    print("Inside EvenNum")
    evenNum = []
    for i in range(30):
        if i % 2 == 0:
            evenNum.append(i)
        if len(evenNum) == 10:
            break
    print("The first 10 Even Numbers are:", evenNum)

def OddNum():
    print("Inside OddNum")
    oddNum = []
    for i in range(30):
        if i % 2 != 0:
            oddNum.append(i)
        if len(oddNum) == 10:
            break
    print("The first 10 Odd Numbers are:", oddNum)

def main():
    print("Inside main")
    T1 = threading.Thread(target=EvenNum)
    T2 = threading.Thread(target=OddNum)
    
    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()