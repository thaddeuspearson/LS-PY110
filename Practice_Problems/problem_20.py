"""
Create a function that takes a list of numbers, all of which are the same
except one. Find and return the number in the list that differs from all the
rest.

The list will always contain at least 3 numbers, and there will always be
exactly one number that is different.

P
    inputs: list
    outputs: int
    rules:
        Explicit Reqs:
            - accept a list of numbers
            - return an int
            - return int is the only different number in the num_list
            - num_list has at least 3 numbers
            - there is exactly one number that is different
E
    (see test cases below)
D
    set
A
    - create num_1, set equal to the num at index 0
    - create num_2, set equal to None
    - iterate through the num_list starting at index 1
        - if the curr_num is not equal to num_1 and num_2 is None
            - set num_2 = curr_num
        - else if the curr_num is equal to num_1 and num_2 is not None:
            - return num_2
        - else if the curr_num is equal to num_2
            - return num_1
C
"""


def what_is_different(num_list: list) -> int | float:
    """
    Returns the unique element in the num_list.
    """
    num_1 = num_list[0]
    num_2 = None

    for i, curr_num in enumerate(num_list):
        if curr_num != num_1 and num_2 is None:
            if i == len(num_list) - 1:
                return curr_num
            num_2 = curr_num
        elif curr_num == num_1 and num_2 is not None:
            return num_2
        elif curr_num == num_2:
            return num_1


if __name__ == "__main__":
    assert what_is_different([0, 1, 0]) == 1
    assert what_is_different([7, 7, 7, 7.7, 7]) == 7.7
    assert what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11
    assert what_is_different([3, 4, 4, 4]) == 3
    assert what_is_different([4, 4, 4, 3]) == 3
