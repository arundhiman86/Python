'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶

old_macdonald('macdonald') --> MacDonald

Note: 'macdonald'.capitalize() returns 'Macdonald'

'''

def old_macdonald(name):
    a =''
    if len(name) > 3:
        a = name[0].capitalize() + name[1:3] + name[3:].capitalize()
        return a
    else:
        return 'Name too short!'
