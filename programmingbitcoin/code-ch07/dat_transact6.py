from helper import decode_base58, little_endian_to_int, hash256, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey

secret = little_endian_to_int(hash256(b'dat_test_private_key'))

private_key = PrivateKey(secret)

public_key = print(private_key.point.address(testnet=True))

prev_tx1 = bytes.fromhex('df29440e796ff7e843d643380d00b79f0d6dab55c84a983849b04f9a8025f072')
prev_index1 = 0
prev_tx2 = bytes.fromhex('47c0095c4e40c79128037c3861445c7f7d93e6ff9b55c10274395798f3503da8')
prev_index2 = 0

tx_in1 = TxIn(prev_tx1, prev_index1)
tx_in2 = TxIn(prev_tx2, prev_index2)

target_amount = 18000
target_h160 = decode_base58('mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1')
target_script = p2pkh_script(target_h160)
target_output = TxOut(amount = target_amount, script_pubkey = target_script)

tx_obj = Tx(1, [tx_in1, tx_in2], [target_output], 0, True)

z1 = tx_obj.sig_hash(0)
z2 = tx_obj.sig_hash(1)
private_key = PrivateKey(little_endian_to_int(hash256(b'dat_test_private_key')))
der1 = private_key.sign(z1).der()
der2 = private_key.sign(z2).der()
sig1 = der1 + SIGHASH_ALL.to_bytes(1, 'big')
sig2 = der2 + SIGHASH_ALL.to_bytes(1, 'big')
sec = private_key.point.sec()
script_sig1 = Script([sig1, sec])
script_sig2 = Script([sig2, sec])
tx_obj.tx_ins[0].script_sig = script_sig1
tx_obj.tx_ins[1].script_sig = script_sig2
print(tx_obj.serialize().hex())
