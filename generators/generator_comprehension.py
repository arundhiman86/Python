'''
Using generator comprehension iterate through the list below, and print out the elements greater than 3.

my_list = [1,2,3,4,5]

'''

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
