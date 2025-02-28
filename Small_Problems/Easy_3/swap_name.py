"""
Write a function that takes a string argument consisting of a first name, a
space, and a last name. The function should return a new string consisting of
the last name, a comma, a space, and the first name.
"""
import sys


def swap_name(name: str) -> str:
    """Returns a new string with the given name order reversed, and separated
    by a comma.

    :param name (str): the name string to swap
    :returns (str): the reversed, comma-separated name
    """
    return ", ".join(reversed(name.split()))


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
swap_name is defined on line 9, and has 1 parameter, name, which expects a
string.

The local variable name is split to a list, and the order of the names is
swapped with the reversed method. Finally, the join method concatenates the
names back together with a comma and a space.

The resulting string is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert swap_name('Joe Roberts') == "Roberts, Joe"
