"""
Create a function that takes a list of integers as an argument. The function
should return the minimum sum of 5 consecutive numbers in the list. If the
list contains fewer than 5 elements, the function should return None.
P
    inputs: list
    outputs: list
    rules:
        Explicit Reqs:
            - accept a list
            - return an int | None
            - return int should be minimum sum of 5 elements or
              None if the list has less than 5 elems
            - minimum sum is made of 5 consecutive elements
        Implicit Reqs:
            - Don't modify the input lst
E
    minimum_sum([1, 2, 3, 4]) is None
    minimum_sum([1, 2, 3, 4, 5, -5]) == 9
    minimum_sum([1, 2, 3, 4, 5, 6]) == 15
    minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16
    minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10
D
    None
A
    - create start and end variables
      start is 0, end = 5
    - create a min_sum var set equal to None
    - loop until end == length of the input list
        - sum a slice starting at start and end
        - compare to min_sum, replace if it is less or None
    return min_sum
C
"""


def minimum_sum(lst: list) -> int:
    """
    Returns the minimum sum of 5 consecutive elements in the given list, or
    None if the given list has a length less than 5
    """
    start = 0
    min_sum = None

    for end in range(5, len(lst)+1):
        if min_sum is None:
            curr_sum = sum(lst[start:end])
            min_sum = curr_sum
        else:
            curr_sum += lst[end - 1] - lst[start - 1]
            min_sum = min(curr_sum, min_sum)

        start += 1

    return min_sum


if __name__ == "__main__":
    assert minimum_sum([1, 2, 3, 4]) is None
    assert minimum_sum([1, 2, 3, 4, 5, -5]) == 9
    assert minimum_sum([1, 2, 3, 4, 5, 6]) == 15
    assert minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16
    assert minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10
