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

#print(type(b'\x00'))
#print(type(0xffffffff))

# from io import BytesIO
# from block import Block
# b = Block.parse(BytesIO(bytes.fromhex('020000208ec39428b17323fa0ddec8e887b\
# 4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3\
# f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d')))
# print('BIP9: {}'.format(b.version >> 29 == 0b001))

print(hash256(bytes.fromhex('020000208ec39428b17323fa0ddec8e887b4a7c53b8c0a0a220cfd0000000000000000005b0750fce0a889502d40508d39576821155e9c9e3f5c3157f961db38fd8b25be1e77a759e93c0118a4ffd71d'))[::-1])
