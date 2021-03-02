from helper import decode_base58, little_endian_to_int, hash256, SIGHASH_ALL, hash160, h160_to_p2sh_address
from script import p2pkh_script, p2sh_script, Script
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey

# make a tx from a p2sh address

secret1 = little_endian_to_int(hash256(b'dat_test_private_key_p2sh1'))

secret2 = little_endian_to_int(hash256(b'dat_test_private_key2_p2sh2'))

private_key1 = PrivateKey(secret1)
private_key2 = PrivateKey(secret2)

public_key1 = decode_base58('mfchv5Xq63UuQTAVwzqhWVHAZVkiZrhDKh')
public_key2 = decode_base58('ms4kdy8Hn4WfxK2J2VpbonTit5NeNy6vJS')

#redeem script as op code

dat_redeem_script_op = Script([0x52, public_key1, public_key2, 0x52, 0xae])

# we serialize it in binary

dat_redeem_script_serialized = dat_redeem_script_op.serialize()

prev_tx = bytes.fromhex('f387eba7393e07b4c2134cd29551b7294a992c9bae129b347b64ba6650522acb')
prev_index = 0

target_h160 = decode_base58('mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1')
target_script = p2pkh_script(target_h160)

target_amount = int(0.00008 * 100000000)
target_output = TxOut(amount=target_amount, script_pubkey=target_script)

tx_in = TxIn(prev_tx, prev_index)

tx_obj = Tx(1, [tx_in], [target_output], 0, True)

z = tx_obj.sig_hash(0)
private_key1 = PrivateKey(secret1)
private_key2 = PrivateKey(secret2)
der1 = private_key1.sign(z).der()
der2 = private_key2.sign(z).der()
sig1 = der1 + SIGHASH_ALL.to_bytes(1, 'big')
sig2 = der2 + SIGHASH_ALL.to_bytes(1, 'big')
script_sig = Script([0x00, sig1, sig2, dat_redeem_script_serialized])
print('script_sig=:{}'.format(script_sig))
tx_obj.tx_ins[0].script_sig = script_sig
print(tx_obj.serialize().hex())

# end
