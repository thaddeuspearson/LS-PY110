"""
Write a function that returns True if the string passed as an argument is a
palindrome, False otherwise. A palindrome reads the same forwards and
backwards. For this problem, the case matters and all characters matter.
"""
import sys


def is_palindrome(word=None):
    """Determines if the given word is a palindrome.

    :param word (str): the given word to check
    :returns bool: True/False respectively if word is a palindrome
    """
    if not word:
        word = input("Please enter a string: ")
    return word == word[::-1]


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
is_palindrome defined on line 9 has one parameter word, which has a default
value of None. the conditional on line 15 checks to see if any input has been
passed as an argument to word, and if not, prompts the user for a string.

The return statement on line 17 explicitly checks whether word is identical to
the reversed string representation of word and returns the resulting boolean.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert is_palindrome('madam') is True
        assert is_palindrome('356653') is True
        assert is_palindrome('356635') is False
        assert is_palindrome('Madam') is False
        assert is_palindrome("madam i'm adam") is False
    else:
        print(is_palindrome())
