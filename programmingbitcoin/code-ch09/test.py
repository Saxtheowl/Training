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
from helper import run
import block
import ecc
import helper
import script
import tx
