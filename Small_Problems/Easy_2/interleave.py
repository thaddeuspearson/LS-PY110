"""
Write a function that combines two lists passed as arguments and returns a new
list that contains all elements from both list arguments, with each element
taken in alternation. You may assume that both input lists are non-empty, and
that they have the same number of elements.
"""
import sys


def interleave(list_1, list_2):
    """Returns a single list with the elements of list_1 and list_2 together.

    :param list_1 (list<many>): The first list to interleave
    :param list_2 (list<many>): The second list to interleave
    :returns (list): the interleaven list"""
    return [elem for tpl in zip(list_1, list_2) for elem in tpl]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
interleave is defined on line 10. It has 2 parameters, list_1 and list_2.

This one liner is on line q6. First, list_1 and list_2 are zipped together
using zip. The outer loop goes through each tuple pair. The inner loop then
iterates through each tuple pait, and adds both members to the list
comprehension. At the end of execution of the loops, the resulting list is
finally returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        expected = [1, "a", 2, "b", 3, "c"]
        assert interleave(list1, list2) == expected
    else:
        print()
