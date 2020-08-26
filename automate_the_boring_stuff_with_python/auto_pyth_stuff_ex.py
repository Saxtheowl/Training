import sys

def collatz(number):
    if number % 2 == 0:
        to_ret = number / 2
    elif number % 2 == 1:
        to_ret = 3 * number + 1
    print(int(to_ret))
    return(int(to_ret))

def collatz2():
    print('enter a number')
    try:
        guess = int(input())
    except ValueError:
        print('you can only enter integer')
        sys.exit()
    while guess != 1:
        guess = collatz(guess)

#collatz2()
"""
spam= ['apples', 'bananas', 'tofu', 'cats']

def list_thing(list):

#creating a string then splitting it as list with two items, second being last word
    new_string=', '.join(list).rsplit(',', 1)    

#Using the same method used above to recreate string by replacing the separator.

    new_string=' and'.join(new_string)
    return new_string

#ExampleList = ['apple', 'orange', 'tomatoes']
ExampleList = ['apple']
print(list_thing(ExampleList))

"""
"""
spam = ['apples', 'bananas', 'tofu', 'cats']

def merge(list):
  return ', '.join(list[:-1] + ['and '+list[-1]])

print(merge(spam))
"""
"""
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple[:-1])
b = "b".join(myTuple[-1])
print(b)
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
"""
while x < len(grid[0]):
    x+=1
    while y < len(grid):
        y+=1
        print(grid[y][x], end='')
    print()
   """ 
"""
for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print()
"""
"""
print(list(range(len(grid[0]))))

print(list(range(1, 100)))
"""
"""
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
"""
"""
DatBirthday = {'roger': '1 dec', 'alfred': '3 april', 'benoit': '4 april'}

while True:
    print("Enter Name:")
    name = input()
    if name == '':
        print('', end='')
    elif name in DatBirthday:
            print("the birthday of, %s is, %s" % name, DatBirthday[name])
    else:
        print("Not in directory, enter date of birth:")
        DateOfBirth = input()
        DatBirthday[name] = DateOfBirth
    

#print('%s', DatBirthday[name])

#print("Hello, %s!" % DatBirthday[name])
"""

"""
spam = {'color': 'red', 'age': 42}

for i in spam.items():
    print(i)

for k, v in spam.items():
    print('key is ' + k + ' and value is ' + str(v))
"""
"""
picnicItems = {'apple': 4, 'cups': 2}
print('I am bringing ' + str(picnicItems['cup']) + ' cups.')
"""
"""
import pprint

message = 'salut mon nom est roger'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
"""

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
"""
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
"""
def DisplayInventory(inv):
    print('Inventory:')
    for k, v in inv:
        print(str(v) + ' ' + str(k))

DisplayInventory(inventory)
