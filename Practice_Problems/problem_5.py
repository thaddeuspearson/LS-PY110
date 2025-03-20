"""
Create a function that takes a string argument and returns the character that
occurs most often in the string. If there are multiple characters with the
same greatest frequency, return the one that appears first in the string. When
counting characters, consider uppercase and lowercase versions to be the same.

P
    inputs: str
    outputs: str
    rules:
        Explicit Reqs:
            - accept a str
            - return a single char str
            - the return char should be the char that occurs most
            - char counts are case insensitive
            - tie: the char which appears first in the string is returned
        Implicit Reqs:
            - empty string returns an empty string
            - all return values should be in lowercase
            - dont modify the input str
        Questions:
            - count spaces?
            - count newlines, tabs etc?
E
    (see test cases below)
D
    dict
A
    - create a dict: `char_countss`
    - iterate through the input string without spaces
        - coerce `curr_char` to lowercase
        - set/increment the counter at the `curr_char` key in `char_countss`
    - retrieve the greatest counter in the dict
    - create a `max_char_earliest_idx` variable set to length of the input str
    - iterate through all chars with the greatest count
        - get each index of each char
    return the input_str[max_char_earliest_idx] in lowercase
C
"""


def most_common_char(input_str: str) -> str:
    """
    Returns the most commonly occuring character (case insensitive). In the
    case of a tie, the character that has the first occurance in the string is
    returned.
    """
    input_str = input_str.lower()
    char_counts = {}

    for char in input_str:
        if char.isalnum():
            char_counts[char] = char_counts.get(char, 0) + 1

    most_common = max(
        char_counts, key=lambda k: (char_counts[k])
    )

    return most_common


if __name__ == "__main__":
    assert most_common_char('Hello World') == 'l'
    assert most_common_char('Mississippi') == 'i'
    assert most_common_char('Happy birthday!') == 'h'
    assert most_common_char('aaaaaAAAA') == 'a'

    my_str = 'Peter Piper picked a peck of pickled peppers.'
    assert most_common_char(my_str) == 'p'

    my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
    assert most_common_char(my_str) == 'e'
