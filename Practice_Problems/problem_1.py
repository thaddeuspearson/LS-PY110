"""
Create a function that takes a list of numbers as an argument. For each
number, determine how many numbers in the list are smaller than it, and
place the answer in a list. Return the resulting list.

P
    inputs: list
    outputs: list
    rules:
        Explicit Reqs:
            - accept a list
            - return a list
            - return list should be the count of elems that are less than the
              element at each index
        Implicit Reqs:
            - an empty list returns an empty list
E
    smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2]
    smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0]
    smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3]
    smaller_numbers_than_current([1]) == [0]

    my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
    result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
    smaller_numbers_than_current(my_list) == result
D
    sset orted list
A
    - create a return list
    - create a set from the list
    - coerce the set to a list and sort in ascending order
    - iterate through the given list
        - find the index of the current element in the sorted list
        - push the index to the return list
    return the return list
C
"""


def smaller_numbers_than_current(lst: list) -> list:
    """
    Returns the number of list elems that are in the list that are less
    than the element at the current index
    """
    sorted_unique_nums = sorted(set(lst))
    return [sorted_unique_nums.index(num) for num in lst]


if __name__ == "__main__":
    assert smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2]
    assert smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0]
    assert smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3]
    assert smaller_numbers_than_current([1]) == [0]

    my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
    result = [0, 2, 4, 5, 6, 1, 2, 3, 2]
    assert smaller_numbers_than_current(my_list) == result
