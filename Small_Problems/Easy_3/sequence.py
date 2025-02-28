"""
Write a function that takes an integer argument and returns a list containin
all integers between 1 and the argument (inclusive), in ascending order.
"""
import sys


def sequence(target: int) -> list:
    """Returns a list of numbers from 1 to the target (inclusively).

    :param target (int): the target to end the sequence
    :returns (list): the list of numbers from 1 to target
    """
    return list(range(1, target+1))


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
sequence is defined on line 8 and has a single parameter, target.

The return statement on line 14 returns a range object that begins at 1, and
ends inclusively at the local variable target. THe built-in list method
coerces this range object to a list, which is the final return value.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert sequence(5) == [1, 2, 3, 4, 5]
        assert sequence(3) == [1, 2, 3]
        assert sequence(1) == [1]
