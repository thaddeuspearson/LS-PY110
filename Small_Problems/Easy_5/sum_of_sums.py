"""
Write a function that takes a list of numbers and returns the sum of the sums
of each leading subsequence in that list. Examine the examples to see what we
mean. You may assume that the list always contains at least one number.

P
    inputs: list
    outputs: int
    rules:
        Explicit Reqs:
            - accept a list
            - return an int
            - int should be the sum of all leading sequences in the list
        Implicit Reqs:
            - negative numbers should decrement the sum
E
    assert sum_of_sums([3, 5, 2]) == 21
    # (3) + (3 + 5) + (3 + 5 + 2) --> 21

    assert sum_of_sums([1, 5, 7, 3]) == 36
    # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

    assert sum_of_sums([1, 2, 3, 4, 5]) == 35
    # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

    assert sum_of_sums([4]) == 4
D
    list
A
    - iterate through the number list
    - create a sub sequence and get its sum
    - append the sum to a generator literal
    - sum the generator and return
C
"""
import sys


def sum_of_sums(numbers: list) -> int:
    """
    Returns the sum of each leading sequence in the given numbers
    ex: [1, 2, 3] = (1) + (1 + 2) + (1 + 2 + 3) = 10
    """
    return sum(
        sum(numbers[n] for n in range(i+1)) for i, _ in enumerate(numbers)
    )


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implemention Level
The sum_of_sums function is defined on line 39, and has one parameter, numbers
which expects a list of ints.

On line 44, a generator comprehension is created by iterating through an
enumeration of numbers to access the indexes as i. A subsequence is created
by using the range function inclusively with i, and accessing each element in
numbers at the i index, and adding them up with sum. This total is appended to
the generator.

The resulting generator is used as an argument to another sum function call,
and the resulting total is returned.

User Level
Sum_of_sums takes an integer list, gets the sum of each leading sequence, and
adds those sums to a final integer result.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert sum_of_sums([3, 5, 2]) == 21
        # (3) + (3 + 5) + (3 + 5 + 2) --> 21

        assert sum_of_sums([1, 5, 7, 3]) == 36
        # (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

        assert sum_of_sums([1, 2, 3, 4, 5]) == 35
        # (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

        assert sum_of_sums([4]) == 4
