"""
Write a program that solicits six (6) numbers from the user and prints a
message that describes whether the sixth number appears among the first five.
"""
import sys


def generate_test_input(test_input):
    """Generates simulated user input

    :param test_input (list<int>): the ints subbing in for user input
    :yeilds num (int): the current int acting as user input
    """
    if test_input:
        for num in test_input:
            yield num


def get_suffix(num):
    """Gets the correct suffix for the given num

    :param num (int): the number to calculate the correct suffix for
    :returns suffix (str): the correct suffix
    """
    match num:
        case 1:
            suffix = "st"
        case 2:
            suffix = "nd"
        case 3:
            suffix = "rd"
        case 6:
            suffix = "last"
        case _:
            suffix = "th"
    return suffix


def solicit_six(test_input=None):
    """asks the user for 6 integers and checks to see if the last integer
    provided is in the first 5 integers provided.

    :param test_input (list<int>): the test cases subbing in for user input
    :returns (str): correctly formatted string depending on the given input
    """
    test_input_generator = generate_test_input(test_input)
    user_input = []

    for n in range(1, 7):
        suffix = get_suffix(n)
        n = '' if n == 6 else n
        user_input.append(next(test_input_generator) if test_input else
                          input(f"Enter the {n}{suffix} number: "))

    is_or_isnt = "is" if user_input[-1] in user_input[:-1] else "isn't"
    return f"{user_input[-1]} {is_or_isnt} in {user_input[:5]}"


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION
Solicit_six is a function defined on line 39, and is the main driver function
of this program. On line 46, a call to helper generate_test_input is assigned
to the variable test_input_generator. This helper function creates a generator
with the given test_input list, containing 6 integers.

user_input is assigned to an empty list literal on line 47.

the for loop on line 49 loops through a range object starting at 1 and ending
at 7. within the context of this loop, a local variable suffix is instantiated
to the return value of calling the helper function get_suffix.

get_suffix, defined on line 19, accepts a single parameter, num, and has a
match statement to compare num to several cases, and return the appropriate
suffix string.

On line 51, a conditional statement checks to see if n is 6 in the current
iteration of the loop. If so, it changes the value of n to an empty string.

On line 52, the append method is called on the user_input list, in order to
push the value of the next element from the test_input_generator, or to the
value entered by the user.

On line 55, a local variable is_or_isnt is assigned to the value of "is" or
"isn't" depending on whether or not the final value of user_input is found
within the first 5 elements of user_input.

Finally, on line 56, using f-string interpolation, the required output string
is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert solicit_six([1, 2, 3, 4, 5, 2]) == "2 is in [1, 2, 3, 4, 5]"
        assert solicit_six([1, 2, 3, 4, 5, 8]) == "8 isn't in [1, 2, 3, 4, 5]"
    else:
        print(solicit_six())
