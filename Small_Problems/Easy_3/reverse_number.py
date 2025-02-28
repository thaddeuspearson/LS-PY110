"""
Write a function that takes a positive integer as an argument and returns that
number with its digits reversed.
"""
import sys


def reverse_number(number: int) -> int:
    """Returns an integer's digits reversed

    :param number (int): the number to reverse
    :returns (int): the reversed integer"""
    return int(str(number)[::-1])


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
reverse_number is defined on line 8, with a single parameter number.

This one-liner coerces number to a string, and uses slicing to reverse it.
Then the reversed string is coerced back into its integer representation and
returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert reverse_number(12345) == 54321
        assert reverse_number(12213) == 31221
        assert reverse_number(456) == 654
        assert reverse_number(1) == 1
        assert reverse_number(12000) == 21
