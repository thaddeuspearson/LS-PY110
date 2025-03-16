"""
Write a function that takes a list as an argument and sorts that list using
the bubble sort algorithm described above. The sorting should be done
"in-place" -- that is, the function should mutate the list. You may assume
that the list contains at least two elements.

P
    inputs: list
    outputs: list
    rules:
        Explicit Reqs
            - accept a list
            - return a list
            - return list should be the same list as input list
            - list should be sorted using bubble sort
        Implicit Reqs:
            - an empty list should return an empty list
E
    lst1 = [5, 3]
    bubble_sort(lst1)
    lst1 == [3, 5]

    lst2 = [6, 2, 7, 1, 4]
    bubble_sort(lst2)
    lst2 == [1, 2, 4, 6, 7]

    lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
    bubble_sort(lst3)

    expected = ["Alice", "Bonnie", "Kim", "Pete",
                "Rachel", "Sue", "Tyler"]
    lst3 == expected
D
    list
A
    - create a `swap_occurred` boolean to False
    - loop continuously while swap_occurred is false
        - interate through the list
            - check the current number, and next number
              and ensure they are in correct order, or swap
                - if swap occurred, set swap_occurred to True
        - check the `swap_occured` boolean
            - if no swap occurred, return the list
            - if a swap occurred, reset swap occurred
C
"""
import sys


def bubble_sort(lst: list) -> list:
    """Sorts the given list in place with Bubble-sort"""
    while True:
        swap_occurred = False

        for idx, num in enumerate(lst):
            if idx < len(lst) - 1:
                if num > lst[idx+1]:
                    temp = num
                    lst[idx] = lst[idx+1]
                    lst[idx+1] = temp
                    if not swap_occurred:
                        swap_occurred = True
        if not swap_occurred:
            return lst


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

bubble_sort is defined on line 51 with one parameter, lst, which expects a
list.

On line 53, a while loop will loop infinately.

In the context of the while loop, on line 54 a local variable called
swap_occurred is instantiated as False.

On line 56, a for loop iterates through an enumeration of list, assigning
local variables idx, and num with the associated values from the enumeration.

Line 57 is the first if condtional check, making sure that the current num is
not the final num in lst, using len() and <.

Line 58 is the second if conditional check, looking to see if num is greater
than the next number. If it is, on lines 59 - 61 the swap operation trades
the nums with each other in the list order.

On line 62, swap_occurred is checked to see if it is still False, if so, it is
flipped to True.

On line 64, swap_occurred is evaluated with an if not statement, in this case,
the sorted list is returned.


User Level:

Bubble sort takes a list and sorts it by comparing each elem with the next, and
swapping their order if the first num is less than the second num. This process
is repeated oer and over again until the list is sorted in ascending order.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        lst1 = [5, 3]
        bubble_sort(lst1)
        assert lst1 == [3, 5]

        lst2 = [6, 2, 7, 1, 4]
        bubble_sort(lst2)
        assert lst2 == [1, 2, 4, 6, 7]

        lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
                'Kim', 'Bonnie']
        bubble_sort(lst3)

        expected = ["Alice", "Bonnie", "Kim", "Pete",
                    "Rachel", "Sue", "Tyler"]
        assert lst3 == expected
