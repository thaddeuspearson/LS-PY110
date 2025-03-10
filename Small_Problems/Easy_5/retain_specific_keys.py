"""
Given a dictionary and a list of keys, produce a new dictionary that only
contains the key/value pairs for the specified keys.

P
    inputs:
    outputs:
    rules:
        Explicit Reqs:
            -
        Implicit Reqs:
            -
        Questions:
            -
E
    input_dict = {
        'red': 1,
        'green': 2,
        'blue': 3,
        'yellow': 4
    }
    keys = ['red', 'blue']
    expected_dict = {'red': 1, 'blue': 3}
    keep_keys(input_dict, keys) == expected_dict
D
    dict
A
    - iterate through the items of dct
    - filter for keys that are in the keys list
    - return the dictionary
C
"""
import sys


def keep_keys(dct: dict, keys: list) -> dict:
    """Filters the given dictionary based on keeping the given keys"""
    return {k: v for k, v in dct.items() if k in keys}


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
The keep_keys function is defined on line 36. It has two parameters, dct, and
keys, which expect a dictionary and a list respectfully.

The one liner on line 38 creates a diftionary comprehension by iterating
through the dict_items view object, filetering for the condition of k being in
keys, and then adding local variables k and v to the dictionary as
corresponding key: value pairs.

The resulting dictionary is returned.


User Level
Keep_keys filters a dictionary with a list of keys that should remain, and
returns a new dictionary with only the filtered keys.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        input_dict = {
            'red': 1,
            'green': 2,
            'blue': 3,
            'yellow': 4
        }
        test_keys = ['red', 'blue']
        expected_dict = {'red': 1, 'blue': 3}
        assert keep_keys(input_dict, test_keys) == expected_dict
