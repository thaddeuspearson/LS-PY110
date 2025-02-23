"""
Write a function that takes a string of digits and returns the appropriate
number as an integer. You may not use any of the standard conversion functions
available in Python, such as int. Your function should calculate the result by
using the characters in the string. For now, do not worry about leading + or -
signs, nor should you worry about invalid characters; assume all characters
are numeric.
"""
import sys


def string_to_integer(int_str=None):
    """Converts a string represenation of an int to an int.

    :param int_str (str): the str representation of an int
    :returns int: the int version of the int_str
    """
    if int_str is None:
        int_str = input("Please enter an integer: ")

    rev_digits = [c for c in int_str[::-1]]
    return sum([(ord(d) - 48) * 10 ** i for i, d in enumerate(rev_digits)])


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
string_to_integer is defined on line 12. It has a single parameter, int_str,
which accepts a string representation of an int.

The conditional check on line 18 determines if any input has been give, and
otherwise prompts the user to input an integer.

The local vatiable rev_ditige is instantiated to a list literal of the
characters of int_str reversed.

An enumerate object is created from rev_digits, and looped through,
for each character, the current character is coerced to its ascii int value,
and 48 is subracted from this in order to account for the shift. Finally, 10
is raised to the ith power and multiplied for each respective digit, resulting
in the int representation of the given digit. Finally, this is summed, and
returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert string_to_integer("4321") == 4321
        assert string_to_integer("570") == 570
    else:
        print(string_to_integer())
