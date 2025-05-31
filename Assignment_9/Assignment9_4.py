import threading
import multiprocessing
import time

def calTotal(args):
    start, end = args
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

def threadTotal(start, end, result):
    total = 0
    for i in range(start, end + 1):
        total += i
    result.append(total)

def main():
    n = 1000

    start_time = time.time()
    total = calTotal((1, n))
    end_time = time.time()
    print("Normal Sum:", total)
    print("Execution time for normal function:", end_time - start_time)

    start_time = time.time()
    mid = n // 2
    result_list = []

    t1 = threading.Thread(target=threadTotal, args=(1, mid, result_list))
    t2 = threading.Thread(target=threadTotal, args=(mid + 1, n, result_list))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    threadtotal = 0
    for i in result_list:
        threadtotal += i

    end_time = time.time()
    print("Thread Sum:", threadtotal)
    print("Execution time for threading:", end_time - start_time)

    start_time = time.time()
    pool = multiprocessing.Pool(processes=2)
    ranges = [(1, mid), (mid + 1, n)]
    results = pool.map(calTotal, ranges)
    pool.close()
    pool.join()

    processSum = 0
    for i in results:
        processSum += i

    end_time = time.time()
    print("Process Sum:", processSum)
    print("Execution time for multiprocessing:", end_time - start_time)

if __name__ == "__main__":
    main()