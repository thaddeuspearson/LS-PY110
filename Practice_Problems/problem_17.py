"""
Create a function that takes a list of integers as an argument. The function
should determine the minimum integer value that can be appended to the list so
the sum of all the elements equal the closest prime number that is greater
than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum
to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the
list to sum to 7.

Notes:

    - The list will always contain at least 2 integers.
    - All values in the list must be positive (> 0).
    - There may be multiple occurrences of the various numbers in the list

P
    inputs: list
    outputs: int
    rules:
        Explicit Reqs:
            - accept a list of ints
            - return an int
            - return int is the number needed to add to the sum of the
              input_nums to get to the next prime number
            - The list will always contain at least 2 integers.
            - All values in the list must be positive (> 0).
            - There may be multiple occurrences of the numbers in the list
E
    (see test cases below)
D

A
    - is_prime
        - floor divide the number by 2
        - loop to the quotient
        - mod each number checking for equality to 0
            - if it is return False
        return True

    - sum the input_nums
    - prime_candidate = sum + 1
    - while prime_candidate is not prime:
        increment prime_canidate by 1
    - return prime_candicate - sum

C
"""


def is_prime(num: int) -> bool:
    """returns is a number is prime or not"""
    i = 2

    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


def nearest_prime_sum(input_nums: list) -> int:
    """
    Returns the distance between the sum of the input_nums list and the next
    prime number.
    """
    input_sum = sum(input_nums)
    candidate = input_sum + 1

    while not is_prime(candidate):
        candidate += 1

    return candidate - input_sum


if __name__ == "__main__":
    assert nearest_prime_sum([1, 2, 3]) == 1
    assert nearest_prime_sum([5, 2]) == 4
    assert nearest_prime_sum([1, 1, 1]) == 2
    assert nearest_prime_sum([2, 12, 8, 4, 6]) == 5
    assert nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4
