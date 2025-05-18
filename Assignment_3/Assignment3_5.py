#5 Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers.

from functools import reduce
from typing import List
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def filter_map_reduce(numbers: List[int]) -> int:

    # Filter prime numbers
    filtered_numbers = list(filter(is_prime, numbers))
    print("List after filter =", filtered_numbers)

    # Map function to multiply each number by 2
    mapped_numbers = list(map(lambda x: x * 2, filtered_numbers))
    print("List after map =", mapped_numbers)

    # Reduce function to return maximum number
    max_number = reduce(lambda x, y: x if x > y else y, mapped_numbers)
    return max_number
if __name__ == "__main__":
    input_list = [2, 70, 11, 10, 17, 23, 31, 77]
    result = filter_map_reduce(input_list)
    print("Output of reduce =", result)
