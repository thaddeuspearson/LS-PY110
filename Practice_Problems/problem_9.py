"""
Create a function that takes two string arguments and returns the number of
times that the second string occurs in the first string. Note that overlapping
strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

P
    inputs: str
    outputs: int
    rules:
        Explicit Reqs:
            - accept a string
            - return an int
            - return int = number of times substr appears in input_str
            - overlapping substrs only count once

        Implicit Reqs:
            - return 0 if the input_str is empty

        Questions:
            - how to handle case? (case-sensitive)
            - how to handle non alphanum chars?
E
    (see test cases below)
D
    counter
A
    - create `substr_count`, initialize to 0
    - create `curr_idx`, initialize to 0
    - create `substr_len`, intialize to the length of substr
    - create `input_str_len`, initialize to length of substr
    - loop until `curr_idx` > `input_str_len` - `substr_len`
        - find the next occurance of the `substr`, starting at `curr_idx`
        - if it is found
            - increment `substr_count` by 1
            - increment `curr_idx` by length of substr
        - if it is not found
            - break
    - return `substr_count`
C
"""


def count_substrings(input_str: str, substr: str) -> int:
    """
    Returns the count of non-overlapping substrs in the given input_str
    """
    substr_count, curr_idx = 0, 0
    substr_len = len(substr)
    last_possible_substr_idx = len(input_str) - substr_len

    while curr_idx < last_possible_substr_idx:
        curr_idx = input_str.find(substr, curr_idx)

        if curr_idx == -1:
            break
        substr_count += 1
        curr_idx += substr_len
    return substr_count


if __name__ == "__main__":
    assert count_substrings('babab', 'bab') == 1
    assert count_substrings('babab', 'ba') == 2
    assert count_substrings('babab', 'b') == 3
    assert count_substrings('babab', 'x') == 0
    assert count_substrings('babab', 'x') == 0
    assert count_substrings('', 'x') == 0
    assert count_substrings('bbbaabbbbaab', 'baab') == 2
    assert count_substrings('bbbaabbbbaab', 'bbaab') == 2
    assert count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1
