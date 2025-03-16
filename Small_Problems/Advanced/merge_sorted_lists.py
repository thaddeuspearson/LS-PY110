"""
Write a function that takes two sorted lists as arguments and returns a new
list that contains all the elements from both input lists in ascending sorted
order. You may assume that the lists contain either all integer values or all
string values.

You may not provide any solution that requires you to sort the result list.
You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

P
    inputs: list
    sorted_lists: list
    rules:
        Explicit Reqs:
            - accept a list
            - return a list
            - return list should be sorted in ascending order
            - do not use any built-in sort methods
            - do not mutate the starting lists
        Implicit Reqs:
            - empty list should return an empty list
            - one empty list should return the non-empty list
E
    assert merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9]
    assert merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3]
    assert merge([], [1, 4, 5]) == [1, 4, 5]
    assert merge([1, 4, 5], []) == [1, 4, 5]

    names1 = ['Alice', 'Kim', 'Pete', 'Sue']
    names2 = ['Bonnie', 'Rachel', 'Tyler']
    names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                    'Rachel', 'Sue', 'Tyler']
    assert merge(names1, names2) == names_expected
D
    None
A
    - create a return list
    - Create two pointer indexes
    - loop while both idxes are less than the len of respective lists
        - append the least of the curr elements the indxes are pointing at
        - increment the idx that was just appended
    - if any elements still exist the other list, append them to return list
    - return return list
C
"""
import sys


def merge(lst_1: list, lst_2: list) -> list:
    """
    Merges the two given lists in sorted order, without using built-in sort
    methods
    """
    sorted_list = []
    i, j = 0, 0
    len_1, len_2 = len(lst_1), len(lst_2)

    while i < len_1 and j < len_2:
        curr_1 = lst_1[i]
        curr_2 = lst_2[j]

        if curr_1 <= curr_2:
            sorted_list.append(curr_1)
            i += 1
        else:
            sorted_list.append(curr_2)
            j += 1

    sorted_list.extend(lst_1[i:])
    sorted_list.extend(lst_2[j:])

    return sorted_list


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:
The merge function is defined on line 51, and takes two parameters, lst_1 and
lst_2, both of which expect a sorted list.

On line 56, a local variable sorted_list is creataed and assigned an empty
list literal.
On line 57, 2 local variables, i and j, are assigned to the value 0.
On line 58, 2 local variables, len_1 and len_2 are assigned to the lengths of
each list respectively.

A while loop with the conditional expression ensuring that i and j are less
than their corresponding list_lens is defined.

On lines 61 and 62, 2 local variables, curr_1 and curr_2, are defined and
initialized to the value of the element at indexes i and j in their respective
lists. This is done to cut down on list lookups.

On lines 64-69, curr_1 and curr_2 are compared in an if/ese conditional block.
This block ensures that the minimum element is appended to the sorted_list and
increments the corresponding index by 1.

Finally, sorted_list is extended by any remaining list elements on lines 71
and 72, and the sorted_list is returned on line 74.


User Level:

Merge takes 2 sorted lists, and merges them together while maintaining the
sorted order. A while loop continues to append the correct list elements in
sorted order, any remaining list elements are appended after the shorter list
is exhausted and one final sorted list is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9]
        assert merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3]
        assert merge([], [1, 4, 5]) == [1, 4, 5]
        assert merge([1, 4, 5], []) == [1, 4, 5]
        assert not merge([], [])

        names1 = ['Alice', 'Kim', 'Pete', 'Sue']
        names2 = ['Bonnie', 'Rachel', 'Tyler']
        names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                          'Rachel', 'Sue', 'Tyler']
        assert merge(names1, names2) == names_expected
