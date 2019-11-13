'''
Create Tic Tac Toe Game
'''

# game_board = ['E'] * 10

game_board = [
    'E',
    'X','E','E',
    'X','X','E',
    'E','X','X'
]

def display_board(board):
    '''
    Takes in a list and prints out a board.
    '''
    # print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# player1_marker, player2_marker = player_input()
# print(f'Player 1 is {player1_marker}, Player 2 is {player2_marker}')

def place_marker(board, marker, position):
    '''
    Places a marker and updates the gameboard
    '''
    board[position] = marker

# place_marker(game_board, 'X', 3)

def win_check(board, mark):
    '''
    Write a function that takes in a board and mark (X or O) and then checks to see if that mark has won.

    '''
    # ROWS
    row = [mark]*3
    if (game_board[1:4] == row or game_board[4:7] == row or game_board[7:] == row or
            # COLUMNS
            board[1] == board[4] == board[7] == mark or
            board[2] == board[5] == board[8] == mark or
            board[3] == board[6] == board[9] == mark or
            # DIAGONALS
            board[1] == board[5] == board[9] == mark or
            board[3] == board[5] == board[7] == mark):
        return True
    else:
        return False

# display_board(game_board)
# win_check(game_board, 'X')

import random

def choose_first():
    '''
    Write a function that uses the random module to randomly decide which player goes first.
    '''
    return 'Player 1' if random.randint(1,2) == 1 else 'Player 2'

# print(choose_first())

def space_check(board, position):
    '''
    Write a function that returns a boolean indicating whether a space on the board is freely available.
    '''
    return board[position] == 'E'

# print(space_check(game_board, 2))

def full_board_check(board):
    '''
    Write a function that checks if the board is full and returns a boolean value.
    '''
    for position in board[1:]:
        if position == 'E':
            return False
    return True

# print(full_board_check(game_board))

def players_choice(board):
    '''
    Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
    '''
    while True:
        choice = int(input('Select a position from 1-9: '))
        if space_check(board, choice):
            return choice
        else:
            print('Position taken, select again.')

# print(players_choice(game_board))

def replay():
    '''
    Write a function that asks the player if they want to play again and returns a boolean True if thy do want to play again.
    '''
    question = input('Do you want to play again? ').lower()
    # if question == 'y' or question == 'yes':
    #     return True
    # else:
    #     return False
    
    return True if question == 'y' or question == 'yes' else False

# print(replay())

# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to TIC TAC TOE')

while True:
    # PLAY THE GAME

    # Set everything up (board, whos first, choose markers)
    the_board = ['E']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or no? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    # GAMEPLAY

    while game_on:
        
        if turn == 'Player 1':

            # Show the board
            display_board(the_board)

            # Choose a position
            position = players_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            # check if they won
            if win_check(the_board, player1_marker):
                # display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'
        
        else:
            # Show the board
            display_board(the_board)

            # Choose a position
            position = players_choice(the_board)
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'

    # if replay is false then break out of while loop(game)
    if not replay():
        break