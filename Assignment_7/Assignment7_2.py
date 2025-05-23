def MapFun(l):
    mappedList = list(map(lambda x: x * 2, l))
    return mappedList

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

    NewList = MapFun(data)
    print("Doubled list : ", NewList)

if __name__ == "__main__":
    main()