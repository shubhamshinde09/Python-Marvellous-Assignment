# 1. Write a program which accept N numbers from user and store It into List. Return addition of all elements from that List.
def sum_of_elements(numbers: List[int]) -> int:
    return sum(numbers)
if __name__ == "__main__":
    n = int(input("Number of elements: "))
    input_list = []
    for _ in range(n):
        num = int(input("Input Element: "))
        input_list.append(num)
    result = sum_of_elements(input_list)
    print("Output:", result)
