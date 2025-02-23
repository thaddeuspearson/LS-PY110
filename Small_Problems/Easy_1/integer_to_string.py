"""
In the previous two exercises, you developed functions that convert simple
numeric strings to signed integers. In this exercise and the next, you're
going to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3,
and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python,
such as str. Your function should do this the old-fashioned way and construct
the string by analyzing and manipulating the number.
"""
import sys


def integer_to_string(integer):
    """Returns the string representation of the given integer.

    :param integer (int): the integer to coerce to a string
    :returns (str): the string representation of integer
    """
    if integer is None:
        integer = int(input("Please enter an integer: "))

    int_str = ''

    while integer != 0:
        int_str += chr((integer % 10) + 48)
        integer //= 10

    return int_str[::-1] or "0"


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
integer_to_string is defined on line 16, with one parameter, integer. The
conditional block on line 22 checks to see if any argument has been passed
to the function during invocation, and prompts the user to enter an integer
if not.

On line 25, a local variable int_str is instantiated to an empty string.

On line 27, a while loop with the conditional expression checking for the
value 0 loops until there are no more digits of integer left. With each
iteration, int_str is concatendated with the ord value of the result of
calling modulo 10 on integer, and adding 48 to account for the shift.
Immediately after, integer is floor divided by 10 in order to remove the last
processed digit.

On line 31, int_str is reversed and returned, or in the case of an empty
string, "0" is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert integer_to_string(4321) == "4321"
        assert integer_to_string(0) == "0"
        assert integer_to_string(5000) == "5000"
        assert integer_to_string(1234567890) == "1234567890"
    else:
        print()
