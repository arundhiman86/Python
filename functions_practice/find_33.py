'''
FIND 33:

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False

'''

def has_33(nums):
    flag = 0
    j = 0
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == 3:
            flag = 1
            print('True')
        j += 1
    if flag == 0:
        print("False")
