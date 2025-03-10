"""
Write a function that takes a string as an argument and returns a list that
contains every word from the string, with each word followed by a space and
the word's length. If the argument is an empty string or if no argument is
passed, the function should return an empty list.

P
    inputs: string
    outputs: list
    rules:
        Explicit Reqs:
            - accept a string
            - return a list
            - list is words and their length, separated by a space
        Implicit Reqs:
            - an empty string should return an empty list
            - no input string should return an empty list
E
    words = 'cow sheep chicken'
    expected_result = ['cow 3', 'sheep 5', 'chicken 7']
    assert word_lengths(words) == expected_result

    words = 'baseball hot dogs and apple pie'
    expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                    'and 3', 'apple 5', 'pie 3']
    assert word_lengths(words) == expected_result

    words = "It ain't easy, is it?"
    expected_result = ['It 2', "ain't 5", 'easy, 5',
                    'is 2', 'it? 3']
    assert word_lengths(words) == expected_result

    big_word = 'Supercalifragilisticexpialidocious'
    assert word_lengths(big_word) == [f'{big_word} 34']

    assert word_lengths('') == []
    assert word_lengths() == []
D
    list, lookup dict
A
    - split the string
    - append the word and its len to a list
    - return the list
C
"""
import sys


def word_lengths(input_str: str = '') -> list:
    """returns the count of each word in the input string"""
    return [f"{word} {len(word)}" for word in input_str.split(" ") if word]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
The word_lengths function is defined on line 49, and has one parameter,
input_str, which expects a string.

On line 51, a list comprehension is created from iterating through the
input_str split on spaces, checking to see if word is truthy, and then using
string interpolation to create the required string and string len.

The resulting list is returned.


User Level
Word_lengths takes a string, and returns a list of all the words in the string
concatenated with how long each word is.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        test_words = 'cow sheep chicken'
        expected_result = [
            'cow 3', 'sheep 5', 'chicken 7'
        ]
        assert word_lengths(test_words) == expected_result

        test_words = 'baseball hot dogs and apple pie'
        expected_result = [
            'baseball 8', 'hot 3', 'dogs 4', 'and 3', 'apple 5', 'pie 3'
        ]
        assert word_lengths(test_words) == expected_result

        test_words = "It ain't easy, is it?"
        expected_result = [
            'It 2', "ain't 5", 'easy, 5', 'is 2', 'it? 3'
        ]
        assert word_lengths(test_words) == expected_result

        big_word = 'Supercalifragilisticexpialidocious'
        assert word_lengths(big_word) == [f'{big_word} 34']

        assert word_lengths('') == []
        assert word_lengths() == []
