#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5

    
#### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False


#### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
    makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False

    
#### OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
    old_macdonald('macdonald') --> MacDonald


#### MASTER YODA: Given a sentence, return a sentence with the words reversed
    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'
    

#### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
    almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True
    
    
#### FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False
    
    
#### PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
    
    
#### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19
    
    
#### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
    summer_69([1, 3, 5]) --> 9
    summer_69([4, 5, 6, 7, 8, 9]) --> 9
    summer_69([2, 1, 6, 9, 11]) --> 14
    
    
#### SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
     spy_game([1,2,4,0,0,7,5]) --> True
     spy_game([1,0,2,4,0,5,7]) --> True
     spy_game([1,7,2,0,4,5,0]) --> False
     
     
#### COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
    count_primes(100) --> 25


#### PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
    print_big('a')
    
    out:   *  
          * *
         *****
         *   *
         *   *


**Write a function that computes the volume of a sphere given its radius.**
<p>The volume of a sphere is given as $$\frac{4}{3} πr^3$$</p>


**Write a function that checks whether a number is in a given range (inclusive of high and low)**


**Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output : 
    No. of Upper case characters : 4
    No. of Lower case Characters : 33


**Write a Python function that takes a list and returns a new list with unique elements of the first list.**

    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]


**Write a Python function to multiply all the numbers in a list.**

    Sample List : [1, 2, 3, -4]
    Expected Output : -24


**Write a Python function that checks whether a passed in string is palindrome or not.**


**Write a Python function to check whether a string is pangram or not.**

    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example : "The quick brown fox jumps over the lazy dog"

