"""PEDAC

Problem:
    Write a program that, given the number of available blocks, calculates the
    number of blocks left over after building the tallest possible valid
    structure.

    Input:
        - Integer value representing the number of available blocks

    Output:
        - Integer value representing the number of leftover blocks after
        building the highest possible tower

    Explicit Rules:
        - The top of the tower must be exactly 1 block
        - Any block in an upper layer must be supported by 4 blocks below it
        - Blocks in lower layers may support more than one block in an upper
        layer
        - No gaps are allowed in between blocks

    Implicit Rules:
        - each layer has exactly the layer number squared blocks in it, 
        counting from the top layer down
        - ex: layer 1 -> 1, layer 2 -> 4, layer 3 -> 9, ...

    Clarifying Questions:
        - Given 0 blocks, should we return 0?
        - Can I assume the input will always be an integer?

Example/Test Cases:
    print(calculate_leftover_blocks(0) == 0)  # True
    print(calculate_leftover_blocks(1) == 0)  # True
    print(calculate_leftover_blocks(2) == 1)  # True
    print(calculate_leftover_blocks(4) == 3)  # True
    print(calculate_leftover_blocks(5) == 0)  # True
    print(calculate_leftover_blocks(6) == 1)  # True
    print(calculate_leftover_blocks(14) == 0) # True

Data Structure:
    Since this is a simple mathematical calculation, no data structure is
    required to solve this problem

Algorithm:
    create a blocks_used variable, start it at 0
    create a curr_layer_req variable, start it at 1
    while compare curr_layer_req + blocks_used <= input_int:
        add curr_layer_req to blocks_used
        increment curr_layer_req by 1 and square the result
    return input_int - blocks_used

Code:
"""


def calculate_leftover_blocks(num_blocks):
    blocks_used = 0
    curr_layer = 1
    curr_layer_req = curr_layer ** 2

    while curr_layer_req + blocks_used <= num_blocks:
        blocks_used += curr_layer_req
        curr_layer += 1
        curr_layer_req = curr_layer ** 2

    return num_blocks - blocks_used


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0)  # True
