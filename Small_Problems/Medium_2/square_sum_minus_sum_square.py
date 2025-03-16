"""
Write a function that computes the difference between the square of the sum of
the first count positive integers and the sum of the squares of the first count
positive integers.

P
    inputs: int
    outputs: int
    rules:
        Explicit Reqs:
            - accept an int
            - return an int
            - return int is the difference of suaring the sum of ints up to the
              given number from the sum of each int squared
        Implicit Reqs:
            - 0 should return 0
E
    sum_square_difference(3) == 22
    # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

    sum_square_difference(10) == 2640
    sum_square_difference(1) == 0
    sum_square_difference(100) == 25164150
D
    2 Generator comprehensions
A
    - create 2 generators
        - sum of squares (generator 1)
            - get each int using range
            - square each int
            - get the sum of the squares
        - square of sums (generator 2)
            - get each int using range
            - sum the ints
            - square the sums
    - return generator 1 - generator 2
C
"""
import sys


def sum_square_difference(num: int) -> int:
    """
    Returns the difference between a sum of the squares of the first num of
    integes and the sum of num integers squared.
    """
    sum_of_squares = sum(n**2 for n in range(num+1))
    square_of_sums = sum(n for n in range(num+1)) ** 2
    return square_of_sums - sum_of_squares


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

On line 42, sum_square_difference is defined with 1 parameter, num, which
expects a int.

On line 47, local variable sum_of_squares is defined with a call to sum, having
a generator comprehension as an argument that squares every number in a range
ending at num+1.

On line 48, local variable square_of_sums is defined with a call to sum, with a
generator comprehension that returns every number in a range ending at num+1.

On line 49, square_of_sums is subtracted by sum_of_squares and the result is
returned.

User Level:

Sum_square_difference takes a number, and gets the sum of the numbers and
squares the result, and subtracts from this the sum of all numbers squared
up to the given number, and returns the result.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert sum_square_difference(3) == 22
        # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

        assert sum_square_difference(10) == 2640
        assert sum_square_difference(1) == 0
        assert sum_square_difference(100) == 25164150
