from tictactoe import Game, Human, Bot
import pandas as pd

# Game play for tictactoe
start_game = False
print("Welcome to TicTacToe presented by Louisa:)")
print("Do you want to do single player or two players?")
game_mode = input("Please type in one or two to indicate your choice: ")
while start_game == False:
    if game_mode == "one":
        print("You have chosen single player:")
        # xname = input("Please enter your name: ")
        game = Game(Human(), Bot(), None, None)
        start_game = True
       
    elif game_mode == "two":
        print("You have chosen two players:")
        xname = input("Please enter playerX's name: ")
        yname = input("Please enter playerY's name: ")
        game = Game(Human(), Human(), xname, yname)
        start_game = True
       
    else:
        print("Input not recognizable, please try again")
        game_mode = input("Please type in one or two to indicate your choice: ")

game.run()