'''
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

'''

def up_low(s):
    u = 0
    l = 0
    print('Original String :  Hello Mr. Rogers, how are you this fine Tuesday?')
    for i in s:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
    print(f'No. of Upper case characters : {u}')
    print(f'No. of Lower case Characters : {l}')
