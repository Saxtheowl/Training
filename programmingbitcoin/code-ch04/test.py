from ecc import S256Point, PrivateKey, G, N
from helper import hash256

#5,000
#2,018**5
#0xdeadbeef12345
"""
#e = int.from_bytes(hash256(b'5000'), 'big')
e = PrivateKey(5000)
#point = e*G
dat_test = (b'x04' + point.x.num.to_bytes(32, 'big') + point.y.num.to_bytes(32, 'big'))

print(dat_test.hex())
"""

#print(priv.point.sec(compressed=False).hex())

priv = PrivateKey(5000)

priv = (b'x04' + priv.point.x.num.to_bytes(32, 'big') + priv.point.y.num.to_bytes(32, 'big'))

print(priv.hex())

#print(e)
