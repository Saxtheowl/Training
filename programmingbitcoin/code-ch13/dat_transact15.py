from helper import decode_base58, little_endian_to_int, hash256, SIGHASH_ALL, hash160, h160_to_p2sh_address
from script import p2pkh_script, p2sh_script, Script
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey

# make a tx from a p2sh address

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
print('dat_redeem_script_serialized:{}'.format(dat_redeem_script_serialized))

prev_tx = bytes.fromhex('74aa4bb3ab5bd9966b8a06c442c37eb9177339dfdb1b1594a8d174e1dc201ff5')
prev_index = 0

target_h160 = decode_base58('mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1')
target_script = p2pkh_script(target_h160)

target_amount = int(0.00008 * 100000000)
target_output = TxOut(amount=target_amount, script_pubkey=target_script)

tx_in = TxIn(prev_tx, prev_index)

# output address that will receive our sat

tx_obj = Tx(1, [tx_in], [target_output], 0, True)

# now we sign the p2sh tx

z = tx_obj.sig_hash(0)
#private_key = PrivateKey(little_endian_to_int(hash256(b'dat_test_private_key')))
private_key1 = PrivateKey(secret1)
private_key2 = PrivateKey(secret2)
der1 = private_key1.sign(z).der()
der2 = private_key2.sign(z).der()
sig1 = der1 + SIGHASH_ALL.to_bytes(1, 'big')
sig2 = der2 + SIGHASH_ALL.to_bytes(1, 'big')
#sec = private_key.point.sec()
#print(sec.hex())
script_sig = Script([0x00, sig1, sig2, dat_redeem_script_serialized])
print('script_sig=:{}'.format(script_sig))

tx_obj.tx_ins[0].script_sig = script_sig
print(tx_obj.serialize().hex())

# end
