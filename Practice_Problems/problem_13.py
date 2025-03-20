"""
Create a function that takes two strings as arguments and returns True if some
portion of the characters in the first string can be rearranged to match the
characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic
characters. Neither string will be empty.

P
    input: two strings
    output: bool
    rules:
        Explicit Reqs:
            - accept 2 strings
            - return a bool
            - return bool indicates if a substr of the first string can be
              rearranged to create the second string
            - both strings will be lowercase alphabetic chars
            - none of the string args will be empty
E
    (see test cases below)
D
    dict

A
    - get `char_counts` of first string
    - iterate through second string
        - check char_counts for the current char
            - if it exists, and is not 0, decrement the char count
            - else return False
        - return True
C
"""


def get_char_counts(input_str: str) -> dict:
    """Returns a dictionary with the characters and their respective counts"""
    char_counts = {}

    for char in input_str:
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts


def unscramble(str_1: str, str_2: str) -> bool:
    """
    Returns if it is possible to rearrange some (or all) characters from the
    first string, and create the second string.
    """
    str_1_char_counts = get_char_counts(str_1)

    for char in str_2:
        if char in str_1_char_counts and str_1_char_counts[char] > 0:
            str_1_char_counts[char] -= 1
        else:
            return False

    return True


if __name__ == "__main__":
    assert unscramble('ansucchlohlo', 'launchschool')
    assert unscramble('phyarunstole', 'pythonrules')
    assert not unscramble('phyarunstola', 'pythonrules')
    assert unscramble('boldface', 'coal')
