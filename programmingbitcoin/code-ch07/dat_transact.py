############## PLEASE RUN THIS CELL FIRST! ###################

# import everything and define a test runner function
"""

from importlib import reload
from helper import run, little_endian_to_int
import ecc
import helper
import tx
import script
import io

"""

"""
dat_s = io.BytesIO(b'abc')
print(little_endian_to_int(dat_s.read(4)))

"""

from helper import decode_base58, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx



# make a transact to mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv with 60% of a UTXO and send back the change

#secret = little_endian_to_int(hash256(b'dat_test_private_key'))

#public key = print(private_key.point.address(testnet=True)) mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1
