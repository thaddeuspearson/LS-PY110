"""
A triangle is classified as follows:

    Equilateral: All three sides have the same length.
    Isosceles: Two sides have the same length, while the third is different.
    Scalene: All three sides have different lengths.

To be a valid triangle, the sum of the lengths of the two shortest sides must
be greater than the length of the longest side, and every side must have a
length greater than 0. If either of these conditions is not satisfied, the
triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as
arguments and returns one of the following four strings representing the
triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'

P
    inputs: int, int, int
    outputs: str ("equilateral"/"isosceles"/"scalene"/"invalid")
    rules:
        Explicit Reqs:
            - accept 3 ints
            - return a string
            - return string: "equilateral", "isosceles", "scalene", "invalid"
        Implicit Reqs:
            -
        Questions:
            - Negative inputs?
E
    triangle(3, 3, 3) == "equilateral"
    triangle(3, 3, 1.5) == "isosceles"
    triangle(3, 4, 5) == "scalene"
    triangle(0, 3, 3) == "invalid"
    triangle(3, 1, 1) == "invalid"
D
    None
A
    - if the triangle is valid:
        - cast input ints to a set and get len
            - if len is 1 return "equalateral"
            - elif len is 2, return "isosceles"
            - else return "scalene"
    return "invalid"

    Triangle is Valid Func
    - sort the inoput ints in ascending
    - 0 in input ints or
      the sum of first two ints is less than the third:
      return False
    - Return True
C
"""
import sys


def is_valid_triangle(sides: list) -> bool:
    """Returns if the given sides create a valid triangle"""
    if 0 in sides:
        return False
    sides.sort()
    return (sides[0] + sides[1]) > sides[2]


def triangle(sides: list) -> bool:
    """Returns the type of triangle given the sides."""
    if is_valid_triangle(sides):
        sides = set(sides)

        match len(sides):
            case 3:
                return "scalene"
            case 2:
                return "isosceles"
            case 1:
                return "equilateral"
    return "invalid"


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

On Line 64 the triangle function is defined with 1 parameter, sides,
which expects a list of 3 ints.

On line 66, the if condional block tests if the given sides are valid with the
helper function is_valid_triangle.

is_valid_triangle is defined on line 56, and has one parameter, sides, which
expects a list of three integers.

On line 58, the in conditional tests if 0 is in sides, if so, returns False.
On line 60, sides is sorted with .sort(), and on line 61, the first two sides
are summed and checked to see if they are larger than the longest side. If so,
True is returned, False if not.

Back in triangle, on line 70, sides is cast to a set. On line 69, a match
block checks the len of the sides set to see how many unique sides it has,
and returns the correct string based on the number of sides in the set.

User Level:
Triangle leverages a helkper function to check to see if the given sides can
compose a valid triangle, and uses addition / conditional testing to see what
kind of triangle the sides can make. The correct resulting string is returned
if the triangle is valid.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert triangle([3, 3, 3]) == "equilateral"
        assert triangle([3, 3, 1.5]) == "isosceles"
        assert triangle([3, 4, 5]) == "scalene"
        assert triangle([0, 3, 3]) == "invalid"
        assert triangle([3, 1, 1]) == "invalid"
