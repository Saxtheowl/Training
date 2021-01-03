from ecc import S256Point, PrivateKey, Signature, G, N
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

priv = PrivateKey(int(0xdeadbeef12345))

#priv = (b'\x04' + priv.point.x.num.to_bytes(32, 'big') + priv.point.y.num.to_bytes(32, 'big'))

#print(priv.hex())

#print(e)
priv = PrivateKey(0xdeadbeef12345)
#print(priv.point.sec())
#print(priv.point.sec(compressed=False).hex())

#txt = "For only {price} dollars!"
#print(txt.format(price = 49))
"""
tab = [5001, 2019**5, 0xdeadbeef54321]

for i in tab:#(5001, 2019**5, 0xdeadbeef54321):
    dat_var = PrivateKey(i)
    print(dat_var.point.sec(compressed=True).hex())
"""

"""
a = 1234
#print(a[1:4])

a = (b'\x04' + a.to_bytes(32, 'big'))

print(a)

"""

r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec

#dat_sig = (0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6 + 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec)

dat_sig = Signature(r, s)

print(type(r))
print(type(s))
#print(dat_sig)
print(dat_sig.der().hex())

#print(dat_sig)
