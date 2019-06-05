'''
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24

'''

def multiply(numbers):
    a = 1
    for i in numbers:
        a *=i
    return a
