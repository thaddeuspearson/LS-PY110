"""
In the previous exercise, you developed a function that converts non-negative
numbers to strings. In this exercise, you're going to extend that function by
adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string
representation. You may not use any of the standard conversion functions
available in Python, such as str. You may, however, use integer_to_string from
the previous exercise.
"""
import sys
from integer_to_string import integer_to_string


def signed_integer_to_string(integer):
    """Returns a string representation of a signed int.

    :param integer (int): an integer to coerce to a string
    :returns int_str (str): the coerced string representation of integer
    """
    if integer is None:
        integer = int(input("Please enter a signed integer: "))

    int_str = ''

    if integer < 0:
        integer *= -1
        int_str += '-'
    elif integer > 0:
        int_str += "+"

    int_str += integer_to_string(integer)
    return int_str


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
signed_integer_to_string, defined on line 15, has exactly one parameter,
integer, which expects an integer argument.

The conditional statement on line 21 checks to see if any argument has been
provided to integer, and prompts the user if not.

On line 24, a local varible int_str is instantiated as an empty string.

The if/elif conditional block starting on line 26 handles the case that
integer is negative or positive, by concatenating a - or + accordingly to
int_str. The multiplication on line 27 it to handle the case that integer is
negative.

int_str is concatenated with the return value of calling the integer_to_string
function with integer as an argument. Finally, int_str is returned on line 33.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert signed_integer_to_string(4321) == "+4321"
        assert signed_integer_to_string(-123) == "-123"
        assert signed_integer_to_string(0) == "0"
    else:
        print()
