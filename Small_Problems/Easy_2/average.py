"""
Write a function that takes one argument, a list of integers, and returns the
average of all the integers in the list, rounded down to the integer component
of the average. The list will never be empty, and the numbers will always be
positive integers.
"""
import sys


def average(nums: list) -> int:
    """Returns the average of the given nums list, rounded down to it's
    integer component.

    :param nums (list): the list of numbers to average
    :returns (int): the integer average of the given numbers
    """
    return int(sum(nums) / len(nums))


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
average is defined on line 10, and has one parameter, nums, which expects a
list.

This one-liner is returned on line 17, first, the sum method totals nums, and
divides it by the length of nums, to get an average, and finally, the int()
built-in coerces the average to it's integer representation.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert average([1, 5, 87, 45, 8, 8]) == 25
        assert average([9, 47, 23, 95, 16, 52]) == 40
        assert average([7]) == 7
