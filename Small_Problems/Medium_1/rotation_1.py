"""
Write a function that rotates a list by moving the first element to the end of
the list. Do not modify the original list; return a new list instead.

P
    inputs: list
    outputs: list
    rules:
        Explicit Reqs:
            - accept a list
            - return a new list
            - do not modify the input list
        Implicit Reqs:
            -   an empty loist returns an empty list
E
    rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7]
    rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a']
    rotate_list(['a']) == ['a']
    rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1]
    rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}]
    rotate_list([]) == []

    # return `None` if the argument is not a list
    rotate_list(None) == None
    rotate_list(1) == None

    # the input list is not mutated
    lst = [1, 2, 3, 4]
    rotate_list(lst) == [2, 3, 4, 1]
    lst == [1, 2, 3, 4]
D
    list
A
    - return None is lst is not a list
    - get a slice of the list from the 1st index -> end
    - append the first element to the end of the new slice
    - return the slice
C
"""
import sys


def rotate_list(lst: list) -> list:
    """Rotates a list by 1 element from front to back"""
    return None if not isinstance(lst, list) else lst[1:] + lst[0:1]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
The rotate_list function is defined on line 44, and has one parameter, lst,
which expects a list.

This one liner uses a ternary statement to check if lst is a list with
`isinstance()` and return None if it is not, or create a new slice starting
with the 1st index until the end of lst, and then appending another slice
starting from the beginning of the linst and going until the first index.

The resulting list is returned.

User Level
Rotate_list takes a list, and moves the first element to the end of the list.
This function handles non-list arguments by returning None in those cases.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7]
        assert rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a']
        assert rotate_list(['a']) == ['a']
        assert rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1]
        assert rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}]
        assert rotate_list([]) == []

        # return `None` if the argument is not a list
        assert rotate_list(None) is None
        assert rotate_list(1) is None

        # the input list is not mutated
        test_lst = [1, 2, 3, 4]
        assert rotate_list(test_lst) == [2, 3, 4, 1]
        assert test_lst == [1, 2, 3, 4]
