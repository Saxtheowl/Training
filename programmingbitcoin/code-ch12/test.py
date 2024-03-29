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

# field_size = 10
# num_function = 5
# tweak = 99
# bit_field_size = field_size * 8
# bit_field = [0] * bit_field_size
# items = (b'Hello World',  b'Goodbye!')
# for item in items:
#     for i in range(num_function):
#         seed = i * BIP37_CONSTANT + tweak
#         h = murmur3(item, seed=seed)
#         bit = h % bit_field_size
#         bit_field[bit] = 1
# print(bit_field_to_bytes(bit_field).hex())

# for i in range(5):
#     print(i)


>>> from bloomfilter import BloomFilter
>>> from helper import decode_base58
>>> from merkleblock import MerkleBlock
>>> from network import FILTERED_BLOCK_DATA_TYPE, GetHeadersMessage, GetDataMe\
ssage, HeadersMessage, SimpleNode
>>> from tx import Tx
>>> last_block_hex = '00000000000538d5c2246336644f9a4956551afb44ba47278759ec55\
ea912e19'
>>> address = 'mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv'
>>> h160 = decode_base58(address)
>>> node = SimpleNode('testnet.programmingbitcoin.com', testnet=True, logging=\
False)
>>> bf = BloomFilter(size=30, function_count=5, tweak=90210)
>>> bf.add(h160)
>>> node.handshake()
>>> node.send(bf.filterload())
>>> start_block = bytes.fromhex(last_block_hex)
>>> getheaders = GetHeadersMessage(start_block=start_block)
>>> node.send(getheaders)
>>> headers = node.wait_for(HeadersMessage)
>>> getdata = GetDataMessage()
>>> for b in headers.blocks:
...
if not b.check_pow():
...
raise RuntimeError('proof of work is invalid')
...
getdata.add_data(FILTERED_BLOCK_DATA_TYPE, b.hash())
>>> node.send(getdata)
