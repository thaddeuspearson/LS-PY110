"""
Write a function that takes a string, doubles every character in the string,
then returns the result as a new string.
"""
import sys


def repeater(input_str: str) -> str:
    """Returns the given string with every characer doubled.

    :param input_str (str): the input string to double
    :returns (str): the doubled string
    """
    return "".join([c + c for c in list(input_str)])


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
repeater is defined on line 8, and has one parameter, input_str.

This one-liner joins the list comprehension created from coercing input_str to
a list, and concatenating each caracter to itself.

The resulting string is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert repeater('Hello') == "HHeelllloo"
        assert repeater('Good job!') == "GGoooodd  jjoobb!!"
        assert repeater('') == ""
