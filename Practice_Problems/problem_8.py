"""
Create a function that takes a non-empty string as an argument. The string
consists entirely of lowercase alphabetic characters. The function should
return the length of the longest vowel substring. The vowels of interest are
"a", "e", "i", "o", and "u".

P
    inputs: non-empty string
    outputs: int
    rules:
        Explicit Reqs:
            - accept a string
            - return an int
            - return int is the len of the longest vowel substr
            - input string is entirely lowercase alphabetic chars
            - "a", "e", "e", "o", "u" are vowels of interest
        Implicit Reqs:
            - don't modify the input string
E
    (see below tests)
D

A
    - create a constant `VOWELS`, a set of lowercase vowels
    - create an empty vowels_and_stars string
    - iterate through the input_str
        - if the curr_char is a vowel, append it to `vowels_and_stars`
        - if not, append a `*`
    - split vowels_and_stars on * char to a list
    - return the lengh of the max string in the str and star list
C
"""


def longest_vowel_substring(input_str: str) -> int:
    """
    Returns te length of the longest vowel substring in the given input_str.
    Expects all chars in input_str to be lowercase and alphabetic.
    """
    VOWELS = {"a", "e", "i", "o", "u"}
    vowels_and_stars = "".join(
        char if char in VOWELS else "*" for char in input_str
    )
    return len(max(vowels_and_stars.split("*"), key=len))


if __name__ == "__main__":
    assert longest_vowel_substring('cwm') == 0
    assert longest_vowel_substring('many') == 1
    assert longest_vowel_substring('launchschoolstudents') == 2
    assert longest_vowel_substring('eau') == 3
    assert longest_vowel_substring('beauteous') == 3
    assert longest_vowel_substring('sequoia') == 4
    assert longest_vowel_substring('miaoued') == 5
