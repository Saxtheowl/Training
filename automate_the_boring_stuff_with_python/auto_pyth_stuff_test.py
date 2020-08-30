import random, sys, pyperclip

def hello(name):
    hello("lul")

def hello2():
    i = 5
    while i in range(1, 10):
        print(i)

def PasswordTest():
    while True:
        print('Whats is your name ?')
        name = input()
        if name != 'Roger':
            continue
        print('Hi roger, whats the password ?')
        password = input()
        if password == 'sniper32':
            break
    print('Access Granted')

def spam(num):
    return 42 / num

"""
try:
    print(spam(1))
    print(spam(0))
except ZeroDivisionError:
    print('error div by zero')
"""

def GuessGame():
    print('guess a number between 1 and 20')
    answer = random.randrange(1, 20)
    guess = None
    while guess != answer:
        try:
            guess = int(input())
        except ValueError:
            print('wrong value input')
            sys.exit()
        if(guess > answer):
            print('it is less')
        elif(guess < answer):
            print('it is more')
    print('correct it was ' + str(answer))

def GuessGame2():
    print('guess a number between 1 and 20')
    answer = random.randrange(1, 20)
    guess = None
    for NumberGuessed in range(1, 3):
        try:
            guess = int(input())
        except ValueError:
            print('wrong value input')
            sys.exit()
        if(guess > answer):
            print('it is less')
        elif(guess < answer):
            print('it is more')
        elif(guess == answer):
            print('correct it was ' + str(answer))
        else:
            break


"""cat = ['blue', '10']
color, weight = cat
for i in range(len(cat)):
    print(cat[i])"""
"""spam = [9, 2, 3, 8]
print(spam)
spam.sort()
print(spam)
"""

"""
eggs = [1, 2, 3]
eggs[0] = 4
print(eggs)
bacon = 'bacon'
print(bacon[1])
bacon[1] = 'b'

"""
"""
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
"""
"""
dat_list = [1,2,3,4]

for i in range(len(dat_list)):
    print(dat_list[i])
"""

"""

print(r'a')

dat_list = ['je', 'mappel', 'roger', ', ']

print(' '.join(dat_list).split(' '))
"""

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
print('\n'*10)

print('HELLO WORLD'.center(50, '-'))
