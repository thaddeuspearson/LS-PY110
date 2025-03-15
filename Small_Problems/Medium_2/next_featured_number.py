"""
A featured number (something unique to this exercise) is an odd number that is
a multiple of 7, with all of its digits occurring exactly once each. For
example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it
is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next
featured number greater than the integer. Issue an error message if there is no
next featured number.

NOTE: The largest possible featured number is 8769543201.

P
    input_nums: int
    outputs: int
    rules:
        Explicit Reqs:
            - accept an int
            - return an int
            - return int should be divisable by 7, odd, and unique digits
            - the largest featured number is 9876543201
            - if given a larger number than the largest, return error message
        Implicit Reqs:
            - None
E
    next_featured(12) == 21
    next_featured(20) == 21
    next_featured(21) == 35
    next_featured(997) == 1029
    next_featured(1029) == 1043
    next_featured(999999) == 1023547
    next_featured(999999987) == 1023456987
    next_featured(9876543186) == 9876543201
    next_featured(9876543200) == 9876543201

    error = ("There is no possible number that "
            "fulfills those requirements.")
    next_featured(9876543201) == error
D
    None
A
    - increment input_num until it is divsable by 7 and odd
      (make_div_by_7_and_odd)
      (add modulo remainder to it or 7 if already divisable by 7), assign value
      to new local var, `curr`
    - Loop until `featured` is not None
        - check all digits to see if they are unique (has_unique_digits)
            - if so, return curr
            - if not, increment num by 14
    - return error message
C
"""
import sys


def make_div_by_7_and_odd(num: int) -> int:
    """Increments num and makes sure it is odd and divisable by 7"""
    num += 7 - (num % 7)
    return num if num % 2 == 1 else num + 7


def has_unique_digits(num: int) -> bool:
    """Check to see if the given num has unique digits"""
    num_str = str(num)
    return len(set(num_str)) == len(num_str)


def next_featured(input_num: int) -> int | str:
    """
    Returns the next featured number larger than the given input_num, or
    error message
    """
    max_featured = 9876543201
    curr = make_div_by_7_and_odd(input_num)

    while curr <= max_featured:
        if has_unique_digits(curr):
            return curr
        curr += 14

    return "There is no possible number that fulfills those requirements."


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

The next_featured function is defined on line 67, and has 1 parameter,
input_num, which expects an int.

On line 72, a constant named MAX_FEATURED is instatnated to the highest
possible featured number.

On line 73, a local variable called curr is set to the return value of the
helper function make_div_by_7_and_odd, which is defined on line 55, and has
1 parameter, num. On line 57, num is incremented to with augmented
assignment the value of the remainder to the next int value that is
divisable by 7. On line 58, a guard clause ternary, ensuring num is odd is
returned.

Back in next_featured, on line 75, curr is checked to be < MAX_FEATURED in the
conditional clause of a while loop. In the loop, on line 76, an if statement
leveraging the return value of has_unique_digits is checked. has_unique_digits
is defined on line 61 and has 1 parameter, num, which expects an int. On line
63, num is coerced to its string representation and assigned to local variable
curr_str. On line 64, curr_str is coerced to a set and the length of this set
is compared to the length of curr_str. The resulting bool is returned.

Back in next_featured, if has_unique_digits is True, curr is returned. If not,
on line 78, curr is incremented by 14, to ensure it is both odd and divisable
by 7.

If curr becomes larger than MAX_FEATURED, the while loop exits and the error
message is returned on line 80.

User Level:
Next_featured takes a number, and finds the next featured number that is
greater than the given number. It leverages a while loop and 2 helper functions
to handle the transformation of the input_num number, and the conditional guard
clause that is responsible for controlling the while loop. Either the next
featured number is returned, or an error message is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert next_featured(12) == 21
        assert next_featured(20) == 21
        assert next_featured(21) == 35
        assert next_featured(997) == 1029
        assert next_featured(1029) == 1043
        assert next_featured(999999) == 1023547
        assert next_featured(999999987) == 1023456987
        assert next_featured(9876543186) == 9876543201
        assert next_featured(9876543200) == 9876543201

        ERROR = ("There is no possible number that "
                 "fulfills those requirements.")
        assert next_featured(9876543201) == ERROR
