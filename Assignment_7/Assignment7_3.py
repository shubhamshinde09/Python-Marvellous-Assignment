def FilterFun(l):
    filteredList = list(filter(lambda x: x % 2 == 0, l))
    return filteredList

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

    NewList = FilterFun(data)
    print("Even Numbers : ", NewList)

if __name__ == "__main__":
    main()