from functools import reduce
import primeNum

def FilterFun(l):
    filteredList = list(filter(primeNum.ChkPrime, l))
    print("List after filter : ", filteredList)

    MapFun(filteredList)

def MapFun(l):
    mappedList = list(map(lambda x: x * 2, l))
    print("List after map : ", mappedList)

    ReduceFun(mappedList)    

def ReduceFun(l):
    ret = reduce(lambda x, y: x if x > y else y, l)
    print("Result of reduce : ", ret)

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

    FilterFun(data)

if __name__ == "__main__":
    main()