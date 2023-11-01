# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner


# Reminder to check all the tests

# print board function
def print_board(board):
     for line in board:
            print("[", end="")
            for item in line:
                print(item, end="")
            print("]")
            
if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    turn = True # Keep track of whose turn it is
    count = 0 # See if draw
    print("Welcome to Tic-Tac-Toe!")
    while winner == None:
        if count == 9:
            print_board(board)
            print("It's a Draw :D")
            break
        if turn:
            print("X's turn!")
        else:
            print("O's turn!")
        # Show the board to the user.
        print_board(board)
        # Input a move from the player.
        try:
            x,y = input("Input x y axis, use space to seperate: ").split()
        except:
            print("Input error, try again")
            continue
        
        if int(x) >= 0 and int(x) <= 2 and int(y) >= 0 and int(y) <= 2: # check if range is in board   
            if  board[int(x)][int(y)] != " ": # already has value
                print("Already has value, please try to place at empty spot")
                continue
            # Update the board.
            if turn: 
                board[int(x)][int(y)] = 'X'
            else:
                board[int(x)][int(y)] = 'O'
            # Update who's turn it is.
            turn = not turn
            count += 1
            # See if anyone wins
            winner = get_winner(board)
        else: # out of range, redo
            print("Input axis out of range, please try again")
     
    if winner != None:       
        print_board(board)
        print(f'{winner} wins!')
