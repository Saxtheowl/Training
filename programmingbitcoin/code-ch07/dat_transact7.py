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

secret1 = little_endian_to_int(hash256(b'dat_test_private_key_p2sh1'))

secret2 = little_endian_to_int(hash256(b'dat_test_private_key2_p2sh2'))

## first we create the scriptPubKey of the redeemscript or redeem script

# we decode our previous pubkey to put them in script commands

private_key1 = PrivateKey(secret1)
private_key2 = PrivateKey(secret2)

print(private_key1.point.address(testnet=True))

print(private_key2.point.address(testnet=True))

public_key1 = decode_base58('mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1')
public_key2 = decode_base58('mwjg9Y1jeFdNu7DQBAW7DUbJqj6jMmhd74')

dat_redeem_script_op = Script([0x52, public_key1, public_key2, 0x52, 0xae])

# make a transact to mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv with 60% of a UTXO and send back the change

secret = little_endian_to_int(hash256(b'dat_test_private_key'))

private_key = PrivateKey(secret)

public_key = print(private_key.point.address(testnet=False)) #1FiiobU54Sja2XB1pqtNzKB2VAkAzm2Ssi 
public_key = print(private_key.point.address(testnet=True)) # mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1

# UTXO that we gonna receive

prev_tx = bytes.fromhex('5419d7e0538c78f8de8d9e0bc020ec94fab386b82a5229b690be87b5f669f3f6')
prev_index = 0

# create the txin with the output of the UTXO we have been given

tx_in = TxIn(prev_tx, prev_index)
tx_outs = []

# output address that will receive the sat we have not spend

change_amount = int(0.00003 * 100000000)
change_h160 = decode_base58('mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1')
change_script = p2pkh_script(change_h160)
change_output = TxOut(amount=change_amount, script_pubkey = change_script)

# output address that will receive our sat

target_amount = int(0.00010 * 100000000)
target_h160 = decode_base58('2N7e6ZAGXoepdVYu2Y8ho7fTf6oxE3j9UwS')
target_script = p2pkh_script(target_h160)
target_output = TxOut(amount=target_amount, script_pubkey=dat_redeem_script_op)

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
