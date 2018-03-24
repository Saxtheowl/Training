import re

dat_string = raw_input('Enter some words: ')
cnt = 0
cnt2 = 0

for c in dat_string:
    cnt2 += 1
    if c in ['a','e','i','o','u','A','E','I','O','U']:
        cnt += 1
print str(cnt) + ' letters in ' + str(cnt2) + ' are vowels.'
