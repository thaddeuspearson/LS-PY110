"""
Write a function that takes one argument, a positive integer, and returns a
list of the digits in the number.
"""
import sys


def digit_list(num: int) -> list:
    """Returns the integer representation of the digits of the given number
    as a list.

    :param num (int): the integer to split to a list
    :returns (list): list containing the integer represenation of the digits
    """
    return [int(n) for n in str(num)]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
digit_list is defined on line 8, and has one parameter, num.

This one-liner uses a list comprehension to loop though the string
representation of num, and coerce each char to its integer representation.

The resulting list is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert digit_list(12345) == [1, 2, 3, 4, 5]
        assert digit_list(7) == [7]
        assert digit_list(375290) == [3, 7, 5, 2, 9, 0]
        assert digit_list(444) == [4, 4, 4]

