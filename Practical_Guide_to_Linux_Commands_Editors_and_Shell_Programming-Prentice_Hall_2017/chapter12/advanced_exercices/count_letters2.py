import re

dat_string = raw_input('Enter some words: ')
cnt = 0
tmp = 0

"""for c in dat_string:
    if c == 'a':
        cnt += 1
print 'The string ' + dat_string + ' has ' + str(cnt) + ' vowels in it.'
"""

for c in dat_string:
    if c in ['a','e','i','o','u','A','E','I','O','U']:
        cnt += 1
print 'The string ' + dat_string + ' has ' + str(cnt) + ' vowels in it.'

