'''
Create a Tic Tac Toe game.

Here are the requirements:

    2 players should be able to play the game (both sitting at the same computer)
    The board should be printed out every time a player makes a move
    You should be able to accept input of the player position and then place a symbol on the board

'''

num = []

def welcome_note():
    while True:
        global num
        # print(num)
        num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # print(num)
        print('Welcome to Tic Tac Toe Game!\n')
        dummy_map()
        player_option()
        play = input("\nDo you want to play again? Type Yes or No: ")
        if play == 'Yes':
            continue
        else:
            break

def dummy_map():
    print(' X | O | X ')
    print('-----------')
    print(' O | X | O ')
    print('-----------')
    print(' X | O | X ')

def game_map(num):
    print("\n")
    print(f' {num[1]} | {num[2]} | {num[3]} ')
    print('-----------')
    print(f' {num[4]} | {num[5]} | {num[6]} ')
    print('-----------')
    print(f' {num[7]} | {num[8]} | {num[9]} ')

def player_option():
    count = 1
    # num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        option1 = input(f"\nChoose what you want to be 'X' or 'O'? ")
        if option1 == 'X' or option1 == 'O':
            break
        else:
            print("\nOops!  That was neither X nor O.  Try again...\n")
            continue
    if option1 == 'X':
        option2 = 'O'
    else:
        option2 = 'X'
    game_map(num)
    mark = 0
    while count < 10:
        if count in (1, 3, 5, 7, 9):
            try:
                mark = int(input(f"\n\nPlayer1 -> Choose a number for {option1} : "))
            except:
                print("\nOops!  That was no valid number.  Try again...")
                continue
            if mark <= 0 or mark >= 10:
                print(f"\nThere is no {mark} position on the board, try between 1 to 9 ")
                continue
            if num[mark] == 'X' or num[mark] == 'O':
                print("\nThis position is already filled, Try another position")
                continue
            check = marker(count, mark, num, option1)
            count += 1
            if check is None:
                continue
            else:
                print(f'\n{check}')
                break
        if count in (2, 4, 6, 8):
            try:
                mark = int(input(f"\n\nPlayer2 -> Choose a number for {option2} : "))
            except:
                print("\nOops!  That was no valid number.  Try again...")
                continue
            if mark <= 0 or mark >= 10:
                print(f"\nThere is no {mark} position on the board, try between 1 to 9 ")
                continue
            if num[mark] == 'X' or num[mark] == 'O':
                print("\nThis position is already filled, Try another position")
                continue
            check = marker(count, mark, num, option2)
            count += 1
            if check is None:
                continue
            else:
                print(f'\n{check}')
                break

def marker(count, mark, num, option):
    if mark in num:
        num[mark] = option
        # for i in range(0,50):
          # print("\n")
        print("\n"*40)
        game_map(num)
        if count >= 5:
            a = win_or_loose(count, num)
            return a

def win_or_loose(count, num):
    win_pos = [(1, 2, 3), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 5, 7), (3, 6, 9),
               (4, 5, 6), (7, 8, 9)]
    if count < 10:
        for elem in win_pos:
            b = elem
            if num[b[0]] == num[b[1]] == num[b[2]] == 'X':
                out = f'{num[b[0]]} Wins'
                return out
            elif num[b[0]] == num[b[1]] == num[b[2]] == 'O':
                out = f'{num[b[0]]} Wins'
                return out
    if count >= 9:
        return "It's a draw"

welcome_note()
