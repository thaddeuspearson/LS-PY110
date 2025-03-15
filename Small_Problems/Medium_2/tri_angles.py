"""
A triangle is classified as follows:

    Right: One angle is a right angle (exactly 90 degrees).
    Acute: All three angles are less than 90 degrees.
    Obtuse: One angle is greater than 90 degrees.

To be a valid triangle, the sum of the angles must be exactly 180 degrees, and
every angle must be greater than 0. If either of these conditions is not
satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and
returns one of the following four strings representing the triangle's
classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to
worry about floating point errors. You may also assume that the arguments are
in degrees.

p
    inputs:
    outputs:
    rules:
        Explict Reqs:
            -
        Implicit Reqs:
            -
E
    triangle(60, 70, 50) == "acute"
    triangle(30, 90, 60) == "right"
    triangle(120, 50, 10) == "obtuse"
    triangle(0, 90, 90) == "invalid"
    triangle(50, 50, 50) == "invalid"
D
    None
A
    - check if sum is not 180 or is 0 is in sides, return "invalid" if so
    - check if 90 is in sides, return "right" if so
    - check if max side is greater than 90, if so return "obtuse"
    - else return "acute"
C
"""
import sys


def triangle(sides: list) -> str:
    """
    Returns if a triangle is "right", "obtuse", "acute", or "invalid"
    """
    if sum(sides) != 180 or 0 in sides:
        return "invalid"
    return "right" if 90 in sides else "obtuse" if max(sides) > 90 else "acute"


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

On line 46, the triangle function is defined with one parameter, sides,
which expects a list of 3 ints.

On line 52, "right" is returned if one of the sides is 90, "obtuse" is returned
if the max side is greater than 90, or "acute" for everything else.

User Level:

Triangle takes a list of sides and returns a string indicating what kind of
triangle it is ("right", "obtuse", "acute"), or "invalid" if it is not a valid
triangle.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert triangle([60, 70, 50]) == "acute"
        assert triangle([30, 90, 60]) == "right"
        assert triangle([120, 50, 10]) == "obtuse"
        assert triangle([0, 90, 90]) == "invalid"
        assert triangle([50, 50, 50]) == "invalid"
