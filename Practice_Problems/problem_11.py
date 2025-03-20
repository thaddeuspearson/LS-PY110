"""
Create a function that takes a nonempty string as an argument and returns a
tuple consisting of a string and an integer. If we call the string argument s,
the string component of the returned tuple t, and the integer component of the
tuple k, then s, t, and k must be related to each other such that s == t * k.
The values of t and k should be the shortest possible substring and the
largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase
alphabetic letters.

P
    inputs: str
    outputs: tuple
    rules:
        Explicit Reqs:
            - accept a str
            - return a tuple
            - input_str is non-empty, and entirely lowercase letters
        Implicit Reqs:
            - if there are no repetitions of substrs, return 1
        Questions:
            - are all input_strs composed entirely of a min len repeated
              substrs?
E
    (see test cases below)
D
    dict, list
A
    - get all substrs
        - make a return list (substrs)
        - iterate through input_str (i)
            - iterate through the remainder of input_str (j)
                - create each substr
                - append to substrs
        return substrs

    - component_substrs = {}
    - create a `substr_count` = 0
    - repeatedly concatenate the substrs to themselves, until
      the concatenation is >= length of the input str
        - increment `substr_count`
        - if ==:
            update component_substrs with substr : substr_count

    - return the max (substr, substr_count)
C
"""


def get_substrs(input_str: str) -> list:
    """
    Returns all substrings of the given input_str
    """
    substrs = []
    input_str_len = len(input_str)

    for i in range(input_str_len):
        for j in range(i+1, input_str_len+1):
            substrs.append(input_str[i:j])

    return substrs


def repeated_substring(input_str: str) -> int:
    """
    Returns a tuple consisting of the smallest substring that can be
    duplicated to create the given input_str, and its count, in the form:
    (substr, count)
    """
    component_substrs = {}
    unique_substrs = set(get_substrs(input_str))
    input_str_len = len(input_str)

    for substr in unique_substrs:
        assembled = ""
        substr_count = 0

        while len(assembled) < input_str_len:
            assembled += substr
            substr_count += 1

        if assembled == input_str:
            component_substrs[substr] = substr_count

    return max(component_substrs.items(), key=lambda t: t[1])


if __name__ == "__main__":
    assert repeated_substring('xyzxyzxyz') == ('xyz', 3)
    assert repeated_substring('xyxy') == ('xy', 2)
    assert repeated_substring('xyz') == ('xyz', 1)
    assert repeated_substring('aaaaaaaa') == ('a', 8)
    assert repeated_substring('superduper') == ('superduper', 1)
