"""
Write a function that counts the number of occurrences of each element in a
given list. Once counted, print each element alongside the number of
occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").
"""
import sys


def count_occurances(items: list) -> str:
    """Outputs a formatted string displaying the items in the list and their
    respective counts.

    :param items (list): the items list to count and print
    :returns output_str (str): the formatted output string
    """
    item_counters = {}

    for item in items:
        item_counters[item] = item_counters.get(item, 0) + 1

    output_str = ""

    for item, item_count in item_counters.items():
        output_str += f"{item} => {item_count}\n"

    return output_str


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
count_occurances is defined on line 9 and has a single parameter, items which
is a list.

On line 16, a local variable item_counters is instantiated to an empty
dictionary literal.

On line 18, a for loop iterates through the items local variable. In each
iteration, the get method is called on item_counters with the item key, either
the current count, or a new counter initialized to 0 is incremented by 1 and
saved at the item key.

On line 23, another for loop iterates through a dict_items object created from
the item_counters dictionary. each item and item_counter is unpacked, and
concatenated to the output_string with an arrow in between them.

Finally, on line 26, the output string is returned.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        # pylint: disable=invalid-name
        vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
                    'motorcycle', 'motorcycle', 'car', 'truck']
        test_1 = count_occurances(vehicles)
        assert test_1 == "car => 4\ntruck => 3\nSUV => 1\nmotorcycle => 2\n"
