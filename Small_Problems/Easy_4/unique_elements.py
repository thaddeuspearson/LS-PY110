"""
From two list arguments, determine the elements that are unique to the first
list. The return value should be a set.

P
    inputs: two lists
    outputs: the unique elements in the first list as a set
    rules:
        Explicit Reqs:
            - accept two lists
            - retrieve the unique elemes in the first as a set
            - will the input lists have the same elem types?
            - what if list 1 contains list 2 as an element?
        Implicit Reqs:
            - an empty first list returns an empty set
            - an empty second list returns all elems of the first

E
    list1 = [3, 6, 9, 12]
    list2 = [6, 12, 15, 18]
    unique_from_first(list1, list2) == {9, 3}
D
    set
A
    - coerce the lists to sets
    - subtract the second set from the first
    - return the difference of the first set
C
"""
import sys


def unique_from_first(list_1: list, list_2: list) -> set:
    """Returns the unique elements of ist 1 as a set"""
    return set(list_1) - set(list_2)


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
On line 33, the unique_from)first function is defined with two parameters,
list_1, and list_2, which both expect lists.

On line 35, each input list is coerced to a set, and the second set is
subtracted from the first set. The resulting unique values remaining in the
first set are returned.

User Level
Unique_from_first takes two lists, finds the unique values in the first list,
and returns them as a set.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        list1 = [3, 6, 9, 12]
        list2 = [6, 12, 15, 18]
        assert unique_from_first(list1, list2) == {9, 3}
