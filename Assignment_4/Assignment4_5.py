# 5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number
# to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function should be ListPrime().
from typing import List
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def sum_of_primes(numbers: List[int]) -> int:
    prime_numbers = filter(is_prime, numbers)
    return sum(prime_numbers)
if __name__ == "__main__":
    n = int(input("Number of elements: "))
    input_list = []
    for _ in range(n):
        num = int(input("Input Element: "))
        input_list.append(num)
    result = sum_of_primes(input_list)
    print("Output:", result)
