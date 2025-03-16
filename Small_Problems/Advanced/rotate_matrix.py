"""
Write a function that takes an arbitrary MxN matrix, rotates it clockwise by
90-degrees as described above, and returns the result as a new matrix. The
function should not mutate the original matrix.

P
    inputs: list of lists (matrix)
    outputs: list of lists (matrix)
    rules:
        Explicit Reqs:
            - accept a list
            - return a list
            - return list should be a matrix
            - return list should be "rotated" by 90 degrees
        Implicit Reqs:
            - empty list should return an empty list
            - empty list of lists should return an empty list of lists
E
    matrix1 = [
        [1, 5, 8],
        [4, 7, 2],
        [3, 9, 6],
    ]
    matrix2 = [
        [3, 7, 4, 2],
        [5, 1, 0, 8],
    ]
    new_matrix1 = rotate90(matrix1)
    new_matrix2 = rotate90(matrix2)
    new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))
    assert new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]]
    assert new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]]
    assert new_matrix3 == matrix2
D
    Zip object, list comprehension
A
    - create a list comprehension
        - loop through a zip object
            - arg should be the reversed matrix unpacked
        - return value should cast the tuple to a list
    - return the list comprehension
C
"""
import sys


def rotate90(matrix: list) -> list:
    """Rotates the given matrix by 90 degrees clockwise."""
    return [list(row) for row in zip(*reversed(matrix))]


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

The rotate90 function is defined on line 47, and has a single parameter,
matrix, which expects a list of lists.

This one-liner is returned on line 49. It is a list comprehension which
iterates through a zip object made from reversing the matrix, specifically
the order of each column, and unpacking those lists, which ar ethen zipped
together as column tuples. Each column tuple is coerced to a list and appended
to the list comprehension.

User Level:
Rotate90 takes a matrix, and rotates it 90 degrees clockwise by leveraging the
zip method, in conjunction with the reversed method, and the unpacking
operator, and coercing each zipped tuple to a list, and appending them to a
return list.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        matrix1 = [
            [1, 5, 8],
            [4, 7, 2],
            [3, 9, 6],
        ]
        matrix2 = [
            [3, 7, 4, 2],
            [5, 1, 0, 8],
        ]
        new_matrix1 = rotate90(matrix1)
        new_matrix2 = rotate90(matrix2)
        new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))
        assert new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]], new_matrix1
        assert new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]]
        assert new_matrix3 == matrix2
