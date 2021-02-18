############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run, hash256, hash160, murmur3, bit_field_to_bytes
from bloomfilter import BIP37_CONSTANT
import block
import ecc
import helper
import merkleblock
import network
import script
import tx
import bloomfilter

# bit_field_size = 999
# bit_field = [0] * bit_field_size
# for item in (b'hello world', b'goodbye'):
#     h = hash160(item)
#     bit = int.from_bytes(h, 'big') % bit_field_size
#     bit_field[bit] = 1
# print(bit_field)

field_size = 10
num_function = 5
tweak = 99
bit_field_size = field_size * 8
bit_field = [0] * bit_field_size
items = (b'Hello World',  b'Goodbye!')
for item in items:
    for i in range(num_function):
        seed = i * BIP37_CONSTANT + tweak
        h = murmur3(item, seed=seed)
        bit = h % bit_field_size
        bit_field[bit] = 1
print(bit_field_to_bytes(bit_field).hex())
