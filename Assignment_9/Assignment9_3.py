import multiprocessing

def Facto(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def main():
    num = [1, 2, 3, 4, 5]

    pool = multiprocessing.Pool()

    result = pool.map(Facto, num)

    pool.close()
    pool.join()

    print("The factorial of the given list is : ", result)

if __name__ == "__main__":
    main()