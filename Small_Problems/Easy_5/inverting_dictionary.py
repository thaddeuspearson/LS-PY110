"""
Given a dictionary where both keys and values are unique, invert this
dictionary so that its keys become values and its values become keys.

P
    inputs: dict
    outputs: dict
    rules:
        Explicit Reqs:
            - accept a dictionary
            - return a dictionary with the keys  and values reversed
        Implicit Reqs:
            - an empty dictionary returns an empty dictionary
        Questions:
            - What to do if the value is an un-hashable type?
            - Return a new dictionary or mutate the input?
E
    invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })
D
    dict
A
    - get the input dict items tuple pairs
    - use a dict comprehension
        - reverse the keys and values
    - return the comprehension
C
"""
import sys


def invert_dict(dct: dict) -> dict:
    """Inverts the given dictionary"""
    return {v: k for k, v in dct.items()}


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
On line 37, the invert_dict function is defined with one parmeter, dct,
which expects a dictionary.

The one liner line 39 creates a dictionary comprehension that is created by
iterating through a dict_items view object on dct and reversing the keys and
values as a tuple.

The resulting dictionary is returned.


User Level
Invert_dict gets the items of a dictionary, reverses the keys and values, and
returns a new dictionary made from the reversed keys and values.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        dict1 = {
            'apple': 'fruit',
            'broccoli': 'vegetable',
            'salmon': 'fish',
        }
        dict2 = {
            'fruit': 'apple',
            'vegetable': 'broccoli',
            'fish': 'salmon',
        }
        assert invert_dict(dict1) == dict2
