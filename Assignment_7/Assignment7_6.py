import CheckPrime

def ChkPrime(l):
    filteredList = list(filter(lambda x: CheckPrime.ChkPrime(x), l))
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

    NewList = ChkPrime(data)
    print("Even Numbers : ", NewList)

if __name__ == "__main__":
    main()