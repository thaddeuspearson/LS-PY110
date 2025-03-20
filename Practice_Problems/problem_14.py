"""
Create a function that takes a single integer argument and returns the sum of
all the multiples of 7 or 11 that are less than the argument. If a number is a
multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21,
and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

P
    inputs: int
    outputs: int
    rules:
        Explicit Reqs:
            - accept an integer
            - return an integer
            - return int is the sum of all the multiples of 7 and 11 below the
              input_int
            - if the input_int is negative, return 0
E
    (see test cases below)
D
    generator comprehension
A
    - create a `total`
    - iterate up to the given input_num
    - check if the curr_num is divisable by 7
        - if so, add it to total
    - check if the curr_num is divisable by 11
        - if so add to the total
    - return total
C
"""


def seven_eleven(input_int: int) -> int:
    """
    Returns the sum of all multiples of 7 or 11 below the given input_int
    """
    return sum(
        num for num in range(input_int) if num % 7 == 0 or num % 11 == 0
    )


if __name__ == "__main__":
    assert seven_eleven(10) == 7
    assert seven_eleven(11) == 7
    assert seven_eleven(12) == 18
    assert seven_eleven(25) == 75
    assert seven_eleven(100) == 1153
    assert seven_eleven(0) == 0
    assert seven_eleven(-100) == 0
