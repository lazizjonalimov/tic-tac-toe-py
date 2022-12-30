
def move_validate(board):
    user_move = ""
    is_incorrect = True
    while is_incorrect:
        print()
        print("Please give the right choice, otherwise we cannot process further!".upper())
        user_move = input("Which cell would you like to choose (From top left [1] To bottom right [9]): ")
        if user_move in "123456789" and 1 <= int(user_move) <= 9 and not(board[int(user_move) - 1] == "O" or board[int(user_move) - 1] == "X"):
            break
        else:
            is_incorrect = True

    return int(user_move)