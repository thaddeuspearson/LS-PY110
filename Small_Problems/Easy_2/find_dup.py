"""
Given an unordered list and the information that exactly one value in the list
occurs twice (every other value occurs exactly once), determine which value
occurs twice. Write a function that finds and returns the duplicate value.
You may assume that the input list will always have exactly one duplicate
value.
"""
import sys


def find_dup(lst):
    """Finds the only duplicate in a list of unique elements.

    :param lst (list): the list to find the duplicate in
    :returns elem (many): the duplicate elem
    """
    elems = set()

    for elem in lst:
        if elem in elems:
            return elem
        elems.add(elem)


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
find_dup is defined on line 11. On line 17, a local variable is instantiated
with the value of an empty set.

On line 19, a for loop is set to iterate through lst one element at a time.
With each iteration, the current element is checked against elems to see if
the current element has been added previously. If it is, it is returned

On line 22, the current element is added to elems.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert find_dup([1, 5, 3, 1]) == 1
        assert find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                  7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
            ]) == 73
