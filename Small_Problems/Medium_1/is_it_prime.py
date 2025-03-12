"""
Write a function that takes a positive integer as an argument and returis true
if the number is pri if it is not prime.

You may not use any of Python's add-on packages to solve this problem. Your
task is to programmatically determine whether a number is prime without
relying on functions that already do that for you.

P
    inputs:
    outputs:
    rules:
        Explicit Reqs:
            -
        Implicit Reqs:
            -
E
    assert is_prime(1)
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4)
    assert is_prime(5) is True
    assert is_prime(6)
    assert is_prime(7) is True
    assert is_prime(8)
    assert is_prime(9)
    assert is_prime(10)
    assert is_prime(23) is True
    assert is_prime(24)
    assert is_prime(997) is True
    assert is_prime(998)
    assert is_prime(3_297_061) is True
    assert is_prime(23_297_061)
D
    None
A
    - check if number is 1 and return false if it is
    - loop up to half of the given number
        - check if the curr num evenly divides the number
            - if it does and isn't 1, return False
    - return True
C
"""
import sys


def is_prime(number: int) -> bool:
    """Returns if the given number is prime"""
    if number == 1:
        return False

    for num in range(1, (number // 2) + 1):
        if number % num == 0 and num != 1:
            return False

    return True


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level

On line 47, the is_prime function is defined with a single parameter, number,
which expects an integer.

On line 49, an if conditional statement checks to see if the number is 1 and
returns False if it is.

On line 52, a for loop iterates through a range object initialized at 1, and
ending at half of the given number inclusively. in each iteration, num is used
in conjunction with the modulo operator to check if there is any remainder
when dividing the original number by the current iteration of num.

If there is no remainder, the num is checked to be sure it isn't 1. In the
case that both of these statements evaluate to True, False is returned.

After the loop, on line 56, True is returned.


User Level
Is_prime takes a number and returns True if it is a prime number (which it
verifies with modular math) or False if it is not.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert not is_prime(1)
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert not is_prime(4)
        assert is_prime(5) is True
        assert not is_prime(6)
        assert is_prime(7) is True
        assert not is_prime(8)
        assert not is_prime(9)
        assert not is_prime(10)
        assert is_prime(23) is True
        assert not is_prime(24)
        assert is_prime(997) is True
        assert not is_prime(998)
        assert is_prime(3_297_061) is True
        assert not is_prime(23_297_061)
