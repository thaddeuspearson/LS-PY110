"""
Write a function that takes a list of numbers and returns a list with the same
number of elements, but with each element's value being the running total from
the original list.
"""
import sys


def running_total(input_list):
    """Creates a new list where each of the elements is the running total
    from all the preceding intergers in the input list.

    :param input_list (list<int>): the input list of integers
    :returns return_list (list<int>): the running totals of each element from
    the input list
    """
    total = 0
    return_list = []

    for num in input_list:
        total += num
        return_list.append(total)

    return return_list


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
running_total is defined on line 9 and has 1 parameter input_list. 2 local
variables are created on lines 10 and 11: total (instantiated to 0) and
return_list (instantiated to an empty list literal).

The for loop on line 13 loops through each number the input list, and with
each iteration, increments the total local variable by the current value of
num on line 14, and appends the current value of total to return_list.

After the loop is finished, return_list is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert running_total([2, 5, 13]) == [2, 7, 20]
        assert running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67]
        assert running_total([3]) == [3]
        assert not running_total([])
    else:
        print(running_total([int(n) for n in sys.argv[1:] if n.isdigit()]))
