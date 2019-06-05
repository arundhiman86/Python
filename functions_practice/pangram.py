'''
Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

'''

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    print(set(''.join(str1.lower().split())))
    print(set(alphabet))
    return set(alphabet) == set(''.join(str1.lower().split()))
