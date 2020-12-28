#!

"""grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
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


grid2 = []

#def GenMap(size x):


for x in range(len(grid[0])):
    for y in range(len(grid)):
        if grid[y][x] == 'O': #or grid[y][x] == '.':
            grid[y][x] = ' '

print('python way:')
    
for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print()

print('c way:')
    
print('\n'.join(map(''.join, grid)))

print("test way:")

x = 0
y = 0

while x < len(grid):
    while y < len(grid[y]):
        print(grid[x][y], end='')
        y += 1
    x += 1
    y = 0
    print()

print()
print('last test:')

x = 50
y = 50

grid2 = [['0' for i in range(x)] for j in range(y)]

"""

for x in range(99):
    for y in range(99):
        grid2[y][x] = '0'

"""

print(x)
print(y)
    
print('python way:')

for x in range(x):
    for y in range(y):
        print(grid2[y][x], end='')
    print()
