tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
"""
def printTable(dat_list):
    colWidths = [0] * len(tableData)
    print(colWidths)
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            colWidths[y] = len(tableData[y][x])
#            lines[y] = '.join(tableData
            print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print()
    print(colWidths)

printTable(tableData)
"""
"""
def printTable(table):
    colWidths = [0] * len(table)
    for i in range(len(table)):
        for x in table[i]:
            if len(x) > colWidths[i]:
                colWidths[i] = len(x)
    print(colWidths)

    for i in range(len(table[0])):
        for x in range(len(table)):
            print(table[x][i].rjust(colWidths[x]),end = ' ')
            if x == len(table)-1:
                print('\r')
"""

tableData=[['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

longest = 0 # to find the longest line
lines = [] # to keep lines 

for elements in zip(tableData[0], tableData[1], tableData[2]):

    # join elements in line - like 'apples' + ' ' + 'Alice' + ' ' + 'dogs'
    line = ' '.join(elements) 

    # add line to the list
    lines.append(line) 

    #print(line) # you can print it to see what you get

    # find the longest line
    length = len(line)
    if length > longest:
        longest = length

#print('the longest:', longest)

longest += 1 # to get one space more at left side

# print lines using `%*s`
# if `longest` is 21 then it will works as `%21s`
for line in lines:
    print('%*s' % (longest, line))

printTable(tableData)
"""
datTable = ['salut', 'moi', 'cest', 'roger']

for i in range(len(datTable)):
    print(datTable[i].rjust(5))
"""
