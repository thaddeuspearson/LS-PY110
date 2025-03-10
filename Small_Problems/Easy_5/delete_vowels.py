"""
Write a function that takes a list of strings and returns a list of the same
string values, but with all vowels (a, e, i, o, u) removed.

P
    inputs: list
    outputs: list
    rules:
        Explicit Reqs:
            - accept a list of strings
            - return a list of strings
            - remove all vowels in the strings
        Implicit Reqs:
            - an empty list returns an empty list
E
    original = ['abcdefghijklmnopqrstuvwxyz']
    expected = ['bcdfghjklmnpqrstvwxyz']
    remove_vowels(original) == expected

    original = ['green', 'YELLOW', 'black', 'white']
    expected = ['grn', 'YLLW', 'blck', 'wht']
    remove_vowels(original) == expected

    original = ['ABC', 'AEIOU', 'XYZ']
    expected = ['BC', '', 'XYZ']
    remove_vowels(original) == expected
D
    list
A
    - create a vowels set
    - iterate through the list
    - iterate through the string
    - save chars that are not vowels
    - add vowel-less strings to return list
    - return the list
C
"""
import sys


VOWELS = {'a', 'e', 'i', 'o', 'u'}


def remove_vowels(strings: list) -> list:
    """Removes the vowels from the strings in a list"""
    return [
        ''.join(c for c in s if c.lower() not in VOWELS) for s in strings
    ]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
The function remove_vowels is defined on line 44, and has one parameter,
strings, which expects a list of strings.

On line 46, a list comprehension is created, which iterates through strings (s)
then through each char (c), transforms c to lowercase, and checks to see if it
is in VOWELS. If it is not, c is saved. join puts the all of the chars together
and the resulting string is appended to the list comprehension.

The resulting list comprehension is returned.


User Level
Remove_vowels takes a list of strings, and returns a new list with all the
vowels removed from the strings in the list.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        original = ['abcdefghijklmnopqrstuvwxyz']
        expected = ['bcdfghjklmnpqrstvwxyz']
        assert remove_vowels(original) == expected

        original = ['green', 'YELLOW', 'black', 'white']
        expected = ['grn', 'YLLW', 'blck', 'wht']
        assert remove_vowels(original) == expected

        original = ['ABC', 'AEIOU', 'XYZ']
        expected = ['BC', '', 'XYZ']
        assert remove_vowels(original) == expected
