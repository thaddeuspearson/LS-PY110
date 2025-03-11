"""
Given a sequence of integers, filter out instances where the same value occurs
successively, retaining only the initial occurrence. Return the refined
sequence.

P
    inputs: list of ints
    outputs: list of ints
    rules:
        Explicit Reqs:
            - accept a list of ints
            - return a list of ints
            - return list should have no successive duplicate ints
        Implicit reqs:
            - multiple instances of the same int are possible, as long as they
              are not successive
            - an empty input list should return an empty list
E
    original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
    expected = [1, 2, 6, 5, 3, 4]
    unique_sequence(original) == expected
D
    list
A
    - create a return list
    - iterate through the input list
    - handle the first element in the list
    - check the previous char to see if it is the same as the curr char
        - if it isnt, append the curr char to the return list
    - return return list
C
"""
import sys


def unique_sequence(numbers: list) -> list:
    """Filters out duplicates ints from the given list."""
    return [
        num for i, num in enumerate(numbers)
        if i == 0 or num != numbers[i-1]
    ]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
The unique_sequence function is defined on line 36, and has 1 parameter,
numbers, which expects a list of ints.

On line 38, a list comprehension is created by iterating though an enumeration
of numbers, creating local variables i and num.

The if conditional on line 40 checks to see if i is the first index, or if num
is not equal to the previous element in num. If either condition is true, num
is appended to the comprehension.

The resulting list is returned.

User Level
Unique_sequence takes a list of integers, removes any duplicate sequences of
integers, and returns the remaining ints in a new list.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
        expected = [1, 2, 6, 5, 3, 4]
        assert unique_sequence(original) == expected
