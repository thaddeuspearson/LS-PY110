"""
Write a function that returns a list of all palindromic substrings of a
string. That is, each substring must consist of a sequence of characters that
reads the same forward and backward. The substrings in the returned list
should be sorted by their order of appearance in the input string. Duplicate
substrings should be included multiple times.

You may (and should) use the substrings function you wrote in the previous
exercise.

For the purpose of this exercise, you should consider all characters and pay
attention to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA'
are not. In addition, assume that single characters are not palindromes.

P
    inputs: string
    outputs: list of palindromic substrings
    rules:
        Explicit Reqs:
            - accept a string
            - use substrings function
            - single char substrs are not palindromes
            - case matters
            - include repeated palindromic substrs

        Implicit Reqs:
            - an empty string returns an empty list
E
    palindromes('abcd') == []
    palindromes('madam') == ['madam', 'ada']
    palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ]
    palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ]
D
    list
A
    - create a return list
    - loop though each index of string with enumerate
    - with each iteration, call substrings on the slice of string starting
      with i
    - loop through all substrings
        - check to see if it is a palindrome with slicing
            - if so, append to the return list
    - return the return list
C
"""
import sys
from all_substrings import substrings


def palindromes(input_str: str) -> list:
    """Returns all palindromic substrings"""
    return [s for s in substrings(input_str) if s == s[::-1] and len(s) > 1]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
On line 63, a list comprehension is created by looping through call to the
substrings function with string given as an argument. With each iteration,
s is checked against two conditions, that it is a palindrome (using slicing),
and that its length is longer than 1. The resulting list is returned.

User Level
Palindromes takes a string and returns a list of all substrings that are
palindromes.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert palindromes('abcd') == []
        assert palindromes('madam') == ['madam', 'ada']
        assert palindromes('hello-madam-did-madam-goodbye') == [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo'
        ]
        assert palindromes('knitting cassettes') == [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt'
        ]
