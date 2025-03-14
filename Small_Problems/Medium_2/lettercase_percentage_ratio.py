"""
Write a function that takes a string and returns a dictionary containing the
following three properties:

    the percentage of characters in the string that are lowercase letters
    the percentage of characters that are uppercase letters
    the percentage of characters that are neither

All three percentages should be returned as strings whose numeric values lie
between "0.00" and "100.00", respectively. Each value should be rounded to two
decimal points.

You may assume that the string will always contain at least one character.

P
    inputs: str
    outputs: dict
    rules:
        Explicit Reqs:
            - accept a string
            - return a dict
            - return dict has 3 keys:
              "lowercase", "uppercase", "neither"
            - each key has the percentage of each category
              as a str representation of the float percentage
        Implicit Reqs:
            -  an empty string returns a dictionary with the keys
               having "0.00" values
E
    expected_result = {
        'lowercase': "50.00",
        'uppercase': "10.00",
        'neither': "40.00",
    }
    letter_percentages('abCdef 123') == expected_result

    expected_result = {
        'lowercase': "37.50",
        'uppercase': "37.50",
        'neither': "25.00",
    }
    letter_percentages('AbCd +Ef') == expected_result

    expected_result = {
        'lowercase': "0.00",
        'uppercase': "0.00",
        'neither': "100.00",
    }
    letter_percentages('123') == expected_result
D
    dict
A
    - create three counters (upper, lower, neither)
    - loop through the string
        - check if the char isalpha
            - if not increment neither
            - if it is
              - check if it isupper
                - if it is increment upper
                - else increment lower
    - format dict and return
C
"""
import sys


def format_percentage(counter: int, length: int) -> str:
    """Formats the percentage string"""
    return f"{counter / length * 100:.2f}"


def letter_percentages(string: str) -> dict:
    """
    Returns a dict indicating the letter percentages of upper, lower, and
    neither cases.
    """
    counters = {
        "lowercase": 0,
        "uppercase": 0,
        "neither": 0
    }

    for char in string:
        if char.isalpha():
            if char.isupper():
                counters['uppercase'] += 1
            else:
                counters["lowercase"] += 1
        else:
            counters["neither"] += 1

    return {k: format_percentage(v, len(string)) for k, v in counters.items()}


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION

"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        expected_result = {
            'lowercase': "50.00",
            'uppercase': "10.00",
            'neither': "40.00",
        }
        actual = letter_percentages('abCdef 123')
        assert letter_percentages('abCdef 123') == expected_result, actual

        expected_result = {
            'lowercase': "37.50",
            'uppercase': "37.50",
            'neither': "25.00",
        }
        assert letter_percentages('AbCd +Ef') == expected_result

        expected_result = {
            'lowercase': "0.00",
            'uppercase': "0.00",
            'neither': "100.00",
        }
        assert letter_percentages('123') == expected_result
