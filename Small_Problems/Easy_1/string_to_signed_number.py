"""
n the previous exercise, you developed a function that converts simple numeric
strings to integers. In this exercise, you're going to extend that function to
work with signed numbers.

Write a function that takes a string of digits and returns the appropriate
number as an integer. The string may have a leading + or - sign; if the first
character is a +, your function should return a positive number; if it is a -,
your function should return a negative number. If there is no sign, return a
positive number. You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python,
such as int. You may, however, use the string_to_integer function from the
previous exercise.
"""
import sys
from string_to_integer import string_to_integer


def string_to_signed_integer(int_str=None):
    """Converts a string represenation of a signed int to an int.

    :param int_str (str): the str representation of an int
    :returns int: the int version of the int_str
    """
    if int_str is None:
        int_str = input("Please enter a signed integer: ")

    integer = string_to_integer(int_str.lstrip("+-"))

    if int_str[0] == "-":
        integer *= -1

    return integer


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
string_to_signed_integer is defined on line 21. It has a single parameter,
int_str. The conditional statement on line 26 checks to see if any argument
has been passed to int_str, and if not, prompts the user for input.

On line 29, a local variable, integer, is instantiated with the
string_to_integer function, which is called with the lstriped int_str.

On line 31, the condtional statement is checking to see if the original
int_str was signed negatively, and if so, multiplied the integer by -1.

integer is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert string_to_signed_integer("4321") == 4321
        assert string_to_signed_integer("-570") == -570
        assert string_to_signed_integer("+100") == 100
    else:
        print(string_to_signed_integer())
