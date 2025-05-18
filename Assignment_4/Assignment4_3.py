# 3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
def min_of_elements(numbers: List[int]) -> int:
    return min(numbers)
if __name__ == "__main__":

    n = int(input("Number of elements: "))
    input_list = []
    for _ in range(n):
        num = int(input("Input Element: "))
        input_list.append(num)
    result = min_of_elements(input_list)
    print("Output:", result)
