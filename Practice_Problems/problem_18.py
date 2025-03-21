"""
Create a function that takes a list of integers as an argument. Determine and
return the index N for which all numbers with an index less than N sum to the
same value as the numbers with an index greater than N. If there is no index
that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the
smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the
numbers to the right of the last element is 0.

P
    inputs: list
    outputs: int
    rules:
        Explicit Reqs:
            - accept a list
            - return an int
            - return int is the smallest index where the numbers on both sides
              of the given index sum to the same number.
            - return -1 if this does not exist in the given num_list
        Implicit Reqs:
            - dont modify the input_nums
E
    (see test cases below)
D
    None
A
    - iterate through the length of the nums_list
        - compare the sums on both sides of the given index
            - if equal, return the index
C
"""


def equal_sum_index(num_list: list) -> int:
    """
    Returns the index of the element where the sums of the numbers on both
    sides of the element are exactly equal (excluding the curr elem), or -1
    """
    for i, _ in enumerate(num_list):
        left_side = sum(num_list[:i])
        right_side = sum(num_list[i+1:])

        if left_side == right_side:
            return i

    return -1


if __name__ == "__main__":
    assert equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3
    assert equal_sum_index([7, 99, 51, -48, 0, 4]) == 1
    assert equal_sum_index([17, 20, 5, -60, 10, 25]) == 0
    assert equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1

    # The following test case could return 0 or 3. Since we're
    # supposed to return the smallest correct index, the correct
    # return value is 0.
    assert equal_sum_index([0, 20, 10, -60, 5, 25]) == 0
