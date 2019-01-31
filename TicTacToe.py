from IPython.display import clear_output
import random

def display_board(board):
    for i in range(0,3):
        print('      |      |      ')
        print('  {}   |  {}   |  {}  '.format(board[3*i+1], board[3*i+2], board[3*i+3]))
        print('      |      |      ')
        if(i != 2):
            print('--------------------')

test_board = ['#','X','X','X','O',' ','O','X','O','X']

def isWon(board, current):
    #check the rows
    for i in range(0,3):
        if board[3*i+1] == board[3*i+2] == board[3*i+3] != ' ':
            display_board(board)
            print('Player {} Wins!!!!'.format(current))
            return True
    #check the columns
    for i in range(0,3):
        if board[0+i] == board[3+i] == board[6+i] != ' ':
            display_board(board)
            print('Player {} Wins!!!!'.format(current))
            return True
    #check the diagonals
    if board[3] == board[5] == board[7] != ' ':
            display_board(board)
            print('Player {} Wins!!!!'.format(current))
            return True
    if board[1] == board[5] == board[9] != ' ':
            display_board(board)
            print('Player {} Wins!!!!'.format(current))
            return True
    return False

def player_input():
    while not(isWon()):
        pass

def full_board_check(board):
    for i in board:
        if i == ' ':
            return False
    display_board(board)
    print("It's a tie :/")
    return True

def place_marker(board, player,position):
    board[position] = player

def replay():
    response = input("Do you want to replay? Say yes or no\n")
    if(response == 'yes'):
        run_game()
    else:
        pass
                     

def run_game():
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player2 = 'X'
    player1 = input("Please pick a marker 'X' or 'O'. You will be player 1'\n")
    while not(player1 == 'X' or player1 == 'O'):
        print("That was an invalid character. Please choose correctly")
        player1 = input("Please pick a marker 'X' or 'O'. You will be player 1'")
    if(player1 == 'X'):
        player2 = 'O'
    current = 'None'
    goes_next = random.randint(1,2)
    if (goes_next == 1):
        current = player1
    else:
        current = player2
    while(not(full_board_check(board)) and not(isWon(board, goes_next))):
        display_board(board)
        position = input("Please pick a number from 1 to 9 player {}".format(goes_next))
        while not(position in ['1','2','3','4','5','6','7','8','9']):
            print("That was an invalid character. Please choose correctly")
            position = input("Please pick a number from 1 to 9 player {}".format(goes_next))
        position = int(position)
        place_marker(board, current, position)
        if (current == player1):
            current = player2
            goes_next = 2
        else:
            current = player1
            goes_next = 1
    replay()

run_game()

