#test

from unittest import TestCase
from ecc import FieldElement, Point

"""prime = 19

for k in (1, 3, 4, 7, 13, 18):
    print([k*i % prime for i in range(prime)])

print()

for p in (7, 11, 17, 31):
#    print([(p**i) % p for i in range(p)])
    print([(p/i % p) for i in range(1, 10)])


class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        # end::source1[]
        # tag::source2[]
        if self.x is None and self.y is None:  # <1>
            return
        # end::source2[]
        # tag::source1[]
        if self.y**2 != self.x**3 + a * x + b:  # <1>
            raise ValueError('({}, {}) is not on the curve'.format(x, y))

#tab = [[4,2], [-1,-1], [77, 18], [7, 5]]
tab = [[109, 105], [17, 56], [200, 119], [1, 193], [42, 99]]
f = 223
#a = Point(1, 1, 5, 7)


#for i in tab:
for x, y in tab:
    if (y**2 % f) == ((x**3 + 7) % f):
        print("ok")
    else:
        print("wrong")

A(-1,8, 0,2)
B(1,5, 1,5)
C(-1,7, 0,9)

new1(-0,3, 1,7) -> (-2, 2,6)
"""

"""
tab = [[192, 105], [17, 56], [200, 119], [1, 193], [42, 99], [1, 1], [1, 1]]
prime = 223

a = FieldElement(0, prime)
b = FieldElement(7, prime)

def dat_test(x, y):
    return y**2 == x**3 + a*x + b


for x, y in tab:
    if dat_test(FieldElement(x, prime), FieldElement(y, prime)):
        print("ok")
    else:
        print("wrong")
"""

"""
prime = 223

a = FieldElement(0, prime)
b = FieldElement(7, prime)
x1 = FieldElement(192, prime)
y1 = FieldElement(105, prime)
x2 = FieldElement(17, prime)
y2 = FieldElement(56, prime)
p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
print(p1+p2)

tab = [[170, 142, 60, 139], [47, 71, 17, 56], [143, 98, 76, 66]]

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)

for xt1, yt1, xt2, yt2 in tab:
    x1 = FieldElement(xt1, prime)
    y1 = FieldElement(yt1, prime)
    x2 = FieldElement(xt2, prime)
    y2 = FieldElement(yt2, prime)
    p1 = Point(x1, y1, a, b)
    p2 = Point(x2, y2, a, b)
    print(p1+p2)
"""


"""
prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)

tab = [[2, 192, 105], [2, 143, 98], [2, 47, 71], [4, 47, 71], [8, 47, 71], [21, 47, 71]]

for mul, x_raw, y_raw in tab:
#    x = x_raw * mul
#    y = y_raw * mul
    x = FieldElement(x_raw, prime)
    y = FieldElement(y_raw, prime)
    p = Point(x, y, a, b)
    # cant do s * mul
    s = mul
    result = mul * p
    print(result)

#wtf
print()
prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x = FieldElement(47, prime)
y = FieldElement(71, prime)
p = Point(x, y, a, b)
for s in range(1,22):
    result = s*p
    print(s, result)
#    print('{}*(47,71)=({},{})'.format(s,result.x.num,result.y.num))
print(result)

"""

"""
#ex5

prime = 223
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x = FieldElement(15, prime)
y = FieldElement(86, prime)
p = Point(x, y, a, b)
product = p
count = 0

#while x != None and y != None:

while(product.x != None):
    product += p
    count += 1
    
print(product.y)
print(count)
"""

# test wether the generator G is on the curve y**2 = x**3 + 7
"""
gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
p = 2**256 - 2**32 - 977
print(gy**2 % p == (gx**3 + 7) % p)

# test wether the generator point G has the order n
"""

"""

x = None

print(type(x) == (int))

"""
