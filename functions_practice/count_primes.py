'''
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

count_primes(100) --> 25

'''

def count_primes(num):
    a = []
    count = 0
    for i in range(2, num+1):
        flag = 0
        for j in range(2, int(i/2)+1):
            if i%j == 0:
                flag = 1
        if flag == 0:
            a.append(i)
            count +=1
    print(a)
    return count
