'''
PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *

'''

def print_big(letter):
    char = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    pattern = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for word in pattern:
        print('\n')
        for i in pattern[word]:
            print(char[i])
