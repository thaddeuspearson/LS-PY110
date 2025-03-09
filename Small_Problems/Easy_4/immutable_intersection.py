"""
Transform two lists into frozen sets and find their common elements.

P
    inputs: two number lists
    outputs: frozenset of the intersection of the input lists
    rules:
        Explicit Reqs:
            - accept 2 number lists as parameters
            - return the intersection of the input lists as a frozenset
        Implicit Reqs:
            - if either list is empty, return an empty frozenset
E
    list1 = [2, 4, 6, 8]
    list2 = [1, 3, 5, 7, 8]
    expected_result = frozenset({8})
    intersection(list1, list2) == expected_result
D
    frozenset
A
    - coerce input lists to sets
    - get the intersection of the coerced sets
    - coerce the intersection to a frozenset
    - return the frozenset
C
"""
import sys


def intersection(nums_1: list, nums_2: list) -> frozenset:
    """Returns the intersection of two lists as a frozenset"""
    return frozenset(set(nums_1) & set(nums_2))


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
On line 30, the intersection functuion is defined with two parameters, nums_1
and nums_2, which both expect a list of numbers.

Both parameters are coerced to lists, and the intersection operator is used to
get the common elements from both of the coerced sets.

Finally the intersection is coerced to a frozenset and returned.

User Level
Intersection takes two input number lists, coerces them to sets, and returns
their intesection as a frozenset.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        list1 = [2, 4, 6, 8]
        list2 = [1, 3, 5, 7, 8]
        expected_result = frozenset({8})
        assert intersection(list1, list2) == expected_result
