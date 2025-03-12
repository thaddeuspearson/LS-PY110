"""
Write a function that rotates the last count digits of a number. To perform
the rotation, move the first of the digits that you want to rotate to the end
and shift the remaining digits to the left.

P
    inputs: int, int
    outputs: int
    rules:
        Explicit Reqs:
            - accept an int
            - return an int
            - return should shift the int at the given negative idx to the end
        Implicit Reqs:
            - a single digit returns the same digit
        Questions:
            - What to do if digit is negative
E
    assert rotate_rightmost_digits(735291, 2) == 735219
    assert rotate_rightmost_digits(735291, 3) == 735912
    assert rotate_rightmost_digits(735291, 1) == 735291
    assert rotate_rightmost_digits(735291, 4) == 732915
    assert rotate_rightmost_digits(735291, 5) == 752913
    assert rotate_rightmost_digits(735291, 6) == 352917
    assert rotate_rightmost_digits(1200, 3) == 1002
D
    string
A
    - Coerce the int to a string
    - slice until the given negative index
    - slice from one index past the given index until the end
    - concatenate the initial slice, the negative index val, and the end slice
    - coerce the resulting concatenation back to an int and return
C
"""
import sys


def rotate_rightmost_digits(number: int, digit: int) -> int:
    """
    Rotates the value at the given digit to the end of the number, and shifts
    the remaining digits over to the left by 1 position
    """
    rotated_number = str(number)
    if digit > 1:
        rotated_number = (
            f"{rotated_number[:-digit]}"
            f"{rotated_number[-digit+1:]}"
            f"{rotated_number[-digit:-digit+1]}"
        )
    return int(rotated_number)


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level

The rotate_rightmost_digits function is defined on line 39, and has 2
parameters, number and digit, both expecting an integer.

On line 44 a local variable, called rotated_number is instantiated with the
coercion of numbers to its string representation.

The if conditional statement on line 45 checks to see if digit is greater than
1 as any positive rotation less than 1 returns the number as given.

Line 46 applies a transformation on multiple lines to rotated_number, using
string slicing to rotate the given digit to the end of the string and shift
the remaining digits left.

On line 51, rotated_number is coerced back to an int and returned.


User Level
Rotate_rightmost_digits takes a number and a digit, counts from the right
to the left to get the specified digit value, and moves that digit to the end
of the number, while shifting the other digits to the left by one position.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert rotate_rightmost_digits(735291, 2) == 735219
        assert rotate_rightmost_digits(735291, 3) == 735912
        assert rotate_rightmost_digits(735291, 1) == 735291
        assert rotate_rightmost_digits(735291, 4) == 732915
        assert rotate_rightmost_digits(735291, 5) == 752913
        assert rotate_rightmost_digits(735291, 6) == 352917
        assert rotate_rightmost_digits(1200, 3) == 1002
