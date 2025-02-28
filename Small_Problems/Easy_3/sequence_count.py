"""
Create a function that takes two integers as arguments. The first argument is
a count, and the second is the starting number of a sequence that your
function will create. The function should return a list containing the same
number of elements as the count argument. The value of each element should be
a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 
0. The starting number can be any integer. If the count is 0, the function
should return an empty list.
"""
import sys


def sequence_count(seq_len: int, count_by: int) -> list:
    """Returns a list of integers in a sequence starting at the argument
    provided to count_by, and ending inclusively at the argument provided
    to seq_len.

    :param seq_len (int): the desired length of the sequence
    :param count_by (int): the start of the sequence, and the amount to
                           increment by
    :returns (list): the sequence starting at count_by
    """
    start = count_by
    stop = count_by * seq_len
    stop += 1 if count_by > 0 else -1
    return ([0 for _ in range(seq_len)] if count_by == 0
            else list(range(start, stop, count_by)))


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
sequence is defined on line 15, and has 2 parameters, seq_len, and count_by.
Both parameters expect integer arguments.

On line 25, a local variable start is instantiated with the count_by local
variable, meaning that they both point to the same integer in memory.

On line 26, the local variable stop is instantiated to the result of
multiplying count_by with seq_len. On line 27, stop is either incremented or
decrememnted by 1 depending on if count_by is positive or negative
respectively. This will ensure that the range is inclusive of the final
sequence element.

On line 28, a list comprehension resulting in exactly count_by 0s is returned
in the case that count_by is a 0. If not, the range method is invoked with
start, stop, and count_by respectfully. The resulting range object is coerced
to a list and then returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert sequence_count(5, 1) == [1, 2, 3, 4, 5]
        assert sequence_count(4, -7) == [-7, -14, -21, -28]
        assert sequence_count(3, 0) == [0, 0, 0]
        assert not sequence_count(0, 1000000)
