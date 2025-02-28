"""
Write a function that takes a string as an argument and returns True if all
parentheses in the string are properly balanced, False otherwise. To be
properly balanced, parentheses must occur in matching '(' and ')' pairs.
"""
import sys


DELIMITER_PAIRS = {'"': '"', "'": "'", '[': ']', '(': ')', '{': '}'}
DELIMITERS = set(DELIMITER_PAIRS.keys() | DELIMITER_PAIRS.values())


def is_balanced(input_str: str) -> bool:
    """Returns True / False if all delimiters are appropriately matched in the
    given string.

    :param input_str (str): the string to check
    :returns (bool): True / False
    """
    stack = []

    for c in input_str:
        if c in DELIMITERS:
            if stack and c == DELIMITER_PAIRS.get(stack[-1], None):
                stack.pop()
            else:
                stack.append(c)
    return not stack


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
is_balanced is defined on line 13, and has 1 parameter, input_str.

On line 20, we define a local variable stack, which is a FIFO data structure.

On Line 22, we look through input_str, and in each iteration, we check to see
if the current character is in the DELIMITERS set defined in the global scope.
If it is, we check \to see if the stack has delimiters currently in it,and if
the current character equals the last character in the stack. If it does, the
last character in the stack is popped, if not, the current character is pushed
on to the stack.

On line 28, if the stack is empty, the boolean value True is returned. False
if otherwise.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert is_balanced("Hey!")
        assert is_balanced("What (is) this?")
        assert is_balanced("((What) (is this))?")
        assert is_balanced("{}")
        assert is_balanced("[]")
        assert is_balanced("()")
        assert is_balanced("{[({})]}")
        assert is_balanced("\"{[('')]}\"")
        assert is_balanced("Hello [Python] (asdf).")
        assert is_balanced("{[()stacks]} are {kool[()]}")
        assert not is_balanced("What ((is))) up(")
        assert not is_balanced(")Hey!(")
        assert not is_balanced("What is) this?")
        assert not is_balanced("What (is this?")
        assert not is_balanced("((What)) (is this))?")
        assert not is_balanced("{[}]")
        assert not is_balanced("({[})")
        assert not is_balanced("][")
        assert not is_balanced("'''")
        assert not is_balanced("'\"'\"'")
