'''
Create a generator that generates the squares of numbers up to some number N

'''

def gensquares(N):
    for i in range(N):
        yield i**2
