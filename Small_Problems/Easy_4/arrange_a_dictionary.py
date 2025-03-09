"""
Given a dictionary, return its keys sorted by the values associated with each
key.

P
    inputs: a dictionary
    outputs: a list of the sorted keys of the input dict
    rules:
        Explicit Reqs:
            - Accept a single dict
            - Return a list of keys, sorted by their value in the input dict
            - Will all the dict keys and values be of the same type?
        Implicit Reqs:
            - an empty dict returns an empty list
E
    my_dict = {'p': 8, 'q': 2, 'r': 6}
    keys = ['q', 'r', 'p']
    order_by_value(my_dict) == keys
D
    list
A
    - get the keys of the dict
    - sort the keys by their associated value
    - return a list of the keys in sorted order
C
"""
import sys


def order_by_value(input_dict: dict) -> list:
    """Returns the keys of the input dict sorted by their respective values"""
    return sorted(list(input_dict.keys()), key=lambda x: input_dict[x])


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
On line 30, the order_by_value function is defined with a single parameter
input_dict, which expects a dictionary.

The one liner on line 32 gets the keys of input_dict with .keys() and coerces
it to a list. It then uses the sorted function to sort the list with a custom
lambda function. The lambda uses the current key to look up its corresponding
value in input_dict for the sort.

Finally, the sorted list is returned.

User Level
Order_by_value returns the keys from a dictionary, sorted by their
corresponding values in the dictionary.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        my_dict = {'p': 8, 'q': 2, 'r': 6}
        keys = ['q', 'r', 'p']
        assert order_by_value(my_dict) == keys
