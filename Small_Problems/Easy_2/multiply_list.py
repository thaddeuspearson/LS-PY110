"""
Write a function that takes two list arguments, each containing a list of
numbers, and returns a new list that contains the product of each pair of
numbers from the arguments that have the same index. You may assume that the
arguments contain the same number of elements.
"""
import sys


def multiply_list(nums_1: list, nums_2: list) -> list:
    """returns a list of products resulting from multiplying the numbers at
    corresponding indexes of two lists. Assumes both lists have the same
    number of elements.

    :param nums_1 (list): first list of nums
    :param nums_2 (list): second list of nums
    :returns list: the products of all the nums in both lists"""
    return [n_1 * n_2 for n_1, n_2 in zip(nums_1, nums_2)]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
multiply_list is defined on line 10. It has two parameters, nums_1 and nums_2
both expecting lists of numbers, and the same number of elements.

The statement on line 18 returns a list comprehension to zip both lists
together, and multiply each corresponding element with each other.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        list1 = [3, 5, 7]
        list2 = [9, 10, 11]
        test_1 = multiply_list(list1, list2)
        assert test_1 == [27, 50, 77], test_1
