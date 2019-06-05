'''
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

'''

def ask():
    while True:
        try:
            a = int(input("Input an integer: "))
            print(f'Thank you, your number squared is: {a**2}')
        except:
            print("An error occured! Please try again!")
            continue
        else:
            break

