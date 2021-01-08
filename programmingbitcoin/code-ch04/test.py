from ecc import S256Point, PrivateKey, Signature, FieldElement, G, N
from helper import hash256, encode_base58, encode_base58_checksum, int_to_little_endian
import sys

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

"""
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec

#dat_sig = (0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6 + 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec)

dat_sig = Signature(r, s)

print(type(r))
print(type(s))
#print(dat_sig)
print(type(dat_sig.der().hex().encode('ascii')))
print(dat_sig.der().hex())

#print(dat_sig)

"""

"""

b = bytearray([1] * 100)
b[0:3] = b'\0'
a = b'\0lulfdsfds'
print(type(a))
#print(type(b))
print(encode_base58(a))
print(encode_base58(b))

"""

#tab = ['7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d', 'eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c', 'c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6']

#for i in tab:
#    tab[i].to_bytes()
#bytes.fromhex(item)
"""
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def encode_base58(s):
    count = 0
    for c in s:
        if c == 0:
            count += 1
        else:
            break
        num = int.from_bytes(s, 'big')
        prefix = '1' * count
        result = ''
        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE58_ALPHABET[mod] + result
            return prefix + result
"""

"""

h = '7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d'

print(encode_base58(bytes.fromhex(h))

"""

"""

5002 (use uncompressed SEC on testnet)
2020 5 (use compressed SEC on testnet)
0x12345deadbeef (use compressed SEC on mainnet)

"""

"""

a = 333
#generate the private key with the integer 333
priv = PrivateKey(5002)
priv2 = PrivateKey(2020**5)
priv3 = PrivateKey(0x12345deadbeef)
print(priv.hex())
#'{:x}'.format(self.secret).zfill(64)
print('{:x}'.format(a).zfill(64))
print(sys.getsizeof(priv.secret))
print(priv.secret)
print()
print(sys.getsizeof(priv.hex()))
print(priv.hex())
# create the public key as SEC format with the private key 
#priv = priv.point.address(priv.point.sec(compressed=False))
print(priv.point.address(compressed=False, testnet=True))
print(priv2.point.address(compressed=True, testnet=True))
print(priv3.point.address(compressed=True, testnet=False))

"""

# encode the SEC format to addresses format (ripemd160)
#priv = .address(priv)
"""print(sys.getsizeof(priv))
print(priv)
priv = priv.hex()
print(sys.getsizeof(priv))
"""
#                      print(priv.point.sec(compressed=False).hex())
"""
print()
p = 2**256 - 2**32 - 977
gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8

x = FieldElement(gx, p)

print('{:x}'.format(x).zfill(64))


"""

"""

priv = PrivateKey(5003)
priv2 = PrivateKey(2021**5)
priv3 = PrivateKey(0x54321deadbeef)

print(priv.wif(compressed=True, testnet=True))
print(priv2.wif(compressed=False, testnet=True))
print(priv3.wif(compressed=True, testnet=False))

"""

priv = PrivateKey(9092092091210920920919099930002)

print(priv.point.address(testnet=True))
print(sys.getsizeof(priv))

r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec

dat_sig = Signature(r, s)

#print(type(dat_sig.der().hex().encode('ascii')))
print(dat_sig.der().hex())
print(sys.getsizeof(dat_sig))
print(encode_base58_checksum(dat_sig.der()))
print(sys.getsizeof(dat_sig))

num = 10011545

print(int_to_little_endian(num, 8))
