
def validate():
    user_choice = ""
    is_incorrect = True
    while is_incorrect:
        print()
        print("Please give the right choice, otherwise we cannot process further!".upper())
        user_choice = input("Which figure would you like to choose (X or O): ")
        if user_choice.upper() == "X":
            break
        elif user_choice.upper() == "O":
            break
        else:
            is_incorrect = True

    return user_choice.upper()
