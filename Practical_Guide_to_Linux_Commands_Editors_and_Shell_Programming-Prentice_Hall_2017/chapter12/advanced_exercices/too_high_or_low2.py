import random

def too_high_or_low(val):
    nb_entered = int(raw_input('Enter a number: '))
    if nb_entered < val:
        print 'number is too low'
        return -1
    elif nb_entered > val:
        print 'number is too high'
        return 1
    else:
        print 'Got it'
        return 0

too_high_or_low(random.randint(0, 10))
