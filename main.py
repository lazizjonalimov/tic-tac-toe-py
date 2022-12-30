"""Things that we need for the project"""
import random, displayBoard, choiceVal, moveVal, checking
# after creating version with the computer as a second player create 2-player version


# play game
def main():
    keep_going = True
    while keep_going:
        moves_number = 0
        not_completed = True
        computer_choice = ""
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]

        print("Welcome to the game of Tic Tac Toe!")
        print()
        print("Here is our board!")
        displayBoard.display_board(board)
        print()
        user_choice = input("Which figure would you like to choose (X or O): ").upper()
        if not(user_choice.upper() == "X" or user_choice.upper() == "O"):
            user_choice = choiceVal.validate()

        if user_choice == "X":
            computer_choice = "O"
        else:
            computer_choice = "X"
        print()
        print("The user's choice: ", user_choice)
        print("The computer's choice: ", computer_choice)
        print()
        while not_completed:
            user_move = input("Which cell would you like to choose (From top left [1] To bottom right [9]): ")
            moves_number += 1
            if not(user_move in "123456789" and 1 <= int(user_move) <= 9) or board[int(user_move) - 1] == "O" or \
                    board[int(user_move) - 1] == "X":
                user_move = moveVal.move_validate(board)
            user_move = int(user_move)
            board[user_move - 1] = user_choice

            computer_move = random.randint(1, 9)

            if "-" in board:
                print()
                while computer_move == user_move or board[computer_move - 1] == "O" or board[computer_move - 1] == "X":
                    computer_move = random.randint(1, 9)
                board[computer_move - 1] = computer_choice
            print(f"User's choice: {user_move}")
            print(f"Computer's choice: {computer_move}")
            print()
            print("Here is our updated board: ")
            # board[computer_move - 1] = computer_choice
            displayBoard.display_board(board)
            print()
            if moves_number >= 1:
                """call the functions that check winners and make the nnot_completed False"""
                by_rows = checking.check_row(board)
                by_columns = checking.check_column(board)
                by_diagonals = checking.check_diagonals(board)
                print(by_rows)
                print(by_columns)
                print(by_diagonals)
                print()
                if by_columns == ['No Winner - Column'] and by_rows == ["No Winner - Row"] and \
                        by_diagonals == ['No Winner - Diagonal']:
                    """HERE we NEED TO ADD THE THING SO THAT IT MOVES BACK AND ASKS FOR A MOVE NUMBER"""

                    if not ("-" in board):
                        print("Unfortunately, both of you could not win the game! - It's Tie!!!!")
                        not_completed = False
                    else:
                        not_completed = True

                elif len(by_rows) == 2 and by_rows[1] in "XO":
                    if user_choice.upper() == by_rows[1]:
                        print("Congrats! - You have won the game!!!")
                        print(f'By {by_rows[0]}')
                        not_completed = False
                    elif computer_choice.upper() == by_rows[1]:
                        print("Sorry! - You have unfortunately lost the game to the robot!!!")
                        print(f'By {by_rows[0]}')
                        not_completed = False
                elif len(by_columns) == 2 and by_columns[1] in "XO":
                    if user_choice.upper() == by_columns[1]:
                        print("Congrats! - You have won the game!!!")
                        print(f'By {by_columns[0]}')
                        not_completed = False
                    elif computer_choice.upper() == by_columns[1]:
                        print("Sorry! - You have unfortunately lost the game to the robot!!!")
                        print(f'By {by_columns[0]}')
                        not_completed = False
                elif len(by_diagonals) == 2 and by_diagonals[1] in "XO":
                    if user_choice.upper() == by_diagonals[1]:
                        print("Congrats! - You have won the game!!!")
                        print(f'By {by_diagonals[0]}')
                        not_completed = False
                    elif computer_choice.upper() == by_diagonals[1]:
                        print("Sorry! - You have unfortunately lost the game to the robot!!!")
                        print(f'By {by_diagonals[0]}')
                        not_completed = False
        keep_gaming = input("Do you wanna continue playing the game (Yes/No): ").upper()
        if keep_gaming == "YES" or keep_gaming == "Y":
            keep_going = True
        elif keep_gaming == "NO" or keep_gaming == "N":
            print("----------------------- Game is Over ------------------------")
            keep_going = False


main()
