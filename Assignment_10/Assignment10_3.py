from functools import reduce

def FilterFun(l):
    filteredList = list(filter(lambda x: 70 <= x <= 90, l))
    print("List after filter : ", filteredList)

    MapFun(filteredList)

def MapFun(l):
    mappedList = list(map(lambda x: x + 10, l))
    print("List after map : ", mappedList)

    ReduceFun(mappedList)    

def ReduceFun(l):
    ret = reduce(lambda x, y: x * y, l)
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