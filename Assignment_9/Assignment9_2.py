import multiprocessing
import time

def square_numbers(no):
    print("Thread name:", multiprocessing.current_process().name)
    result = []
    for n in no:
        result.append(n * n)
    print("Square of the list",result)
    time.sleep(1)

def main():
    num1 = [1, 2, 3, 4, 5]
    num2 = [6, 7, 8 , 9, 10]

    p1 = multiprocessing.Process(target=square_numbers(num1), name="Process-1")
    p2 = multiprocessing.Process(target=square_numbers(num2), name="Process-2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()