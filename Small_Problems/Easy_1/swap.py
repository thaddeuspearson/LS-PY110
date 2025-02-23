"""
Given a string of words separated by spaces, write a function that swaps the
first and last letters of every word. You may assume that every word contains
at least one letter, and that the string will always contain at least one
word. You may also assume that each string contains nothing but words and
spaces, and that there are no leading, trailing, or repeated spaces.
"""
import sys


def swap(words=None):
    """Returns the given string with each word having the first and last
    characters swapped.

    :param words (str): the words to swap
    :returns str: the words with the first and last characters swapped
    """
    if words is None:
        words = input("Please enter a string: ")

    swapped_words = []

    for word in words.split():
        swapped = word[-1] + word[1:-1] + word[0] if len(word) > 1 else word
        swapped_words.append(swapped)

    return " ".join(swapped_words)


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
swap is defined on line 11, and accepts a single parameter, words, which
accepts a string. The conditional on line 18 checks to see if any input has
ben provided to words, and prompts the user to input a string if not.

On line 21, a local variable swapped_words is instantiated with an empty list
literal.

The for loop on line 23 interates through each word, and swaps the first and
last characters with the logic on line 24. The else statement covers the edge
case that the curent word is only 1 character in length. The swapped word is
appended to swapped_words on line 25.

On line 27, swapped_words is joined together with a space character as the
delimiter, and the resulting string is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert swap('Oh what a wonderful day it is') \
                    == "hO thaw a londerfuw yad ti si"
        assert swap('Abcde') == "ebcdA"
        assert swap('a') == "a"
    else:
        print(swap())
