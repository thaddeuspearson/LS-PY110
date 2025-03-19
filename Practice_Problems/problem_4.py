"""
Create a function that takes a list of integers as an argument and returns a
tuple of two numbers that are closest together in value. If there are multiple
pairs that are equally close, return the pair that occurs first in the list.

P
    inputs: list of integers
    outputs: tuple of two numbers
    rules:
        Explicit Reqs:
            - accept a list
            - return tuple
            - return tuple should have 2 elements
            - return tuple should be the two ints in the input list that are
              closest together
            - if multiple pairs have the same difference, return the pair that
              occurs first in the list
        Implicit Reqs:
            - an empty list returns an empty tuple
            - Don't modify the input list
        Questions:
            - How to determine "first" in the list?
                - both elements, or only a single element?
            - Account for pairs of the same number?
E
    assert closest_numbers([5, 25, 15, 11, 20]) == (15, 11)
    assert closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27)
    assert closest_numbers([12, 22, 7, 17]) == (12, 7)
D

A
    - create a `closest_difference` variable, set to infinity
    - create a `closest_pair` variable, initialize to None
    - for each pair in the input list
        - calculate the absolute value of the difference of the pair
        - if the difference is less than the closest_difference
            - assign closest_difference to the current_difference
            - assign pair to closest_pair
        - if the curr_difference is equal to the closest_difference:
            - if the index of both elemts in the pair are lower than
              the indexes of the closest_pair:
                - assign pair to closest_pair
    - return the closest_pair
C
"""


def closest_numbers(input_lst: list) -> list:
    """
    Returns the closest pair of numbers in the given list. If there is a tie,
    the pair where both elements come first will be returned.
    """
    closest_pair = ()
    closest_pair_second_idx = len(input_lst)
    closest_diff = float('inf')

    for i in range(len(input_lst) - 1):
        for j in range(i+1, len(input_lst)):
            num_1 = input_lst[i]
            num_2 = input_lst[j]
            curr_pair = num_1, num_2
            curr_diff = abs(num_1 - num_2)

            if curr_diff < closest_diff or \
               curr_diff == closest_diff and j < closest_pair_second_idx:
                closest_pair = curr_pair
                closest_diff = curr_diff
                closest_pair_second_idx = j

    return closest_pair


if __name__ == "__main__":
    assert closest_numbers([5, 25, 15, 11, 20]) == (15, 11)
    assert closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27)
    assert closest_numbers([12, 22, 7, 17]) == (12, 7)
    assert closest_numbers([1, 2, 3, 2, 3, 1]) == (2, 2)
