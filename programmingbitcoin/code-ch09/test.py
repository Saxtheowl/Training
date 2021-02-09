############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
from importlib import reload
from helper import run
from block import Block
import ecc
import helper
import script
import tx

# import requests

# def get_url(testnet=False):
#     if testnet:
#         return 'http://testnet.programmingbitcoin.com'
#     else:
#         return 'http://mainnet.programmingbitcoin.com'

# tx_id = '1ed5583812bda08b71a71c2fa1e6788dac956efa9d2c26b6c9fd10f6e885658f'

# url = '{}/tx/{}.hex'.format(get_url(True), tx_id)

# print(url)

# response = requests.get(url)
# print(response.text.strip())

############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function

from importlib import reload
from helper import run, hash256
from io import BytesIO
import block
import ecc
import helper
import script
import tx
import signal
import sys
import random

# #print(type(b'\x00'))
# #print(type(0xffffffff))

# # from io import BytesIO
# # from block import Block
# # b = Block.parse(BytesIO(bytes.fromhex('020000208ec39428b17323fa0ddec8e887b\
# # 4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3\
# # f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')))
# # print('BIP9: {}'.format(b.version >> 29 == 0b001))

# dat_prev_block_hash = '000000000000001adf44c7d697675855572eca4dd4db7d0c0b845916d849af76'
# dat_prev_block_hash_t1 = '11111111111111adf44c7d697675855572eca4dd4db7d0c0b845916d849af76'
# dat_nonce = 0
# dat_try = hash256(str(dat_nonce).encode())
# dat_tab = []
# dat_nb_try = 0

# def dat_end_print():
#     for _ in dat_tab:
#         print(_)
#     print('dat_nonce: {} dat_try: {}'.format(dat_nonce, dat_try))
#     print('len dat_tab: {}'.format(len(dat_tab)))
#     print('dat nb try: {}', format(dat_nb_try))

# def signal_handler(sig, frame):
#     print('You pressed Ctrl+C!')
#     dat_end_print()
#     sys.exit(0)
# signal.signal(signal.SIGINT, signal_handler)

# while dat_try[:4] != b'\x00' * 4:# + b'\0':
#     if dat_try[:2] == b'\x00' * 2:
#         dat_tab.append(dat_try)
#     dat_nonce +=1
# #    dat_nonce = random.randint(1, 9999999999999999)
#     dat_try = hash256(str(dat_nonce).encode())
#     dat_nb_try += 1

# # def dat_end_print():
# #     for _ in dat_tab:
# #         print(_)
# #     print('dat_nonce: {} dat_try: {}'.format(dat_nonce, dat_try))
# #     print('len dat_tab: {}'.format(len(dat_tab)))
# #     print('dat nb try: {}', format(dat_nb_try))
   
# dat_end_print()

block_raw = bytes.fromhex('04000000fbedbbf0cfdaf278c094f187f2eb987c86a199da22bbb20400000000000000007b7697b29129648fa08b4bcd13c9d5e60abb973a1efac9c8d573c71c807c56c3d6213557faa80518c3737ec1')
stream = BytesIO(block_raw)
block = Block.parse(stream)
dat_target = block.target()

raw_bytes = dat_target.to_bytes(32, 'big')
raw_bytes = raw_bytes.lstrip(b'\x00')
if raw_bytes[0] > 0x7f:
    exponent = len(raw_bytes) + 1
    coefficient = b'\x00' + raw_bytes[:2]
else:
    exponent = len(raw_bytes)
    coefficient = raw_bytes[:3]
new_bytes = coefficient[::-1] + bytes([exponent])

