""" from hashlib import sha256
x = 5
y = 0  # We don't know what y should be yet...
a = 0
b = 0
while b != "00":
    a = sha256(f'{x*y}'.encode())
    b = a.hexdigest()[:999]
    print(b)
    y += 1
print(f'The solution is y = {y}')

"""

"""a = sha256(str{y*X}.encode()).hexdigest()[-1]"""

name = 'roger'

print(f"bonjour {name} ca va?")