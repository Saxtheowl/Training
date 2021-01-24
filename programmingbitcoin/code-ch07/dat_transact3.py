from helper import decode_base58, little_endian_to_int, hash256, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey

# our old private key

private_key = PrivateKey(little_endian_to_int(hash256(b'dat_test_private_key')))

prev_tx1 = bytes.fromhex('23f031f63c53f8fbaf58ff5c2df34f60099d0ddb775ecf98dbf5f27fd5c555de')
prev_index1 = 0

tx_in1 = TxIn(prev_tx1, prev_index1)

tx_outs = []
target_amount = int((0.00100000 * 100000000) - 192)
target_h160 = decode_base58('mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv')
target_script = p2pkh_script(target_h160)
target_output = TxOut(amount=target_amount, script_pubkey=target_script)
tx_obj = Tx(1, [tx_in1], [target_output], 0, True)

z1 = tx_obj.sig_hash(0)
der1 = private_key.sign(z1).der()
sig1 = der1 + SIGHASH_ALL.to_bytes(1, 'big')
sec = private_key.point.sec()
script_sig1 = Script([sig1, sec])
tx_obj.tx_ins[0].script_sig = script_sig1
print(tx_obj.serialize().hex())
