"""
Write another function that returns True if the string passed as an argument
is a palindrome, or False otherwise. This time, however, your function should
be case-insensitive, and should ignore all non-alphanumeric characters. If you
wish, you may simplify things by calling the is_palindrome function you wrote
in the previous exercise.
"""
import sys
from is_palindrome import is_palindrome


def is_real_palindrome(word=None):
    """Determines if the given word is a real palindrome. A real palindrome
     ignores non alphanumeric characters and is case insensitive

    :param word (str): the given word to check
    :returns bool: True/False respectively if word is a real palindrome
    """
    if not word:
        word = input("Please enter a string: ")
    filtered_word = "".join([c.lower() for c in word if c.isalnum()])
    return is_palindrome(filtered_word)


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
is_real_palindrome has one parameter word, which expectss a string. The
conditional statement on line 19 checks to see if an argument has been
provided to the word paramenter, and if not, prompts the user for a string.

The local variable filterd_word on line 21 is instantiated with the join
method being called on a list comprehension which loops through each character
of word and checks if it is an alphanumeric character, and if it is, changes
it to lowercase.

On line 22, the is_palindrome function is called with filtered_word and the
return value from that function call is returned in the function scope of
is_real_palindrome.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert is_real_palindrome('madam') is True
        assert is_real_palindrome('356653') is True
        assert is_real_palindrome('356635') is False
        assert is_real_palindrome('356a653') is True
        assert is_real_palindrome('123ab321') is False
        assert is_real_palindrome('Madam') is True
        assert is_real_palindrome("Madam, I'm Adam") is True
    else:
        print(is_real_palindrome())
