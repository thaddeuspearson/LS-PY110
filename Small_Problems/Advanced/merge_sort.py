"""
Write a function that takes a list argument and returns a new list that
contains the values from the input_list list in sorted order. The function
should sort the list using the merge sort algorithm as described above. You may
assume that every element of the list will have the same data type: either all
numbers or all strings.

Feel free to use the merge function you wrote in the previous exercise.
P
    input_lists: list
    outputs: list
    rules:
        Explicit Reqs:
            - accept a list
            - return a list
            - return list should be sorted in order
        Implicit Reqs:
            - an empty list should return an empty list
E
    assert merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9]
    assert merge_sort([5, 3]) == [3, 5]
    assert merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7]
    assert merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9]

    original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
    expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler']
    assert merge_sort(original) == expected

    original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46]
    expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54]
    assert merge_sort(original) == expected
D
    list
A
    - create base case
        if the length of the first element is 1, return a call to merge
    - create recursive case
        - divide the list in half
        - call merge_sort on the two halves
        - return a call to merge with the halves

C
"""
import sys
from merge_sorted_lists import merge


def merge_sort(input_list: list) -> list:
    """
    Uses the merge sort alrogithm to sort the given input_list list in
    ascending order
    """
    if len(input_list) == 1:
        return input_list

    first_half = input_list[:len(input_list) // 2]
    second_half = input_list[len(input_list) // 2:]

    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

    return merge(first_half, second_half)


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

The merge_sort function is defined on line 48, and has one parameter,
input_list, which expects a list.

On line 53, a base case is established, checking to see if the length of the
list is exactly 1. if it is, then the input_list list is returned.

Lines 56 and 57 split the input_list list into 2 pieces with slicing.

Lines 59 and 60 recursively call the merge_sort functions with both halves.

Finally, on line 62, merge is called with the 2 halves to put the lists in
sorted order.


User Level:
Merge_sort takes a list of elements, and sorts the input_list list by
splitting it into halves, until only lists of one element remain. Then, each
single elem list is merged together with its corresponding half repeatedly,
until all the pieces are put back together in sorted order.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9]
        assert merge_sort([5, 3]) == [3, 5]
        assert merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7]
        assert merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9]

        original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie']
        expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler']
        assert merge_sort(original) == expected

        original = [7, 3, 9, 15, 23, 1, 6, 51, 22,
                    37, 54, 43, 5, 25, 35, 18, 46]
        expected = [1, 3, 5, 6, 7, 9, 15, 18, 22,
                    23, 25, 35, 37, 43, 46, 51, 54]
        assert merge_sort(original) == expected
