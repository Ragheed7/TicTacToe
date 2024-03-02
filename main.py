from random import *

board = [" " for x in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def players():
    num_of_players = int(input('Do you want to play against the Computer (press 1) or 1 vs 1 (press 2)? '))
    if num_of_players == 1 or num_of_players == 2:
        print('Number of players:', num_of_players)
        return num_of_players
    else:
        print('Unsupprted value!')


def X_O(num_of_players):
    if num_of_players == 1:
        p1_icon = input('Choose your icon X or O: ').upper()
        if p1_icon == 'X':
            p2_icon = 'O'
            print('Player 1: X \nPlayer 2: O')

        elif p1_icon == 'O':
            p2_icon = 'X'
            print('Player 1: O \nPlayer 2: X')
        else:
            print('sorry!')

    elif num_of_players == 2:
        p1_icon = input('Choose icon X or O for player 1: ').upper()
        if p1_icon == 'X':
            p2_icon = 'O'
            print('Player 1: X \nPlayer 2: O')
        elif p1_icon == 'O':
            p2_icon = 'X'
            print('Player 1: O \nPlayer 2: X')
        else:
            print('Sorry!')
    return p1_icon, p2_icon


def turn(num_of_players):
    if num_of_players == 1:
        first_turn = input('Do you want to start first? (press Y/N)').upper()
        if first_turn == 'Y':
            print('Be Ready! You will play first')
            return True
        elif first_turn == 'N':
            print('Computer will play first')
            return False
        else:
            print('Oops!')

    elif num_of_players == 2:
        first_turn = input('Player one starts (press Y/N)? ').upper()
        if first_turn == 'Y':
            print('Be Ready! Player One will play first')
            return True
        elif first_turn == 'N':
            print('Be Ready! Player Two will play first')
            return False
        else:
            print('Oops!')
    else:
        print('Sorry, something went wrong!')

def is_available(icon,choice):
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print("\nThat space is already taken!")


def player_move(icon, first_turn):
    while True:
    #if num_of_players == 2 and first_turn == True:

        print("Your turn player {}".format(icon))
        choice = int(input("Enter your move (1-9): ").strip())

        if choice > 9 or choice < 1:
            print("\nPlease enter a value between (1-9).")

        # if space is used
        elif board[choice - 1] == "X" or board[choice - 1] == "O":
            print("That space is already taken!\n")

        # fill space
        else:
            board[choice - 1] = icon

def computer_move(icon):
    print("Computer's turn:")
    print_board()

    while True:
        # Computer's random choice
        choice = random.randint(1, 9)

        # If slot is already used
        if board[choice - 1] == "X" or board[choice - 1] == "O":
            continue

        # If slot available
        else:
            # Wait for user to see the board
            input("Press enter to continue.")

            # Fill slot
            board[choice - 1] = icon

'''
#elif num_of_players == 2 and first_turn == False:
        print("Your turn player {}".format(icon))
        choice = int(input("Enter your move (1-9): ").strip())
        if board[choice - 1] == " ":
            board[choice - 1] = icon
        else:
            print()
            print("That space is already taken!")

    #elif num_of_players == 1 and first_turn == True:
        print("Your turn player {}".format(icon))
        choice = int(input("Enter your move (1-9): ").strip())
        if board[choice - 1] == " ":
            board[choice - 1] = icon

    #elif num_of_players == 1 and first_turn == False:
        print("Computer turn {}".format(icon))
        choice = randint(1, 9)
        if board[choice - 1] == " ":
            board[choice - 1] = icon

'''



def is_win(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
            (board[3] == icon and board[4] == icon and board[5] == icon) or \
            (board[6] == icon and board[7] == icon and board[8] == icon) or \
            (board[0] == icon and board[3] == icon and board[6] == icon) or \
            (board[1] == icon and board[4] == icon and board[7] == icon) or \
            (board[2] == icon and board[5] == icon and board[8] == icon) or \
            (board[0] == icon and board[4] == icon and board[8] == icon) or \
            (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_full():
    if " " not in board:
        return True
    else:
        return False


def play_again():
    play = input('Do you want to play again? (Y/N): ').upper()
    if play == 'N':
        return False


def clear_board():
    global board
    board = [" " for x in range(9)]


def startGame():
    while True:

        clear_board()
        players_number = players()

        if players_number == 1:
            icon1 = None
            icon2 = None
            while icon1 is None:
                icon1, icon2 = X_O(players_number)
            while True:
                is_first_turn = turn(players_number)
                print_board()
                if player_move(icon1, is_first_turn):
                    print_board()
                    if is_win(icon1):
                        print(icon1, 'wins! Congratulations!')
                        break
                    elif is_full():
                        print("It's a draw!")
                        break
                    break


                if player_move(icon2, is_first_turn):
                    print_board()
                    if is_win(icon2):
                        print_board()
                        print(icon2, "wins! Congratulations!")
                        break
                    elif is_full():
                        print("It's a draw!")
                        break
                    break


        elif players_number == 2:
            is_first_turn = turn(players_number)
            icon1 = None
            computer = None
            while icon1 is None:
                icon1, computer = X_O(players_number)
            if is_first_turn == False:
                while True:
                    if computer_move(computer):
                        print_board()
                        computer_move(computer)
                        print_board()
                        if is_win(computer):
                            print(computer, 'wins! Congratulations!')
                            break
                        elif is_full():
                            print("It's a draw!")
                            break
                        break
            else:
                while True:
                    if player_move(icon1,is_first_turn):
                        player_move(icon1,is_first_turn)
                        print_board()
                        player_move(icon1,is_first_turn)
                        print_board()
                        if is_win(icon1):
                            print(icon1, 'wins! Congratulations!')
                            break
                        elif is_full():
                            print("It's a draw!")
                            break
                        break


            play = play_again()
            if play == False:
                break


startGame()
