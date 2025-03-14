"""
Given this recursive algorithm, try to write a recursive function that
computes the nth Fibonacci number, where nth is an argument passed to
the function.

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
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(12) == 144
    assert fibonacci(20) == 6765
D
    None
A
    - handle base cases when number is 1 or 2
    - return fibonacci called on n - 1 plus fibonacci on n - 2
C
"""
import sys


def fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number recursively."""
    return 1 if n <= 2 else fibonacci(n - 1) + fibonacci(n - 2)


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level

On line 37 the fibonacci function is defined with 1 parameter, n, which
expects an int.

The one liner on line 39 leverages a ternary statement, which returns 1 in the
base case that n is either 1 or 2, or peforms the fibonacci sequence by
recursively calling fibonacci on n - 1, and adding that with fibonacci called
on n - 2.

User Level

Fibonacci takes a number, and returns the nth fibonacci number recursively.
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
