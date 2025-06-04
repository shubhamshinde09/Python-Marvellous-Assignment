def Power(x,y):
    if y == 0:
        return 1
    else:
        result = Power(x, y - 1)
        return x * result

def main():
    print("Enter the value of a : ")
    a = int(input())
    print("Enter the value of b : ")
    b = int(input())
    ret = Power(a,b)
    print("The Power of given number is : ",ret)

if __name__ == "__main__":
    main()