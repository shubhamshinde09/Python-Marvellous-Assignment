# 3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
from functools import reduce
from typing import List
from operator import mul
def filter_map_reduce(numbers: List[int]) -> int:
    # Filter numbers between 70 and 90
    filtered_numbers = list(filter(lambda x: 70 <= x <= 90, numbers))
    print("List after filter =", filtered_numbers)

    # Map function to increase each number by 10
    mapped_numbers = list(map(lambda x: x + 10, filtered_numbers))
    print("List after map =", mapped_numbers)

    # Reduce function to return product of all numbers
    product = reduce(mul, mapped_numbers, 1)
    return product
if __name__ == "__main__":
    input_list = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    result = filter_map_reduce(input_list)
    print("Output of reduce =", result)