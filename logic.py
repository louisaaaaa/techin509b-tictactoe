# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    # Check horizontal
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != " ":
        return(board[0][0])
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != " ":
        return(board[1][0])
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != " ":
        return(board[2][0])
    # Check vertical
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != " ":
        return(board[0][0])
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != " ":
        return(board[0][1])
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != " ":
        return(board[0][2])
    # Check diagnal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return(board[1][1])
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
        return(board[1][1])
    
    return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O"  # FIXME
