"""
Write a function that takes a string, doubles every consonant in the string,
and returns the result as a new string. The function should not double vowels
('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.
"""
import sys


CONSONANTS = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}


def double_consonants(input_str: str) -> str:
    """Returns only consonants in the input_str doubled.

    :param input_str (str): the string to double the consonants
    :returns (str): the doubled consonant string"""
    return "".join([c*2 if c.lower() in CONSONANTS else c for c in input_str])


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
double_consonants is defined on line 15, and has one parameter, input_str.

This one-liner joins a list comprehension created from interating through the
input_str, checking each character to see if it is a consonant, and doubling
it if it is, otherwise leaving it as a single character if it is not.

The resulting string is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert double_consonants('String') == "SSttrrinngg"
        assert double_consonants('Hello-World!') == "HHellllo-WWorrlldd!"
        assert double_consonants('July 4th') == "JJullyy 4tthh"
        assert double_consonants('') == ""
