from tictactoe import Game, Human, Bot

# Game play for tictactoe
start_game = False
print("Welcome to TicTacToe presented by Louisa:)")
print("Do you want to do single player or two players?")
game_mode = input("Please type in one or two to indicate your choice: ")
while start_game == False:
    if game_mode == "one":
        print("You have chosen single player:")
        game = Game(Human(), Bot())
        start_game = True
    elif game_mode == "two":
        print("You have chosen two players:")
        game = Game(Human(), Human())
        start_game = True
    else:
        print("Input not recognizable, please try again")
        game_mode = input("Please type in one or two to indicate your choice: ")

game.run()