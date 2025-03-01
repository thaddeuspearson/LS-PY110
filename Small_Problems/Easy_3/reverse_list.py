"""
Write a function that takes a list as an argument and reverses its elements,
in place. That is, mutate the list passed into the function. The returned
object should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).
"""
import sys


def swap_in_place(x: int | str, y: int | str) -> tuple:
    """Uses XOR operations to swap x and y

    :param x (int/str): the first elem to swap
    :param y (int/str): the second elem to swap
    :returns x, y: the swapped elems"""
    x_is_int = isinstance(x, int)
    y_is_int = isinstance(y, int)
    x = ord(str(x))
    y = ord(str(y))
    x ^= y
    y ^= x
    x ^= y
    x = chr(x)
    y = chr(y)
    x = int(x) if y_is_int else x
    y = int(y) if x_is_int else y
    return x, y


def reverse_list(target: list) -> list:
    """Reverses a list in place without using built-in python methods.

    :param target (list): the list to reverse in place
    :returns target(list): the reversed target list
    """
    front = 0
    back = len(target) - 1

    while front < back:
        target[front], target[back] = swap_in_place(target[front],
                                                    target[back])
        front += 1
        back -= 1
    return target


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
reverse_list is defined on line 37, and is the main driver function. It has 1
parameter, target, which is the list to be swapped.

On lines 43 and 44, 2 pointer local variables (front and back) are created.
These hold the index values of the front and the back of target respectfully.

The while loop on 46 uses a boolean expression to ensure that front never gets
incremented past back. With each iteration, the current elements at the front
and back index are swapped in place with the swap_in_place helper function.

swap_in_place is defined on line 11, and has 2 parameters, x and y. These
parameters can accept ints or strings. Lines 17 and 18 check to see if the
arguments passed to x or y are integers, and set the local variables x_is_int,
y_is_int to boolean True/False values accordingly. Lines 19 and 20 change the
values of x and y to the ord() values of their string representations.

Lines 21 through 23 use XOR to perform the swap truly in place.

Lines 24 and 25 coerce x and y back their chr values. Lines 26 and 27 coerce x
and/or y to ints based on the truthiness of x_is_int / y_is_int.
Finally the tuple containing x, y are returned on line 28.

Moving back into the execution context of reverse_list, front and back are
incremented and decremented accordingly on lines 49 and 50, within the context
of the while loop.

Finally, the reversed target list is returned on line 52.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        list1 = [1, 2, 3, 4]
        result = reverse_list(list1)
        assert result == [4, 3, 2, 1], result
        assert list1 is result, result

        list2 = ["a", "b", "c", "d", "e"]
        result2 = reverse_list(list2)
        assert result2 == ['e', 'd', 'c', 'b', 'a'], result2
        assert list2 is result2, result2

        list3 = ["abc"]
        result3 = reverse_list(list3)
        assert result3 == ['abc'], result3
        assert list3 is result3, result3

        list4 = []
        result4 = reverse_list(list4)
        assert result4 == [], result4
        assert list4 is result4, result4
