"""
Write a function that returns a list of all substrings of a string. Order the
 returned list by where in the string the substring begins. This means that
 all substrings that start at index position 0 should come first, then all
 substrings that start at index position 1, and so on. Since multiple
 substrings will occur at each position, return the substrings at a given
 index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the
previous exercise.

P
    inputs:
    outputs:
    rules:
        Explitic Reqs:
            - Use the leading_substring function
            - accept a string
            - return all sublists of the string
        Implicit Reqs:
            - an empty string returns an empty list

E
    expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
    ]
    substrings('abcde') == expected_result)
D
    list
A
    - create a list comprehension
        - loop through each letter of the string
        - call leading_substrings on each letter
    - return the resulting list
C
"""
import sys
from leading_substrings import leading_substrings


def substrings(input_str: str) -> list:
    """Returns all substrings of the input_str"""
    all_substrs = []

    for i, _ in enumerate(input_str):
        all_substrs.extend(leading_substrings(input_str[i:]))
    return all_substrs


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
On line 45, the substrings function is defined and has 1 parameter, input_str.

On line 47, a local varible all_substrs is assigned to an empty list literal.

on line 49, a for loop is defined and uses the enumerate function to access
the index, i, and an unused variable , noted with the underscore.
In the context of each iteration, on line 50, all_substrs is extended with
the list of leading substrings returned from calling the leading_substrings
function with a slice of the input_str starting at the i index.

all_substrs is returned on line 51, after the for loop has finished.

User Level
Substrings leverages the leading_substrings function to iterate through the
indexes of a string, create a substring with slicing, and call
leading_substrings with every substring ending with the final character of
the original input string. The final result is every possible substring of
the given string returned as a list.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        expected_result = [
            "a", "ab", "abc", "abcd", "abcde",
            "b", "bc", "bcd", "bcde",
            "c", "cd", "cde",
            "d", "de",
            "e",
        ]
        assert substrings('abcde') == expected_result
