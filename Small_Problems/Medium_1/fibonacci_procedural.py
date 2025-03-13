"""
Write a function called assert fibonacci that computes the nth Fibonacci
number, where nth is an argument passed to the function.

P
    inputs: int
    outputs: int
    rules:
        Explicit Reqs:
            - accept an int
            - return an int
            - return int is the nth fibonacci number
        Implicit Reqs:
            - if the input is 0, return a 0
        Questions:
            - What to do with negative numbers?
E
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(12) == 144
    assert fibonacci(20) == 6765
    assert fibonacci(50) == 12586269025
    assert fibonacci(75) == 2111485077978050
D
    None
A   - create base case checks for 1 and 2 return 1 exclusively
    - create a first_previous fibonacci number variable initialized to 1
    - create a second_previous fibonacci number variable initialized to 1
    - create a fibonacci sum variable initialized to 0
    - loop until the given number (start at 2, end at number, count by 1)
        - sum first and second together
        - second_previous is assigned the value of first_previous
        - first_previous is assigned the sum
C
"""
import sys


def fibonacci(number: int) -> int:
    """Returns the nth fibonacci number procedurally."""
    if number <= 2:
        return 1

    current, previous = 1, 1

    for _ in range(3, number + 1):
        previous, current = current, current + previous

    return current


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level

The fibonacci function is defined on line 44, and has one parameter, number,
which expects an int.

The if conditional statement on line 46 handles the base cases when number is
1 or 2, and in these cases, returns 1 on line 47.

On line 49, two local variables are defined, current and pevious, and both set
to 1.

The for loop on line 51 begins at 3, since cases 1 and 2 are already handled,
and loops until the number inclusively. Within the context of the loop,
the current is assigned to the sum of itself and previous, and previous is
assigned to the previous value of current.

After the for loop finishes, current is returned.

User Level

Fiboonacci takes in a number, representing the nth fibonacci number desired,
performs the fibonacci sequence, and returns the nth fibonacci number.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert fibonacci(1) == 1
        assert fibonacci(2) == 1
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8
        assert fibonacci(12) == 144
        assert fibonacci(20) == 6765
        assert fibonacci(50) == 12586269025
        assert fibonacci(75) == 2111485077978050
