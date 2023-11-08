# Class and functions for TicTacToe by Louisa
import random
class Board:
    def __init__(self):
        self._rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __str__(self):
        s = '\n'
        for row in self._rows:
            s = s + '['
            for cell in row:
                if cell == None:
                    s = s + ' '
                else:
                    s = s + cell
            s = s + ']\n'
        return s

    def get(self, x, y):
        return self._rows[x][y]

    def set(self, x, y, value):
        self._rows[x][y] = value
        
    def check(self): # Winner logic for tictactoe
        if self.get(0,0) == self.get(0,1) == self.get(0,2) and self.get(0,0) != " ":
            return(self.get(0,0))
        if self.get(1,0) == self.get(1,1) == self.get(1,2) and self.get(1,0) != " ":
            return(self.get(1,0))
        if self.get(2,0) == self.get(2,1) == self.get(2,2) and self.get(2,0) != " ":
            return(self.get(2,0))
        # Check vertical
        if self.get(0,0) == self.get(1,0) == self.get(2,0) and self.get(0,0) != " ":
            return(self.get(0,0))
        if self.get(0,1) == self.get(1,1) == self.get(2,1) and self.get(0,1) != " ":
            return(self.get(0,1))
        if self.get(0,2) == self.get(1,2) == self.get(2,2) and self.get(0,2) != " ":
            return(self.get(0,2))
        # Check diagnal
        if self.get(0,0) == self.get(1,1) == self.get(2,2) and self.get(0,0) != " ":
            return(self.get(0,0))
        if self.get(2,0) == self.get(1,1) == self.get(0,2) and self.get(2,0) != " ":
            return(self.get(2,0))
        
        return None

    def check_draw(self):
        for row in self._rows:
            for cell in row:
                if cell == None:
                    return False
        
        return True
        

class Game:

    def __init__(self, playerX, playerO):
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO

    def run(self):
        winner = None
        current_player = self._playerX
        while winner == None:
            if current_player == self._playerX:
                print("Player X's turn")
            else:
                print("Player O's turn")
            
            try:
                x,y = current_player.play_move(self._board)
                # playmove
                if current_player == self._playerX:
                    self._board.set(int(x),int(y),"X")
                    current_player = self._playerO # Switch player
                elif current_player == self._playerO:
                    self._board.set(int(x),int(y),"O")
                    current_player = self._playerX # Switch player
            except:
                print("Please try again")
                
            print("\n>>>>>>>>>>>>>>>>>>>>>>>")
            winner = self._board.check()
            if self._board.check_draw():
                winner = "Draw"
            
        print(self._board)
        if winner != "Draw":
            print(f'Player {winner} wins!')
        else:
            print("It's a draw!")

class Human:
    def play_move(self, board):
        print(board)
        try:
            x,y = input("Input x y axis, use space to seperate: ").split()
        except:
            print("Input not recognized")
            return None
        
        # Check if range is in board  
        if int(x) >= 0 and int(x) <= 2 and int(y) >= 0 and int(y) <= 2: 
            if board.get(int(x),int(y))!= None: # already has value
                print("Already has value, please try to place at empty spot")
                return None
            # Update the board.
            return x, y
        else: # Out of range, redo
            print("Input axis out of range")
            return None

class Bot:
    def play_move(self, board):
        print(board)
        while True:
            x = random.randrange(0,3)
            y = random.randrange(0,3)
            if board.get(x,y) == None:
                return x, y