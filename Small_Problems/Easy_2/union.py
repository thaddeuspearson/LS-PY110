"""
Write a function that takes two lists as arguments and returns a set that
contains the union of the values from the two lists. You may assume that both
arguments will always be lists.
"""
import sys


def union(list_1, list_2):
    """Returns the union of 2 lists as a set

    :param list_1 (list<multi>): first list to union
    :param list_2 (list<multi>): second list to union
    :returns (set): the unioned set
    """
    return set(list_1) | set(list_2)


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
union is defined on line 9 and has 2 parameters, list_1 and list_2.

On line 15, both lists are cast to sets, and unioned with the union operator.
The resulting unioned set from this operation is then returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}
