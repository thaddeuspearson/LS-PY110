"""
Write a function that takes a string as an argument and returns that string
with a staggered capitalization scheme. Every other character, starting from
the first, should be capitalized and should be followed by a lowercase or
non-alphabetic character. Non-alphabetic characters should not be changed, but
should be counted as characters for determining when to switch between upper
and lower case.

P
    inputs: str
    outputs: str
    rules:
        Explicit Reqs:
            - accept a string
            - return a string
            - leave all non-alphabetic chars as they are
            - alternate case for each alphabetic char
        Implicit Reqs:
            - empty string should return an empty string
        Questions:
            - do we need to account for international characters?
E
    string = 'I Love Launch School!'
    result = "I LoVe lAuNcH ScHoOl!"
    assert staggered_case(string) == result

    string = 'ALL_CAPS'
    result = "AlL_CaPs"
    assert staggered_case(string) == result

    string = 'ignore 77 the 4444 numbers'
    result = "IgNoRe 77 ThE 4444 nUmBeRs"
    assert staggered_case(string) == result

    assert staggered_case('') == ""
D
    str
A
    - enumerate the string
    - check each char index for parity
    - upper or lower case each char accordingly
    - append to a generator comprehension
    - use join to stich the string back together
    - return the transformed string
C
"""
import sys


def staggered_case(string: str) -> str:
    """Returns a string with alternating case (ignores non-alpha chars)"""
    return ''.join(
        c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(string)
    )


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
The staggered_case function is defined on line 43, with a single parameter,
string, which expects a str.

On line 45 the join method is called on an empty string literal with a
generator comprehension as its agrument. the comprehension iterates through
the enumeration of string, and uses a conditional if/else ternary to either
uppercase or lowercase the current character if the index is even or odd
respectively.

The final joined string is returned.

User Level
Staggered_case takes a string and returns a new string with each character
upper or lowercased ina staggered pattern.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        # pylint: disable=invalid-name
        test_string = 'I Love Launch School!'
        result = "I LoVe lAuNcH ScHoOl!"
        assert staggered_case(test_string) == result

        test_string = 'ALL_CAPS'
        result = "AlL_CaPs"
        assert staggered_case(test_string) == result

        test_string = 'ignore 77 the 4444 numbers'
        result = "IgNoRe 77 ThE 4444 nUmBeRs"
        assert staggered_case(test_string) == result

        assert staggered_case('') == ""
