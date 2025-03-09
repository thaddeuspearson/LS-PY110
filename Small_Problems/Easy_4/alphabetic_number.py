"""
Write a function that takes a list of integers between 0 and 19 and returns a
list of those integers sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven,
twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

P
    input: list<int>: [0..19]
    output: list<int>: [0..19] sorted aplhabetically by English representation
    rules:
        Explicit Reqs:
            Must return a list - same as the input, or a new one?
            Return must be sorted alphabetically by english representation
        Implicit Reqs
E
    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                  10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                       7, 17, 6, 16, 10, 13, 3, 12, 2, 0]
D
    list as a lookup using indexes
A
    - create a lookup list constant with each english representation stored
      at its corresponding index
    - use sorted in combination with a custom lambda sorting function
    - return the new sorted list
C
"""
import sys

ENGLISH_INTS = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
]


def alphabetic_number_sort(numbers):
    """Sorts the given number list by its English word representation"""
    return sorted(numbers, key=lambda x: ENGLISH_INTS[x])


# pylint: disable=pointless-string-statement
"""CODE EXPLANATIONS
Implementation Level:
On line 33, a constant ENGLISH_INTS is defined as a list. Each element in the
list is the english represeentation of the index it is stored at.

On line 40, the alphabetic_number_sort function is defined, and has one,
parameter, numbers, which expects a list of integers.

This one liner on line 42 leverages the sorted function, and sets the key
argument to a lambda function which has 1 parameter x. During the sort, the
lambda will lookup the string element in ENGLISH_INTS at the current index
assigned to x, and use what is returned as the key to sort on. Since the
elements in ENGLISH_INTS are strings, the sort is performed alphabetically.

THe newly sorted list that is created by sorted is returned.

User Level:
Alphabetic_number_sort accepts a list of all ints from 0 to 19, sorts them
by their english representation of each integer element, and returns a new
list. It leverages a lookup dictionary that has each index holding the value
of its english representation (ex: 0 -> 'zero', 1 -> 'one'...).
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        input_list = [
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19
        ]

        expected_result = [
            8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
            7, 17, 6, 16, 10, 13, 3, 12, 2, 0
        ]

        assert alphabetic_number_sort(input_list) == expected_result
