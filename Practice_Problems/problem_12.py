"""
Create a function that takes a string as an argument and returns True if the
string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least
once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a
pangram since it uses every letter at least once. Note that case is irrelevant

P
    inputs: str
    outputs: bool
    rules:
        Explicit Reqs:
            - accept a str
            - return a bool
            - return bool indicates if a word is a pangram
            - a pangram is a string that contains each letter of the alphabet
              at least once
            - case insensitive
        Implicit Reqs:
            - empty input_str returns False
E
    (see test cases below)
D
    set
A
    - create a `LETTERS` set for lookup
    - get only alphabetic chars in lowercase from `input_str`
      (`only_lower_letters`)
    - coerce `only_lower_letters` to a set
    - return `only_lower_letters` == `LETTERS`
C
"""


def is_pangram(input_str: str) -> bool:
    """
    Returns if the given string is a pangram.
    """
    LOWERCASE_LETTERS = {chr(char) for char in range(ord("a"), ord("z")+1)}

    only_lower_letters = "".join(
        char.lower() for char in input_str if char.isalpha()
    )
    return set(only_lower_letters) == LOWERCASE_LETTERS


if __name__ == "__main__":
    assert is_pangram('The quick, brown fox jumps over the lazy dog!')
    assert not is_pangram('The slow, brown fox jumps over the lazy dog!')
    assert is_pangram("A wizard’s job is to vex chumps quickly in fog.")
    assert not is_pangram("A wizard’s task is to vex chumps quickly in fog.")
    assert is_pangram("A wizard’s job is to vex chumps quickly in golf.")

    my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
    assert is_pangram(my_str)
