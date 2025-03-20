"""
Create a function that takes a list of integers as an argument and returns the
number of identical pairs of integers in that list. For instance, the number
of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For
instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2.
The first list contains two complete pairs while the second has an extra 2
that isn't part of the other two pairs.

P
    inputs: list of ints
    outputs: int
    rules:
        Explicit Reqs:
            - accept a list
            - return an int
            - return int should be the number of identical pairs
            - if the input list is less than 1 elem, return 0
            - count complete duplicate pairs only
        Implicit Reqs:
            - None
E
    (see tests below)
D
    - set
A
    - create `pairs_counter` initialize to 0
    - create an empty set `available_partner_nums`
    - iterate through the list
        - if the curr num is in the set
            - remove the num from the set and increment `pairs_counter`
        - else add the curr num to `available_partner_nums`
    - return `pairs_counter`
C
"""


def pairs(nums: list) -> int:
    """
    Returns the number of pairs of identical numbers exist in the given list.
    """
    pairs_counter = 0
    available_partner_nums = set()

    for n in nums:
        if n in available_partner_nums:
            available_partner_nums.remove(n)
            pairs_counter += 1
        else:
            available_partner_nums.add(n)
    return pairs_counter


if __name__ == "__main__":
    assert pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3
    assert pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4
    assert pairs([]) == 0
    assert pairs([23]) == 0
    assert pairs([997, 997]) == 1
    assert pairs([32, 32, 32]) == 1
    assert pairs([7, 7, 7, 7, 7, 7, 7]) == 3
