import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
            if text[7] != '-':
                return False
            for i in range(8, 12):
                if not text[i].isdecimal():
                    return False
            return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    print("old i =%d", int(i))
#    print('chunk to test is:%s', chunk)
    if isPhoneNumber(chunk):
        print(int(i))
        print('Phone number found: ' + chunk)
print('Done')
"""
phoneNumRegex=re.compile('r\d\d\d-\d\d\d-\d\d\d')
mo=phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
"""
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
#print('Phone number found: ' + mo.group())
#print(mo.group())
mo.groups(1)
#Phone number found: 415-555-4242
"""
batRegex = re.compile(r'(Ha){3}')
mo1 = batRegex.search('HahaHa')
print(mo1.group())
"""

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHa')
#mo1.groups(1)

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall(r'12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 wans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

atRegex = re.compile(r'.at')
save = atRegex.findall('the cat in the hat sat on the flat mat.')
print(save)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
save = mo.groups(0)
print(save)

robocop = re.compile(r'robocop', re.I)
print(robocop.search('Robocop is part man, part machine, all cop.').group())

agentNamesRegex = re.compile(r'Agent \')
test = print(agentNamesRegex.findall(r'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

print(test)
