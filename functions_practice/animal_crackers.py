'''
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False

'''

def animal_crackers(text):
    a = text.split()
    if a[0][0] == a[1][0]:
        return True
    else:
        return False
