"""
Create a function that takes a string argument and returns a dict object in
which the keys represent the lowercase letters in the string, and the values
represent how often the corresponding letter occurs in the string.
P
    - input: str
    - output: dict
    - rules:
        Explicit Reqs:
            - accept a str
            - return a dict
            - return dict has keys that atre lowercase letters, and values
              that are their count
            - ignore chars that are uppercase or have no case
        Implicit Reqs:
            - empty string returns an empty dictionary
E
    (see  test cases below)
D
    - dict
A
    - create a return dict, `lowercase_char_counts`
    - iterate through the `input_str`
        - filter for
            - characterss that are alphabetic
            - lowercase
        - add/increment the char / count
    return `lowercase_char_counts`
C
"""


def count_letters(input_str: str) -> dict:
    """
    Returns a dictionary of all the lowercase char counts in the given
    input_str. Ignores all other chars.
    """
    lowercase_char_counts = {}

    for c in input_str:
        if c.isalpha() and c.islower():
            lowercase_char_counts[c] = lowercase_char_counts.get(c, 0) + 1

    return lowercase_char_counts


if __name__ == "__main__":
    expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
    assert count_letters('woebegone') == expected

    expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
                'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
    assert count_letters('lowercase/uppercase') == expected

    expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
    assert count_letters('W. E. B. Du Bois') == expected

    assert count_letters('x') == {'x': 1}
    assert count_letters('') == {}
    assert count_letters('!!!') == {}
