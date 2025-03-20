"""
Create a function that returns the count of distinct case-insensitive
alphabetic characters and numeric digits that occur more than once in the
input string. You may assume that the input string contains only
alphanumeric characters.

P
    inputs: str
    outputs: int
    rules:
        Explicit Reqs:
            - accept a str
            - return an int
            - return int is the count of all duplicate chars in the str
            - duplicate is case-insensitive
            - input_str only has alphanumeric chars
        Implicit Reqs:
            - empty string returns 0
E
    (see test cases below)
D
    dict
A
    - coerce input_str to lowercase
    - create a `duplicates` dict
    - iterate through input_str
        - if the current char is not in duplicates. add it with the value
          False
        - if it is in it, set to True
    - return the count of duplicates
C
"""


def distinct_multiples(input_str: str) -> int:
    """
    Returns the count of case-insensitive dictinct multiples in the input str.
    """
    duplicate_chars = {}
    input_str = input_str.lower()

    for char in input_str:
        if char not in duplicate_chars:
            duplicate_chars[char] = False
        else:
            duplicate_chars[char] = True

    return len([dup for dup in duplicate_chars.values() if dup])


if __name__ == "__main__":
    assert distinct_multiples('xyz') == 0
    assert distinct_multiples('xxyypzzr') == 3
    assert distinct_multiples('xXyYpzZr') == 3
    assert distinct_multiples('unununium') == 2
    assert distinct_multiples('multiplicity') == 3
    assert distinct_multiples('7657') == 1
    assert distinct_multiples('3141592653589793') == 4
    assert distinct_multiples('2718281828459045') == 5
