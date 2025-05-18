# 4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.
from functools import reduce
from typing import List
def filter_map_reduce(numbers: List[int]) -> int:
    # Filter even numbers
    filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("List after filter =", filtered_numbers)

    # Map function to calculate square of each number
    mapped_numbers = list(map(lambda x: x ** 2, filtered_numbers))
    print("List after map =", mapped_numbers)

    # Reduce function to return sum of all numbers
    total_sum = reduce(lambda x, y: x + y, mapped_numbers)
    return total_sum
if __name__ == "__main__":
    input_list = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
    result = filter_map_reduce(input_list)
    print("Output of reduce =", result)