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


from bloomfilter import BloomFilter
from helper import decode_base58
from merkleblock import MerkleBlock
from network import FILTERED_BLOCK_DATA_TYPE, GetHeadersMessage, GetDataMessage, HeadersMessage, SimpleNode
from tx import Tx

# book showcase

#last_block_hex = '00000000000538d5c2246336644f9a4956551afb44ba47278759ec55ea912e19'
#address = 'mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv'

# our test

#last_block_hex = '0000000017e6fbd8931bce659d45d92040a4674950f2ae5416d0bf1a239641f9'
last_block_hex = '00000000970369111c044804ec0319792c9e1aa29f59a622c5d14b3544ae4eba'
#0000000017e6fbd8931bce659d45d92040a4674950f2ae5416d0bf1a239641f9
#last_block_hex = '0000000000000004fea90996fdf40772e2c2c76205a1fb57fae465194fdaffb9'
address = 'mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1'


h160 = decode_base58(address)
node = SimpleNode('testnet.programmingbitcoin.com', testnet=True, logging=False)
bf = BloomFilter(size=30, function_count=5, tweak=90210)
bf.add(h160)
node.handshake()
node.send(bf.filterload())
start_block = bytes.fromhex(last_block_hex)
getheaders = GetHeadersMessage(start_block=start_block)
node.send(getheaders)
print('ok2')
headers = node.wait_for(HeadersMessage)
print('ok3')
getdata = GetDataMessage()
for b in headers.blocks:
    if not b.check_pow():
        raise RuntimeError('proof of work is invalid')
    getdata.add_data(FILTERED_BLOCK_DATA_TYPE, b.hash())
node.send(getdata)
found = False
while not found:
    print('ok1')
    message = node.wait_for(MerkleBlock, Tx)
    if message.command == b'merkleblock':
        if not message.is_valid():
            raise RuntimeError('invalid merkle proof')
    else:
        for i, tx_out in enumerate(message.tx_outs):
            if tx_out.script_pubkey.address(testnet=True) == address:
                print('found: {}:{}'.format(message.id(), i))
                found = True
                break
