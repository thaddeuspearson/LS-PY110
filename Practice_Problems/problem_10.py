"""
Create a function that takes a string of digits as an argument and returns the
number of even-numbered substrings that can be formed. For example, in the
case of '1432', the even-numbered substrings are '14', '1432', '4', '432',
'32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a
separate substring.

P
    inputs: string
    outputs: int
    rules:
        Explicit Reqs:
            - accept a string
            - return an int
            - return int is the count ov substs that are even when coerced to
              an int
        Implicit Reqs:
            - empty input_str returns 0
E
    (see test cases below)
D
    list
A
    - get all substrs from input_str
        - iterate through the input str (i)
            - interate through the remaining chars in input str (j)
                - get the slice using the two indexes input_str[i:j+1]
        - return alll substrs as a list

    - filter the substr list for even substrs only
    - return the length of filtered list
C
"""


def get_substrs(input_str: str) -> list:
    """
    Returns all substrings from the given input_str
    """
    substrs = []

    for i in range(len(input_str)):
        for j in range(i, len(input_str)):
            substrs.append(input_str[i:j+1])

    return substrs


def even_substrings(input_str: str) -> int:
    """
    Return all substrings that coerce to an even number.
    """
    substrs = get_substrs(input_str)
    return len([s for s in substrs if int(s) % 2 == 0])


if __name__ == "__main__":
    # get_substrs('1432')
    assert even_substrings('1432') == 6
    assert even_substrings('3145926') == 16
    assert even_substrings('2718281') == 16
    assert even_substrings('13579') == 0
    assert even_substrings('143232') == 12
