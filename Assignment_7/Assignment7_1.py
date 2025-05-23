CalculateSquare = lambda No : No ** 2

CalculateCube = lambda No : No ** 3

def main():
    print("Enter a number : ")
    num = int(input())
    s = CalculateSquare(num)
    c = CalculateCube(num)

    print("Square : ",s)
    print("Cube : ",c)

if __name__ == "__main__":
    main()
