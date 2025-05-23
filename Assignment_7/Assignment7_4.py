from functools import reduce

def ReduceFun(l):
        ret = reduce(lambda x, y: x * y, l)
        return ret

def main():
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

    NewList = ReduceFun(data)
    print("Product : ", NewList)

if __name__ == "__main__":
    main()