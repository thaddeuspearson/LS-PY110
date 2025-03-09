"""
Write a function that takes a string argument and returns a list of substrings
of that string. Each substring should begin with the first letter of the word,
and the list should be ordered from shortest to longest.

P
    inputs: string
    outputs: list of substrings
    rules:
        Explicit Reqs:
            - accept a string
            - return a list of substrings
        Implicit Reqs:
            - an empty string returns an empty list

E
    leading_substrings('abc') == ['a', 'ab', 'abc']
    leading_substrings('a') == ['a']
    leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy']
D
    list
A
    - create a return list
    - loop through the indexes of the string
        - append a slice of the string up to the current index inclusively
    - return the return list
C
"""
import sys


def leading_substrings(input_str: str) -> list:
    """Gets all substrings of input_str that begin with the firset letter of
    input_str
    """
    return [input_str[:i+1] for i, _ in enumerate(input_str)]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
The leading_substrings  function is defined on line 32, and has a single
parameter, input_str, which expects a string.
On line 36, a list comprehension is used in combination with the enumerate
function. At each iteration, the index of the current element is assigned to
i, and a slice of the string up to i (inclucively) is appended to the list.

The final list resulting from the comprehension is returned.

User Level
Leading_substrings gets all the substrings from a given string that start with
the leading character of the string, and returns them as a list.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert leading_substrings('abc') == ['a', 'ab', 'abc']
        assert leading_substrings('a') == ['a']
        assert leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy']
