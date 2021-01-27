from helper import decode_base58, little_endian_to_int, hash256, SIGHASH_ALL
from script import p2pkh_script, Script
from tx import TxIn, TxOut, Tx
from ecc import PrivateKey

# use 2 txin to send to mwJn1YPMq7y5F8J3LkC5Hxg9PHyZ5K4cFv

# our old private key

private_key = PrivateKey(little_endian_to_int(hash256(b'dat_test_private_key')))

# some sats from a previous tx

prev_tx1 = bytes.fromhex('74699b8cc3dd67bdd54314283603c72b76a09368e5646b5b29c28028d5ae0076')
prev_index1 = 1

# sats from change of the tx of previous exercise

prev_tx2 = bytes.fromhex('47c0095c4e40c79128037c3861445c7f7d93e6ff9b55c10274395798f3503da8')
prev_index2 = 1

tx_in1 = TxIn(prev_tx1, prev_index1)
tx_in2 = TxIn(prev_tx2, prev_index2)

# where we send our sats

tx_outs = []
target_amount = 200000
target_h160 = decode_base58('mvEg6eZ3sUApodedYQrkpEPMMALsr1K1k1')
target_script = p2pkh_script(target_h160)
target_output = TxOut(amount=target_amount, script_pubkey=target_script)
tx_obj = Tx(1, [tx_in1, tx_in2], [target_output], 0, True)

# we sign

z1 = tx_obj.sig_hash(0)
z2 = tx_obj.sig_hash(1)
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
