"""
Given two lists, convert them to sets and return a new set which is the union
of both sets.

P
    inputs: two lists of ints
    outputs: a set of ints
    rules:
        Explicit Reqs:
            - accepts 2 lists as args
            - converts those lists to sets
            - returns a single set with the union of the two coerced sets
                - does it need to be a completely new set returned?
        Implicit Reqs:
            - empty lists should be accounted for
E
    list1 = [3, 5, 7, 9]
    list2 = [5, 7, 11, 13]
    merge_sets(list1, list2) -> {3, 5, 7, 9, 11, 13}
D
    return set
A
    - coerce the input lists to sets
    - union the sets
    - return the unioned set
C
"""
import sys


def merge_sets(list_1: list, list_2: list) -> set:
    """Returns two input lists merged to a single set"""
    return set(list_1) | set(list_2)


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:
On line 31, the merge_sets function is defined with two parameters, list_1 and
list_2, which both expect lists of numbers.

Both list_1 and list_2 are coerced to sets, and unioned with the union
operator on line 33, and the resulting set is returned.

User Level:
Merge_sets accepts two number lists as parameters, coerces them to sets, and
returns their union.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        list1 = [3, 5, 7, 9]
        list2 = [5, 7, 11, 13]
        assert merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13}
