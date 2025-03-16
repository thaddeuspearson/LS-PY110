"""
Write a function that takes a list of lists that represents a 3x3 matrix an
returns the transpose of the matrix. You should implement the function on
your own, without using any external libraries.

Take care not to modify the original matrix -- your function must produce a
new matrix and leave the input matrix list unchanged.

P
    inputs: list of lists
    outputs: list of list
    rules:
        Explicit Reqs:
            - accept a list
            - return a list
            - return list should be the transposition of the input list
            - Do not modify the original list
        Implicit Reqs:
            - an empty list should return an empty list
            - an empty list of empty lists should return an empty list of lists
E
    matrix = [
        [1, 5, 8],
        [4, 7, 2],
        [3, 9, 6],
    ]
    new_matrix = transpose(matrix)
    new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]
    matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]]
D
    a zip object
A
    - create a return list
    - iterate through a range object the size of one side of the given matrix
        - create a new empty list
        - iterate through the nested lists
            - push the index of the curr num to the empty list
        - push the new list to the return list
    - return return list
C
"""
import sys


def transpose(matrix: list) -> list:
    """Transposes a 3 x 3 matrix and returns it."""
    return [list(col) for col in zip(*matrix)]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

The transpose function is defined on line 45, and has 1 parameter, matrix,
which expects a list of lists with the same len.

This one liner uses a list comprehension, zip, and list unpacking. The
comprehension loops through a zip object that is provided the matrix as an
argument, and each row of the matrix is unpacked, so zip has each individual
row passed to it.

Zip then created tuples for each of the columns in each row, and groups them
together. In the outer comprehension loop, each tuple is coerced to a list and
the resulting transposed list is returned.

User Level:

Transpose takes a matrix, zips each row together as columns, transforms each
column tuple to a list, and returns the transposed matrix.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        test_3_by_3_matrix = [
            [1, 5, 8],
            [4, 7, 2],
            [3, 9, 6],
        ]
        new_3_by_3_matrix = [
            [1, 4, 3], 
            [5, 7, 9], 
            [8, 2, 6]
        ]
        assert transpose(test_3_by_3_matrix) == new_3_by_3_matrix
        assert test_3_by_3_matrix == test_3_by_3_matrix

        test_3_by_5_matrix = [
            [1, 2, 3, 4, 5],
            [4, 3, 2, 1, 0],
            [3, 7, 8, 6, 2],
        ]
        new_3_by_5_matrix = [
            [1, 4, 3],
            [2, 3, 7],
            [3, 2, 8],
            [4, 1, 6],
            [5, 0, 2],
        ]
        assert transpose(test_3_by_5_matrix) == new_3_by_5_matrix
        assert test_3_by_5_matrix == test_3_by_5_matrix

        assert transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]]
        assert transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]]
        assert transpose([[1]]) == [[1]]
        
        
        
