"""
Write a function that takes two arguments, an inventory item ID and a list of
transactions, and returns a list containing only the transactions for the
specified inventory item.

 P
    inputs: list of dicts
    outputs: list of dicts
    rules:
        Explicit Reqs:
            - accept a list of dicts representing transactions
            - return a list of dicts representing transactions
            - each transaction is formatted the same
        Implicit Reqs:
            - an empty list should return an empty list
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
    transactions_for(101, transactions) == [
            {"id": 101, "movement": "in",  "quantity":  5},
            {"id": 101, "movement": "in",  "quantity": 12},
            {"id": 101, "movement": "out", "quantity": 18},
    ]
 D
    list
 A
    - create a list comprehension
    - iterate through the transactions
        - if the current transationsi has the indicated id number, add it
    - return the comprehension
 C
"""
import sys


def transactions_for(item_id: int, transactions: dict) -> list:
    """Returns all transactions for item_id"""
    return [t for t in transactions if t["id"] == item_id]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level
On line 46, the transactions_for function is defined with 2 parameters,
item_id, which expects an int value, and transactions, expecting a list of
transactions.

On Line 48, a list comprehension is created from looping through the keys of
transactions, checking if the value of the transaction at the key "id" is
equal to item_id, and if so, appending that transaction to the comprehension.

The final comprehension is returned.


User Level
Transactions_for checks a list of transations for any transaction made by
item_id, and returns them in a list.
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

        assert transactions_for(101, test_transactions) == [
            {"id": 101, "movement": "in",  "quantity":  5},
            {"id": 101, "movement": "in",  "quantity": 12},
            {"id": 101, "movement": "out", "quantity": 18},
        ]
