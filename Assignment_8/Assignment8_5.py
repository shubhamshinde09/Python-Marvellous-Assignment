import threading

def StartToEnd(n):
    print("Print Start to End")
    for i in range(1,n+1):        
        print(i , end=" ")
    print()

def EndTostart(n):
    print("Print End to Start")
    for i in range(n,0,-1):        
        print(i , end=" ")
    print()
        
def main():
    print("Demonstration of parallel execution")

    thread1 = threading.Thread(target=StartToEnd, args = (50,))
    thread2 = threading.Thread(target=EndTostart, args = (50,))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    print("exit from main")

if __name__ == "__main__":
    main()