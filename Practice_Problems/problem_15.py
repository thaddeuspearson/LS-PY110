"""
Create a function that takes a string argument that consists entirely of
numeric digits and computes the greatest product of four consecutive digits
in the string. The argument will always have more than 4 digits.

P
    inputs: str
    outputs: int
    rules:
        Explicit Reqs:
            - accept a str
            - return an int
            - return int is the greatest product of 4 consecutive digits
            - the arguments given will always have more than 4 digits
E
    (see test cases below)
D
    None
A
    - create `greatest_product` and initialize to i * i+1 * i+2
    - coerce the `input_str` to `chars_list`
    - iterate through the `chars_list` (`curr_idx`)
        - multiply curr_product by curr_idx
        curr_product = * i+3
        - if curr_product > greatest_product
            - replace
        - curr_product divided by curr_idx - 3
C
"""


def greatest_product(input_str: str) -> int:
    """
    Returns the greatest product of 4 consecutive digits in the input_str
    """
    input_nums = [int(digit) for digit in input_str]
    curr = input_nums[0] * input_nums[1] * input_nums[2] * input_nums[3]
    greatest = curr

    for i in range(4, len(input_nums)):
        curr = curr // input_nums[i-4] * input_nums[i]
        greatest = max(greatest, curr)

    return greatest


if __name__ == "__main__":
    assert greatest_product('23456') == 360
    assert greatest_product('3145926') == 540
    assert greatest_product('1828172') == 128
    assert greatest_product('123987654') == 3024
