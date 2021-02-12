from helper import decode_base58, little_endian_to_int, hash256, SIGHASH_ALL, hash160, h160_to_p2sh_address
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey

# -- try of a 2 of 2 musig p2sh -- 

# 2 private key because 2 of 2

secret1 = little_endian_to_int(hash256(b'dat_test_private_key_p2sh1'))

secret2 = little_endian_to_int(hash256(b'dat_test_private_key2_p2sh2'))

# derived pubkeys

private_key1 = PrivateKey(secret1)
private_key2 = PrivateKey(secret2)

print(private_key1.point.address(testnet=True))

print(private_key2.point.address(testnet=True))

## first we create the scriptPubKey of the redeemscript or redeem script

# we decode our previous pubkey to put them in script commands

public_key1 = decode_base58('mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1')
public_key2 = decode_base58('mwjg9Y1jeFdNu7DQBAW7DUbJqj6jMmhd74')

#dat_redeem_script_t1 = 0x52, public_key1, public_key2, 0x52, 0xae

dat_redeem_script_op = Script([0x52, public_key1, public_key2, 0x52, 0xae])

dat_redeem_script_op_serialized = dat_redeem_script_op.serialize()

#dat_redeem_script = dat_redeem_script.raw_serialize()

dat_redeem_script_h160 = hash160(dat_redeem_script_op_serialized)

#dat_redeem_script_address = h160_to_p2sh_address(dat_redeem_script_op, testnet = True)

#print(dat_redeem_script_address)

# create a simple address to send to the p2sh address that will receive the fund

secret = little_endian_to_int(hash256(b'dat_test_private_key3'))

private_key3 = PrivateKey(secret)

public_key = print(private_key3.point.address(testnet=True, p2sh=True)) #2N7e6ZAGXoepdVYu2Y8ho7fTf6oxE3j9UwS
