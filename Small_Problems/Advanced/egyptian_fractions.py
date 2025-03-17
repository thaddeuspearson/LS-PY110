"""
Write two functions: one that takes a Rational number as an argument, and
returns a list of the denominators that are part of an Egyptian Fraction
representation of the number, and another that takes a list of numbers in the
same format, and calculates the resulting Rational number. You will need to
use the Fraction class provided by the fractions module.

P
    Egyptian
        inputs: Fraction
        outputs: list
        rules:
            Explicit Reqs:
                - accept a Fraction instance
                - return a list of unit fraction denominators
                - The list of fractions should sum to the target fraction
            Implict Reqs:
                - None

    Unegyptian
        inputs: egyptian_fraction
        outputs: Fraction instance
        rules:
            Explicit Reqs:
                - accept an eqyptian_fraction
                - return a Fraction instance
                - the return Fraction instance is the sum of all the given
                  unit denominators coerced to unit fractions
            Implict Reqs:
                - None
E
    assert egyptian(Fraction(2, 1)) == [1, 2, 3, 6]
    assert egyptian(Fraction(137, 60)) == [1, 2, 3, 4, 5]
    assert egyptian(Fraction(3, 1)) == [
        1, 2, 3, 4, 5, 6, 7,
        8, 9, 10, 15, 230, 57960
    ]

    assert unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2)
    assert unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4)
    assert unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20)
    assert unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130)
    assert unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7)
    assert unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1)
    assert unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1)
    assert unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1)
D

A
    Egyptian:
        - create an empty return list
        - create the first unit denominator to start (1)
        - loop until the target equals 0
            - check if curr unit fraction is less than the target
                - if so, subtract it from the target
                - append the unit denominator to the return list
            - increment the unit denominator by 1
        return the return list
    Unegyptian:
        - iterate through the egyptian fraction denominators
        - create each unit fraction, and append to a generator
        - sum the generator
        - coerce the sum to a Fraction instance
C
"""
import sys
from fractions import Fraction


def egyptian(target_fraction: Fraction) -> list:
    """
    Returns a list of unit fraction demoninators (egyptian fraction)
    culminating in the given fraction.
    """
    unit_denominators = []
    curr_denominator = 1

    while target_fraction != 0:
        curr_fraction = Fraction(1, curr_denominator)

        if curr_fraction <= target_fraction:
            target_fraction -= curr_fraction
            unit_denominators.append(curr_denominator)

        curr_denominator += 1
    return unit_denominators


def unegyptian(egyptian_fraction_denominators: list) -> Fraction:
    """
    Returns a fraction class created from in the given egyptian fraction.
    """
    return Fraction(
        sum(
            Fraction(1, denominator)
            for denominator in egyptian_fraction_denominators
        )
    )


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level Egyptian:

- On line 67, the egyptian function is defined with a single parameter,
target_fraction, which expects a Fraction instance.

- On line 72, a local variable unit_demoninators is instantiated with an empty
list literal. On line 73, a local variable named curr_denominator is defined
and assigned the integer value 1.

- On line 75, a while loop is defined to loop with the conditional expression
that target_fraction does not equal 0. On line 76, a local variable called
curr_fraction is instantiated to a Fraction instance composed of the unit
fraction created with 1 and the curr_denominator.

- On line 78, an if conditional block is guarded by the checking to see if
curr_fraction is less than target_fraction. if it is, it is subtracted from
target_fraction, and the denominator is appended to unit_denominators.

- On line 82, curr_denominator is incremented by 1.

- After the loop has exited, unit_denominators is returned on line 83.


User Level Egyptian:

- Egyptian takes a fraction, uses subraction to break it down to a list of
smaller unit fractions, and the denominators from these unit fractions are
returned as a list.


Implementation Level Unegyptian:

- On line 86, the unegyptian function is defined, with one parameter,
egyptian_fraction_denominators, which expects a list of ints.

- On line 90 a An instance of a Fraction is returned. The argument to the
Fraction constructor is a call to sum, which also has an argument of a
generator comprehension.

- This comprehension starting on line 92 iterates through the given
egyptian_fraction_denominators, appends each unit fraction compiosed of
1 and the current iteration of denominator.

- The resulting fraction is returned.


User Level Unegyptian:

- Unegyptian takes a list of unit denominators, creates their unit fraction
representions, sums them up, and returns a new instance of a Fraction class.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert egyptian(Fraction(2, 1)) == [1, 2, 3, 6]
        assert egyptian(Fraction(137, 60)) == [1, 2, 3, 4, 5]
        assert egyptian(Fraction(3, 1)) == [
            1, 2, 3, 4, 5, 6, 7,
            8, 9, 10, 15, 230, 57960
        ]
        assert unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2)
        assert unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4)
        assert unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20)
        assert unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130)
        assert unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7)
        assert unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1)
        assert unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1)
        assert unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1)
