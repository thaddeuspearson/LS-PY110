"""
Take the number 735291 and rotate it by one digit to the left, getting 352917.
Next, keep the first digit fixed in place and rotate the remaining digits to
get 329175. Keep the first two digits fixed in place and rotate again to get
321759. Keep the first three digits fixed in place and rotate again to get
321597. Finally, keep the first four digits fixed in place and rotate the
final two digits to get 321579. The resulting number is called the maximum
rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum
rotation of that integer. You can (and probably should) use the
rotate_rightmost_digits function from the previous exercise.

P
    inputs: integer
    outputs: integer
    rules:
        Explicit Reqs:
            - accept an int
            - return an int
            - rotate the number according to the problem description:
              735291 ->  352917
              352917 -> 3 29175
              329175 -> 32 1759
              321759 -> 321 597
              321597 -> 3215 79
        Implicit Reqs:
            - any single digit number returns itself
        Questions:
            - What to do with negative numbers?
E
    assert max_rotation(735291) == 321579
    assert max_rotation(3) == 3
    assert max_rotation(35) == 53
    assert max_rotation(8703529146) == 7321609845

    # Note that the final sequence here is `015`. The leading
    # zero gets dropped, though, since we're working with
    # an integer.
    assert max_rotation(105) == 15
D
    string
A
    - copy / coerce the number to a string
    - loop through a range object of the length of the number - 2 inclusively
        - call rotate_rightmost_digits with the copy and the current range num
    return the copy
C
"""
import sys
from rotation_2 import rotate_rightmost_digits


def max_rotation(number: int) -> int:
    """
    Rotates the given number in repeating succession to give a rotated value
    """
    for n in range(len(str(number)), 1, -1):
        number = rotate_rightmost_digits(number, n)

    return number


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level

The max_rotation function is defined on line 54 takes a sigle parameter,
number, which expects an int.

On line 58, a for loop is defined which loops through a range object, starting
at the length of the digits of number, and counting backwards by 1.

Within the context of the loop, number is rotated with a call to
rotate_rightmost_digits with number and the current range num as arguments.

After the loop has completed, the rotated number is returned

User Level
Max_rotation takes an integer, and rotates its digits to a maximal amount by
rotating each digit position to the end, shifting over the remaining digits,
and repeating while preserving each digit rotation from left to right.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert max_rotation(735291) == 321579
        assert max_rotation(3) == 3
        assert max_rotation(35) == 53
        assert max_rotation(8703529146) == 7321609845

        # Note that the final sequence here is `015`. The leading
        # zero gets dropped, though, since we're working with
        # an integer.
        assert max_rotation(105) == 15
