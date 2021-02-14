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

from helper import decode_base58, little_endian_to_int, hash256, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey

# make a transact to mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv with 60% of a UTXO and send back the change

secret = little_endian_to_int(hash256(b'dat_test_private_key'))

private_key = PrivateKey(secret)

public_key = print(private_key.point.address(testnet=False)) #1FiiobU54Sja2XB1pqtNzKB2VAkAzm2Ssi 
public_key = print(private_key.point.address(testnet=True)) # mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1

# UTXO that we gonna receive

prev_tx = bytes.fromhex('1ed5583812bda08b71a71c2fa1e6788dac956efa9d2c26b6c9fd10f6e885658f')
prev_index = 1

# create the txin with the output of the UTXO we have been given

tx_in = TxIn(prev_tx, prev_index)
tx_outs = []
change_amount = int(0.00003 * 100000000)

# output address that will receive the sat we have not spend

change_h160 = decode_base58('mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1')
change_script = p2pkh_script(change_h160)
change_output = TxOut(amount=change_amount, script_pubkey = change_script)

# output address that will receive our sat

target_amount = int(0.00006 * 100000000)
target_h160 = decode_base58('mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv')
print()
print(target_h160)

target_script = p2pkh_script(target_h160)
print()
print(target_script)
target_output = TxOut(amount=target_amount, script_pubkey=target_script)
tx_obj = Tx(1, [tx_in], [change_output, target_output], 0, True)
#print(tx_obj).hex()

# now we sign the transaction

z = tx_obj.sig_hash(0)
private_key = PrivateKey(little_endian_to_int(hash256(b'dat_test_private_key')))
der = private_key.sign(z).der()
sig = der + SIGHASH_ALL.to_bytes(1, 'big')
sec = private_key.point.sec()
script_sig = Script([sig, sec])
tx_obj.tx_ins[0].script_sig = script_sig
print(tx_obj.serialize().hex())

# end

