

def check_row(board):
    """Check winner by row"""
    winner = []
    if board[0] == board[1] == board[2] and (board[0] == board[1] == board[2] != "-"):
        winner.append("First Row")
        if board[0] == "O":
            winner.append("O")
        elif board[0] == "X":
            winner.append("X")

    elif board[3] == board[4] == board[5] and (board[3] == board[4] == board[5] != "-"):
        winner.append("Second Row")
        if board[3] == "O":
            winner.append("O")
        elif board[3] == "X":
            winner.append("X")

    elif board[6] == board[7] == board[8] and (board[6] == board[7] == board[8] != "-"):
        winner.append("Third Row")
        if board[6] == "O":
            winner.append("O")
        elif board[6] == "X":
            winner.append("X")
    else:
        winner.append("No Winner - Row")
    return winner


def check_column(board):
    """Check the winner by column"""
    winner = []

    if board[0] == board[3] == board[6] and (board[0] == board[3] == board[6] != "-"):
        winner.append("First Column")

        if board[0] == "O":
            winner.append("O")
        elif board[0] == "X":
            winner.append("X")

    elif board[1] == board[4] == board[7] and (board[1] == board[4] == board[7] != "-"):

        winner.append("Second Column")

        if board[1] == "O":
            winner.append("O")
        elif board[1] == "X":
            winner.append("X")
    elif board[2] == board[5] == board[8] and (board[2] == board[5] == board[8] != "-"):

        winner.append("Third Column")

        if board[2] == "O":
            winner.append("O")
        elif board[2] == "X":
            winner.append("X")
    else:
        winner.append("No Winner - Column")
    return winner


def check_diagonals(board):
    """Check the winner by diagonals"""
    winner = []
    if board[0] == board[4] == board[8] and (board[0] == board[4] == board[8] != "-"):
        winner.append("First Diagonal")

        if board[0] == "O":
            winner.append("O")
        elif board[0] == "X":
            winner.append("X")
    elif board[2] == board[4] == board[6] and (board[0] == board[4] == board[8] != "-"):
        winner.append("Second Diagonal")
        if board[2] == "O":
            winner.append("O")
        elif board[2] == "X":
            winner.append("X")
    else:
        winner.append("No Winner - Diagonal")
    return winner
