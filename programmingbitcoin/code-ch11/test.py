############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
import block
import ecc
import helper
import network
import script
import tx
import merkleblock
import math

total = 27

max_depth = math.ceil(math.log(total, 2))
merkle_tree = []
for depth in range(max_depth + 1):
    num_items = math.ceil(total / 2**(max_depth - depth))
    level_hashes = [None] * num_items
    merkle_tree.append(level_hashes)
for level in merkle_tree:
    print(level)
