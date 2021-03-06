from helper import decode_base58, little_endian_to_int, hash256, SIGHASH_ALL, hash160, h160_to_p2sh_address
from script import p2pkh_script, p2sh_script, Script
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey

# we send to a p2sh address

secret1 = little_endian_to_int(hash256(b'dat_test_private_key_p2sh1'))

secret2 = little_endian_to_int(hash256(b'dat_test_private_key2_p2sh2'))

private_key1 = PrivateKey(secret1)
private_key2 = PrivateKey(secret2)

print(private_key1.point.address(testnet=True)) #mfchv5Xq63UuQTAVwzqhWVHAZVkiZrhDKh 
print(private_key2.point.address(testnet=True)) #ms4kdy8Hn4WfxK2J2VpbonTit5NeNy6vJS

## first we create the scriptPubKey of the redeemscript or redeem script

# we decode our previous pubkey to put them in script commands

public_key1 = decode_base58('mfchv5Xq63UuQTAVwzqhWVHAZVkiZrhDKh')
public_key2 = decode_base58('ms4kdy8Hn4WfxK2J2VpbonTit5NeNy6vJS')

#redeem script as op code

dat_redeem_script_op = Script([0x52, public_key1, public_key2, 0x52, 0xae])
print('dat_redeem_script_op:{}'.format(dat_redeem_script_op))

# we serialize it in binary

dat_redeem_script_serialized = dat_redeem_script_op.serialize()
print('dat_redeem_script_serialized:{}'.format(dat_redeem_script_serialized))

# hash 160

dat_redeem_script_h160 = hash160(dat_redeem_script_serialized)

print('dat_redeem_script_h160:{}'.format(dat_redeem_script_h160))

# we get the address

dat_redeem_script_address = h160_to_p2sh_address(dat_redeem_script_h160, testnet=True)

print('dat_redeem_script_address:{}'.format(dat_redeem_script_address))

# get it back in bytes

dat_target_h160 = decode_base58(dat_redeem_script_address)

print('dat_redeem_script_h160:{}'.format(dat_target_h160))

# use the result to build our p2sh_script

target_script = p2sh_script(dat_target_h160)

print('target script :{}'.format(target_script))
print('is p2sh: {}'.format(target_script.is_p2sh_script_pubkey()))

print(dat_redeem_script_h160)
print()
print('redeem script address: {}'.format(dat_redeem_script_address))

# UTXO that we gonna receive

prev_tx = bytes.fromhex('6a8d25641686f572c7b5bba56c49db66ff0b896b447d2a768933cf818472958e')
prev_index = 1

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
