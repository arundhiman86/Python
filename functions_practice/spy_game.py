'''
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False

'''

def spy_game(nums):
    a = []
    k = 0
    for i, j in enumerate(nums):
        if j == 0 and k < 2:
            a.append(j)
            k +=1
        if j == 7 and k == 2:
            a.append(j)
    if a[0] == a[1] == 0 and a[2] == 7:
        return True
    else:
        return False
