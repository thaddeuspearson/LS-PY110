"""
Modify the function from the previous exercise so it ignores non-alphabetic
characters when determining whether it should uppercase or lowercase each
letter. The non-alphabetic characters should still be included in the return
value; they just don't count when toggling the desired case.

P
    inputs: string
    outputs: string
    rules:
        Explicit Reqs:
            - accept a string
            - return a string
            - return string should alternate cases and ignore non alpha chars
            - non-alpha chars do not count as case change placeholders
        Implicit Reqs:
            - an empty string returns an empty string
        Questions:
            - account for interational chars?
E
    string = 'I Love Launch School!'
    result = "I lOvE lAuNcH sChOoL!"
    staggered_case(string) == result

    string = 'ALL_CAPS'
    result = "AlL_cApS"
    staggered_case(string) == result

    string = 'ignore 77 the 4444 numbers'
    result = "IgNoRe 77 ThE 4444 nUmBeRs"
    staggered_case(string) == result

    staggered_case('') == ""
D
    str
A
    - create a bool called upper
    - create a return_str
    - iterate through the input_str
        - check to see if the curr char is alpha
            - if so, check to see if upper is true
                - if so append char upper to return str
                - if not, char lower to string
                - flip upper
            - if not append curr c to return_str
    - return return_str
C
"""
import sys


def staggered_case(string: str) -> str:
    """Returns a string with alternating case (ignores non-alpha chars)"""
    upper = True
    return_str = ""

    for c in string:
        if c.isalpha():
            return_str += c.upper() if upper else c.lower()
            upper = not upper
        else:
            return_str += c
    return return_str


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
On line 52, the staggered_case function is defined with a sigle parameter,
string, which expects a str.

On line 54, a local variable called upper is instantiated to True.
On Line 55, a local variable called return_str is icreates as an empty str.

On line 57, a for loop iterates through string one c at a time. On line 58,
c is checked to see if it is an alphabetic char with .isalpha(). If it is
then return_str is concatenated with c based on the result of the ternary
statement checking to see if upper is furrently set to True or not. The
corresponding string method is called based on the result of this boolean
check. Finally upper is flipped with the not operator on line 60.

In the case that c is not an alphabetic char, then current value of c is
concatenated to return_str.

Finally, return str is returned on line 63.


User Level
staggered case takes an inout string, alternates upper and lower case for each
alphabetic character, skipping non-alphabetic characters when continuing the
pattern, and returns the newly transformed string.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        # pylint: disable=invalid-name
        test_string = 'I Love Launch School!'
        result = "I lOvE lAuNcH sChOoL!"
        assert staggered_case(test_string) == result

        test_string = 'ALL_CAPS'
        result = "AlL_cApS"
        assert staggered_case(test_string) == result

        test_string = 'ignore 77 the 4444 numbers'
        result = "IgNoRe 77 ThE 4444 nUmBeRs"
        assert staggered_case(test_string) == result

        assert staggered_case('') == ""
