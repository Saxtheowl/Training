#!/usr/bin/python

my_rand_list = [5, 6, 4, 1, 7, 3, 2, 0, 8, 9]
largest = -1

for item in my_rand_list:
    if(item > largest):
        largest = item
        print largest,
print
print 'largest number ', largest
        
