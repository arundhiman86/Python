'''
Create a generator that yields "n" random numbers between a low and high number

'''

import random

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low, high)
