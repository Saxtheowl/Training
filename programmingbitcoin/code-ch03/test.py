#test

from unittest import TestCase

"""prime = 19

for k in (1, 3, 4, 7, 13, 18):
    print([k*i % prime for i in range(prime)])

print()

for p in (7, 11, 17, 31):
#    print([(p**i) % p for i in range(p)])
    print([(p/i % p) for i in range(1, 10)])
"""

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
tab = 

#a = Point(1, 1, 5, 7)


#for i in tab:
for x, y in tab:
    try:
        if Point(y, x, 5, 7):
            print("ok")
#            print("y =%d", y)
    except:
        print("wrong")
#        print("y =%d", y)
"""        if (Point(x, y, 5, 7):

            print("ok for %d %d", x, y)

"""

"""
A(-1,8, 0,2)
B(1,5, 1,5)
C(-1,7, 0,9)

new1(-0,3, 1,7) -> (-2, 2,6)
