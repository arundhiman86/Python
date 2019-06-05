'''
Write a function that checks whether a number is in a given range (inclusive of high and low)

'''

def ran_check(num,low,high):
    if num in range(low, high+1):
        return f'{num} is in range between {low} to {high}'
