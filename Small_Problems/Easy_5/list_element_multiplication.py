"""
Given two lists of integers of the same length, return a new list where each
element is the product of the corresponding elements from the two lists.

P
    inputs: 2 lists of integers
    outputs: 1 list of integers
    rules:
        Explicit Reqs:
            - accept two lists
            - return 1 list
            - return list is products of the elems in the input lists
        Implicit Reqs:
            - two empty list returns an empty list
E
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    multiply_items(list_a, list_b) == [4, 10, 18]
D
    list
A
    - zip the input lists
    - multiply the zipped elems
    - append to a return list
    - return the return list
C
"""
import sys


def multiply_items(list_1: list, list_2: list) -> list:
    """Returns a new list containing the products of each of the elements in
    the given input lists"""
    return [p * q for p, q in zip(list_1, list_2)]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
The multiply_items function is defined on line 31, and has 2 params, list_1
and list_2, both expecting a list.

On line 34, a list comprehension is created by zipping up the two input lists,
multiplying the two elements in each zip tuple together, and appending them to
the list comprehension.

The resulting list is returned.


User Level
Multiply_items takes two lists of identical length, multiplies each list
element with with the corresponding element in the opposite list, and returns
the products as a new list.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        list_a = [1, 2, 3]
        list_b = [4, 5, 6]
        assert multiply_items(list_a, list_b) == [4, 10, 18]
