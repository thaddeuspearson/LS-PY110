"""
Write a function that calculates and returns the index of the first Fibonacci
number that has the number of digits specified by the argument. The first
Fibonacci number has an index of 1. You may assume that the argument is always
an integer greater than or equal to 2.

P
    inputs: int
    outputs: int
    rules:
        Explicit Reqs:
            -
        Implicit Reqs:
            -
E
    assert find_fibonacci_index_by_length(2) == 7
    assert find_fibonacci_index_by_length(3) == 12
    assert find_fibonacci_index_by_length(10) == 45
    assert find_fibonacci_index_by_length(16) == 74
    assert find_fibonacci_index_by_length(100) == 476
    assert find_fibonacci_index_by_length(1000) == 4782
    assert find_fibonacci_index_by_length(10000) == 47847
D
    None
A
    - create a fib_len variable and initialize at 0
    - crate a fib_idx and initialize at 0
    - While the fibonacci length is less than the length given
        - call fibonacci with the next integer
        - coerce the result to a str, and take the len
        - increment fib_idx
    - return fib_idx
C
"""
import sys
from fibonacci_memoization import fibonacci


def find_fibonacci_index_by_length(length: int) -> int:
    """
    Finds the fibononacci index of the first fibonacci number that
    has the given length. Note: Fibonacci indexes start at 1.
    """
    sys.set_int_max_str_digits(50_000)
    idx = 1

    while len(str(fibonacci(idx))) != length:
        idx += 1
    return idx


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level

On line 39, the find_fibonacci_index_by_length function is defined with 1
parameter, length, which expects an int.

Line 43 sets the max str digits to 50000.
On line 45, idx, a local variable, is created and set to 1.

Line 47 defines a while loop that will run until the result of calling
fibonacci on the current number's len (when coerced as a string) is equal to
the input length.

On line 48, idx is incremented by 1.

On line 59, after the while loop has finished executing, idx is returned.

User Level

Find_fibonacci_index_by_length takes an integer length, and calls fibonacci
until it reaches a number that has the given length, and returns the index of
that fibonacci number. Note Fibonacci indexes start at 1.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert find_fibonacci_index_by_length(2) == 7
        assert find_fibonacci_index_by_length(3) == 12
        assert find_fibonacci_index_by_length(10) == 45
        assert find_fibonacci_index_by_length(16) == 74
        assert find_fibonacci_index_by_length(100) == 476
        assert find_fibonacci_index_by_length(1000) == 4782
        assert find_fibonacci_index_by_length(10000) == 47847
