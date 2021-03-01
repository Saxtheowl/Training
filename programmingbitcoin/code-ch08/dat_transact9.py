from helper import decode_base58, little_endian_to_int, hash256, SIGHASH_ALL, hash160, h160_to_p2sh_address
from script import p2pkh_script, p2sh_script, Script
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey

secret = little_endian_to_int(hash256(b'dat_test_private_key'))

private_key = PrivateKey(secret)

public_key = print(private_key.point.address(testnet=False)) #1FiiobU54Sja2XB1pqtNzKB2VAkAzm2Ssi 
public_key = print(private_key.point.address(testnet=True)) # mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1

secret1 = little_endian_to_int(hash256(b'dat_test_private_key_p2sh1'))

secret2 = little_endian_to_int(hash256(b'dat_test_private_key2_p2sh2'))

## first we create the scriptPubKey of the redeemscript or redeem script

# we decode our previous pubkey to put them in script commands

private_key1 = PrivateKey(secret1)
private_key2 = PrivateKey(secret2)

public_key1 = decode_base58('mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1')
public_key2 = decode_base58('mwjg9Y1jeFdNu7DQBAW7DUbJqj6jMmhd74')

#redeem script as op code

dat_redeem_script_op = Script([0x52, public_key1, public_key2, 0x52, 0xae])

# we serialize it in binary

dat_redeem_script_serialized = dat_redeem_script_op.serialize()

# hash 160

dat_redeem_script_h160 = hash160(dat_redeem_script_serialized)

# we get the address

dat_redeem_script_address = h160_to_p2sh_address(dat_redeem_script_h160, testnet=True)

# get it back in bytes

dat_target_h160 = decode_base58(dat_redeem_script_address)

# use the result to build our p2sh_script

target_script = p2sh_script(dat_target_h160)

print(target_script)
print('is p2sh: {}'.format(target_script.is_p2sh_script_pubkey()))

print(dat_redeem_script_h160)
print()
print(dat_redeem_script_address)

# UTXO that we gonna receive

prev_tx = bytes.fromhex('a0cbae8045fd0a52f198c21c855874dbad44cc964ead3ed4d8fb1838ce4b9e4b')
prev_index = 0

# create the txin with the output of the UTXO we have been given

tx_in = TxIn(prev_tx, prev_index)

# output address that will receive our sat

target_amount = int(0.00009 * 100000000)
target_output = TxOut(amount=target_amount, script_pubkey=target_script)

tx_obj = Tx(1, [tx_in], [target_output], 0, True)

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
