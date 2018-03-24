import re

dat_string = raw_input('Enter some words: ')
cnt = 0
tmp = 0

for c in dat_string:
    cnt += 1
print 'The string ' + dat_string + ' has ' + str(cnt) + ' characters in it.'
