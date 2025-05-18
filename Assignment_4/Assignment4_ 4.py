# 4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
def frequency_of_element(numbers: List[int], element: int) -> int:
    return numbers.count(element)
if __name__ == "__main__":

    n = int(input("Number of elements: "))
    input_list = []
    for _ in range(n):
        num = int(input("Input Element: "))
        input_list.append(num)
    element_to_search = int(input("Element to search: "))
    result = frequency_of_element(input_list, element_to_search)
    print("Output:", result)