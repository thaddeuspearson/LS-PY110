"""
Implement a binary_search function that takes a list and a search item as
arguments, and returns the index of the search item if found, or -1 otherwise.
You may assume that the list argument will always be sorted.

P
    inputs: list
    outputs: int
    rules:
        Explicit Reqs:
            - accept a list
            - return an int
            - int should be the index of the elem to find or -1
            - the input list will always be sorted
        Implicit Reqs:
            - an empty list returns -1
E
    businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
    assert binary_search(businesses, 'Pizzeria') == 7
    assert binary_search(businesses, 'Apple Store') == 0

    assert binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1
    assert binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6
    assert binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1

    names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler']
    assert binary_search(names, 'Peter') == -1
    assert binary_search(names, 'Tyler') == 6
D
    None
A
    - base case, return -1 if the to_search is empty
    - find the midpoint element of the list
    - check if the midpoint elem is the elem to find, return the idx if True
    - check if the midpoint elem is greater than the elem to find, call
      binary_search on a beginning slice to the midpoint of the current list
    - handle the opposite case of above
C
"""
import sys


def binary_search(to_search: list, to_find: int | str) -> int:
    """Returns the index of the element, or -1 if not found"""
    if not to_search:
        return -1

    mid = (len(to_search) - 1) // 2
    curr_elem = to_search[mid]

    if curr_elem == to_find:
        return mid
    if to_find < curr_elem:
        return binary_search(to_search[:mid], to_find)
    result = binary_search(to_search[mid+1:], to_find)
    return result + mid+1 if result != -1 else result


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

On line 46, binary_search is defined with 2 parameters, to_seach and to_find,
which expect a list and an int | str respectively.

On line 48 an if conditional statement checks to make sure to_search is not
empty. if it is, -1 is returned.

On line 51, a local variable mid is defined as the middle index of to_search.
On line 52, a local variable curr_elem is assigned to the elem at the mid idx.

On line 54, an if conditional statem,emnt checks to see if curr_elem equals
to_find, and if so, the idx (mid) is returned.

On line 56, an if conditional statement checks to see if to_find is less
than the curr_elem, and if so recursively calls binary_search with a slice of
to_search up until the midpoint.

On line 58/59, the opposite case is handled, to_find is greater than curr_elem
mid + 1 is added to the return statement here to account for the slicing, but
only in the case that the return value is not -1.


User Level:
Binary_search takes a list to search through, and an element to search for, and
recursively calls binary_search until the element is found, and its index is
returned. -1 is returned if the item does not appear in the list.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        businesses = [
            'Apple Store', 'Bags Galore', 'Bike Store',
            'Donuts R Us', 'Eat a Lot', 'Good Food',
            'Pasta Place', 'Pizzeria', 'Tiki Lounge', 'Zooper'
        ]
        assert binary_search(businesses, 'Pizzeria') == 7
        assert binary_search(businesses, 'Apple Store') == 0

        assert binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1
        assert binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6
        assert binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1

        names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler']
        assert binary_search(names, 'Peter') == -1
        assert binary_search(names, 'Tyler') == 6
