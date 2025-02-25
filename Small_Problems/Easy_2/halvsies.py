"""
Write a function that takes a list as an argument and returns a list that
contains two elements, both of which are lists. Put the first half of the
original list elements in the first element of the return value and put the
second half in the second element. If the original list contains an odd number
of elements, place the middle element in the first half list.
"""
import sys
from math import ceil


def halvsies(lst):
    half_idx = ceil(len(lst) / 2)
    return [lst[:half_idx], lst[half_idx:]]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
halvsies is defined on line 12. It has one parameter, lst, which expects a
list.

On line 13, a local variable named half_idx is instantiated to the value of
calling the len built-in function on lst, dividing it by 2, and using the ceil
function from the math module to round up, in oder to account for lists with
an odd number of elements.

On line 14, a list literal is created, containing 2 sub-lists which use
half_idx to create the necessary slices in order to "split the list in half".
This newly created list is then returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        test_1 = halvsies([1, 2, 3, 4])
        assert test_1 == [[1, 2], [3, 4]], test_1

        test_2 = halvsies([1, 5, 2, 4, 3])
        assert test_2 == [[1, 5, 2], [4, 3]], test_2

        test_3 = halvsies([5])
        assert test_3 == [[5], []], test_3

        test_4 = halvsies([])
        assert test_4 == [[], []], test_4
