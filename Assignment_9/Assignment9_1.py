import threading
import time

def print1to5():
    print("Thread name:", threading.current_thread().name)
    for i in range(1, 6):
        print(i, end=" ")
    time.sleep(1)
    print() 

def main():
    print("Inside main")

    T1 = threading.Thread(target=print1to5, name="Thread1")
    T2 = threading.Thread(target=print1to5, name="Thread2")
    T3 = threading.Thread(target=print1to5, name="Thread3")
    
    T1.start()
    T1.join()

    T2.start()
    T2.join()

    T3.start()
    T3.join()

if __name__ == "__main__":
    main()