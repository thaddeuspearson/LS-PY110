"""
Create a function that takes a list of integers as an argument and returns the
integer that appears an odd number of times. There will always be exactly one
such integer in the input list.


P
    inputs: list
    outputs: int
    rules:
        Explicit Reqs:
            - accept a list of ints
            - return an int
            - return int should be the int that appears in the list an odd
              number of times
            - There is always exactly 1 int that appears an odd number of
              times
E
    (see test cases below)
D
    set
A
    - iterate through the nums_list
        - if the curr_num is not in the `odd_appearance`
            - add the number to odd_appearance
        - if it is, remove it from odd_appearance
    return odd_appearance[0]
C
"""


def odd_fellow(num_list: list) -> int:
    """
    Returns the num in the num list that appears an odd number of times.
    """
    odd_appearances = set()

    for num in num_list:
        if num not in odd_appearances:
            odd_appearances.add(num)
        else:
            odd_appearances.remove(num)
    return odd_appearances.pop()


if __name__ == "__main__":
    assert odd_fellow([4]) == 4
    assert odd_fellow([7, 99, 7, 51, 99]) == 51
    assert odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7
    assert odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6
    assert odd_fellow([0, 0, 0]) == 0
