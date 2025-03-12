"""
Write a function that takes a string as an argument and returns that string
with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three',
'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its
corresponding digit character.

You may assume that the string does not contain any punctuation.

P
    inputs: str
    outputs: str
    rules:
        Explicit Reqs:
            - accept a string
            - return a string
            - return string should have all int words replaced with int
              representations
        Implicit Reqs:
            - an empty string returns an empty string
E
    message = 'Please call me at five five five one two three four'
    word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4"

D
    lookup dictionary
A
    - create a number lookup dictionary
    - split the message to a list
    - check each word to see if it is in the lookup
        - if it is, replace it with the lookup value
    - join the list and return it
C

"""
import sys

NUMBERS = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}


def word_to_digit(message: str) -> str:
    """
    Returns the given string with all number words transformed to their
    string integer value
    """
    return ' '.join([
        NUMBERS[word.lower()]
        if word.lower() in NUMBERS else word
        for word in message.split(" ")
    ])


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level

On line 37, a number lookup dictionary is assigned to the constant NUMBERS,
with the keys being the english word for the given number, and the value being
the string representation of the integer number value.

The word_to_digit function is defined on line 43, and acceptes a single
parameter, message, which expects a string.

On line 48 a list comprehension is created and passed to the join function as
an argument.

In the comprehension, the word local variable is checked to see if it is a
number word. If it is, it is used as a key for the lookup dictionary and
returned to the comprehension, and if not, is simply returned to the
comprehension.

The final list created from joining the string  is returned.

User Level

Word_to_digit takes a message string, replaces any english integer words,
and replace them with their integer values.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        test_message = 'Please call me at five five five one two three four'
        assert word_to_digit(test_message) == "Please call me at 5 5 5 1 2 3 4"
