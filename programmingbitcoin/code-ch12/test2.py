############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run, hash256, h160
import bloomfilter
import block
import ecc
import helper
import merkleblock
import network
import script
import tx

bit_field_size = 10
bit_field = [0] * bit_field_size
for item in (b'hello world', b'goodbye'):
    h = hash160hash16
    bit = int.from_bytes(h, 'big')

bit = int.from_bytes(h, 'big') % bit_field_size
bit_field[bit] = 1
print(bit_field)
