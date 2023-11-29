# Class and functions for TicTacToe by Louisa
import random
import pandas as pd

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

    def __init__(self, playerX, playerO, playerX_name, playerY_name):
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO
        self._playerX_name = playerX_name
        self._playerY_name = playerY_name
        

    def run(self):
        winner = None
        current_player = self._playerX
        first_step = False
        first_x = 0
        first_y = 0
        while winner == None:
            if current_player == self._playerX:
                print("Player X's turn")
            else:
                print("Player O's turn")
            
            try:
                x,y = current_player.play_move(self._board)
                if first_step == False:
                    first_x = x
                    first_y = y
                    first_step = True
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
            if self._board.check_draw():
                winner = "Draw"
            winner = self._board.check()
            
            
        print(self._board)
        try:
            df = pd.read_csv("database.csv")
            df1 = pd.read_csv("database_win_loc.csv")
        except FileNotFoundError:
            # If the file doesn't exist, create an empty DataFrame with the required columns
            df = pd.DataFrame(columns=['Name', 'Win', 'Lose', 'Draw'])
            
        if winner != "Draw":
            print(f'Player {winner} wins!')
            if winner == 'X': 
                df = update_win(df, self._playerX_name)
                df = update_lose(df, self._playerY_name)
                df.to_csv("database.csv", index=False)
                # Log for linear regression
                new_row = pd.DataFrame({'X': [first_x], 'Y': [first_y], 'Result': ['Win']})
                df1 = pd.concat([df1, new_row])
                df1.to_csv("database_win_loc.csv", index=False)
                
            elif winner == 'Y': 
                df = update_win(df, self._playerY_name)
                df = update_lose(df, self._playerX_name)
                df.to_csv("database.csv", index=False)
               # Log for linear regression
                new_row = pd.DataFrame({'X': [first_x], 'Y': [first_y], 'Result': ['Lose']})
                df1 = pd.concat([df1, new_row])
                df1.to_csv("database_win_loc.csv", index=False)
                
        else:
            print("It's a draw!")
            df = update_draw(df, self._playerY_name)
            df = update_draw(df, self._playerX_name)
            df.to_csv("database.csv", index=False)
            
            # Log for linear regression
            new_row = pd.DataFrame({'X': [first_x], 'Y': [first_y], 'Result': ['Draw']})
            df1 = pd.concat([df1, new_row])
            df1.to_csv("database_win_loc.csv", index=False)

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
            
# Write to csv
def update_win(df, name):
    # Check if the name exists in the DataFrame
    if name in df['Name'].values:
        # Update the 'Win' column for the specified name
        df.loc[df['Name'] == name, 'Win'] += 1
    else:
        # If the name doesn't exist, add a new row with the provided information
        new_row = pd.DataFrame({'Name': [name], 'Win': [1], 'Lose': [0], 'Draw': [0]})
        df = pd.concat([df, new_row], ignore_index=True)
    return df

def update_lose(df, name):
    # Check if the name exists in the DataFrame
    if name in df['Name'].values:
        df.loc[df['Name'] == name, 'Lose'] += 1
    else:
        new_row = pd.DataFrame({'Name': [name], 'Win': [0], 'Lose': [1], 'Draw': [0]})
        df = pd.concat([df, new_row], ignore_index=True)
    return df

def update_draw(df, name):
    # Check if the name exists in the DataFrame
    if name in df['Name'].values:
        df.loc[df['Name'] == name, 'Draw'] += 1
    else:
        new_row = pd.DataFrame({'Name': [name], 'Win': [0], 'Lose': [0], 'Draw': [1]})
        df = pd.concat([df, new_row], ignore_index=True)
    return df