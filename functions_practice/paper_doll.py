'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

'''

def paper_doll(text):
    a = '' 
    for i in text:
        a = a + i*3
    return a
