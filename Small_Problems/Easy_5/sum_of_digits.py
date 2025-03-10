"""
Write a function that takes one argument, a positive integer, and returns the
sum of its digits.

P
    inputs: int
    outputs:    int
    rules:
        Explicit Reqs:
            - accept an int
            - return an int
            - return int is the sum of the input int's digits
        Implicit Reqs:
            - None
E
    assert sum_digits(23) == 5
    assert sum_digits(496) == 19
    assert sum_digits(123456789) == 45
D
    list
A
    - coerce tnum to a str
    - interate through the chars in the str
    - coere the chars to an int and append to a list
    - sum the list and return the result
C
"""
import sys


def sum_digits(num: int) -> int:
    """Sums the digits of the input integer num"""
    return sum(int(digit) for digit in str(num))


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
The sum_digits function is defined on line 31, and has 1 parameter, num,
which expects an integer.

On line 33, a generator comprehension is created by coercing num to a str, and
iterating through the digits. Each digit is coerced back to an it, and appended
to the generator comprehension.

The final generator comprehension is totaled with sum() and the result is
returned.

User Level
Sum_digits takes an integer, sums up the integers digits, and returns the
result.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert sum_digits(23) == 5
        assert sum_digits(496) == 19
        assert sum_digits(123456789) == 45
