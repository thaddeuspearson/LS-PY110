"""
Write a function that takes a list of positive integers as input, multiplies
all of the integers together, divides the result by the number of entries in
the list, and returns the result as a string with the value rounded to three
decimal places.
"""
import sys


def multiplicative_average(int_list: list) -> str:
    """Returns the multiplicative average of the given integer list

    :param int_list (list<int>): the list of ints to average
    :returns (str): the multiplicative average of the given integer list
    """
    return f"{sum(int_list) / len(int_list):3d}"


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
multiplicative_average is defined on line 10, and has a single parameter,
int_list which expects a list of positive intergers.

This one-liner uses the sum method to add the ints in int_list together
and divide it by the length of int_list, in order to return the average.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert multiplicative_average([3, 5]) == "7.500"
        assert multiplicative_average([2, 5, 8]) == "26.667"
        assert multiplicative_average([2, 5]) == "5.000"
        assert multiplicative_average([1, 1, 1, 1]) == "0.250"
        assert multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667"
