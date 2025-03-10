"""
Building on the previous exercise, write a function that returns True or False
based on whether or not an inventory item (an ID number) is available. As
before, the function takes two arguments: an item ID and a list of
transactions. The function should return True only if the sum of the quantity
values of the item's transactions is greater than zero. Notice that there is a
movement property in each transaction object. A movement value of 'out' will
decrease the item's quantity.

You may (and should) use the transactions_for function from the previous
exercise.

P
    inputs: int, dictionary
    outputs: boolean
    rules:
        Explicit Reqs:
            - accept an int and a dict
            - return a bool
            - calculate the current inventory based on movements in and out
            - return if the current quantity is greater than 0
        Implicit Reqs:
            - an empty transactions dict should return False
            - a transactions dict without the given item_id shoudl return False
E
    transactions = [
        {"id": 101, "movement": 'in',  "quantity":  5},
        {"id": 105, "movement": 'in',  "quantity": 10},
        {"id": 102, "movement": 'out', "quantity": 17},
        {"id": 101, "movement": 'in',  "quantity": 12},
        {"id": 103, "movement": 'out', "quantity": 20},
        {"id": 102, "movement": 'out', "quantity": 15},
        {"id": 105, "movement": 'in',  "quantity": 25},
        {"id": 101, "movement": 'out', "quantity": 18},
        {"id": 102, "movement": 'in',  "quantity": 22},
        {"id": 103, "movement": 'out', "quantity": 15},
    ]
    is_item_available(101, transactions) == False)
    is_item_available(103, transactions) == False)
    is_item_available(105, transactions) == True)
D
    none
A
    - get all transations from helper func
    - create an inventory counter
    - loop through each transaction
    - adjust the counter as necessary
    - return if the counter is greaer than 0
C
"""
import sys
from inventory_item_transactions import transactions_for


def is_item_available(item_id: int, transactions: dict) -> bool:
    """Returns if the given item is available based on transactions data."""
    all_transactions = transactions_for(item_id, transactions)
    item_inventory = 0

    for t in all_transactions:
        quantity = t["quantity"]
        item_inventory += quantity if t["movement"] == 'in' else -quantity
    return item_inventory > 0


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
On line 55, is_item_available is defined with two parameters, item_id, which
expects an int, and transactions, which expects a list of transaction dicts.

On line 57, the local variable all_transations is assigned to the return value
of calling transations_for with item_id and transactions as args respectively.

item_inventory, a local variable, is assigned to 0 on line 58.

On line 60, a for loop iterates through all_transations.

On line 61, a local variable quantity is instantiated with the value at the
"quantity" key of the current transaction, t.

On line 62, a ternary statement eother adds or subtracts the value of quantity
from item_inventory, based on the value of t at the "movement" key.

Finally, on line 63, item_inventory is checked to see if it is greater than 0
and the boolean result from this expression is returned.


User Level
is_item_available takes an item_id and a list of transations, calculates the
current inventory level of the item based off of the movements associated the
given item_id stored in transactions, and returns if there is any inventory
of the item in stock or not.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        test_transactions = [
            {"id": 101, "movement": 'in',  "quantity":  5},
            {"id": 105, "movement": 'in',  "quantity": 10},
            {"id": 102, "movement": 'out', "quantity": 17},
            {"id": 101, "movement": 'in',  "quantity": 12},
            {"id": 103, "movement": 'out', "quantity": 20},
            {"id": 102, "movement": 'out', "quantity": 15},
            {"id": 105, "movement": 'in',  "quantity": 25},
            {"id": 101, "movement": 'out', "quantity": 18},
            {"id": 102, "movement": 'in',  "quantity": 22},
            {"id": 103, "movement": 'out', "quantity": 15},
        ]
        assert not is_item_available(101, test_transactions)
        assert not is_item_available(103, test_transactions)
        assert is_item_available(105, test_transactions)
