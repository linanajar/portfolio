# Tic Tac Toe


# dictionaries to mapp the columns and rows with their corresponding index
COLUMNS = {'a': 0, 'b': 1, 'c': 2}
ROWS = {'1': 0, '2': 1, '3': 2}

player_1_symbol = 'O'
player_2_symbol = 'X'


def print_game_instructions():
    '''
    Prints the game instructions and rules for Tic Tac Toe.
    '''
    print("Hi and welcome to tic tac toe!\n"
          "This is how the game works:\n"
          "Players take turns placing their symbol (X or O) in an empty square.\n"
          "The first player to get three of their symbols in a row (horizontally,\n"
          "vertically, or diagonally) wins. If all squares\n"
          "are filled and no one has three in a row, the game is a draw.\n"
          "You can exit the game at any point by typing 'exit' in the terminal.\n"
          "The first player plays an O and the second player plays with an X.\n"
          "After each round the game update is shown. Have fun!\n"
          "This is the game board:")


def ask_to_continue():
    '''
    Checks whether the user wants to continue the game or not.
    If the user wants to continue, the game goes on and
    otherwise the game is exited.

    Returns:
        bool:
            True: player wants to continue
            False: player wants to end game
    '''
    print("Would you like to play another game? Y/N")

    continue_game = input().strip().lower()
    if "exit" in continue_game:
        if confirm_exit():
            return False
        else:
            return ask_to_continue()
    if continue_game.startswith('y'):
        return True
    elif continue_game.startswith('n'):
        return False
    else:
        print("I did not catch that, can you type 'yes' or 'no'?")
        return ask_to_continue()


def confirm_exit():
    '''
    When the user types 'exit' in the terminal this
    function confirms the exit and exits the game.

    Returns:
        bool:
            True: player wants to exit game
            False: player wants to continue game (false exit)
    '''
    print("Are you sure you want to exit the game?")
    exit_game = input().strip().lower()
    if exit_game.startswith('y'):
        print('So sad to see you go, thanks for playing!')
        return True
    else:
        print("Phew, that's good to hear, let's continue!")
        return False


def get_valid_move_input():
    '''
    Gets user input on where to make a move.

    Returns:
        str or None:
            None: player wants to exit game
            Move: player's move (str)
    '''
    while True:
        move = input("Where would you like to add your move? ").strip().lower()
        if 'exit' in move:
            if confirm_exit():
                return None

        else:
            return move


def create_board():
    '''
    Creates the playing board.

    Returns:
        list: the game board as a 3x3 list of lists

    '''
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    display_board(board)
    return board


def play_game_round(player_1, player_2, board):
    '''
    Plays a full round of Tic Tac Toe between two players.

    Args:
        player_1 (str): symbol for player_1 (currently 'O')
        player_2 (str): symbol for player_1 (currently 'X')
        board (list): the current game board

    Returns:
        str or None:
            'exit': the user wants to exit the game
            None: game continues
    '''
    current_player = player_1

    while True:
        print(f"It's {current_player}'s turn.")
        result = handle_player_move(current_player, board)
        if result == 'exit':
            return 'exit'
        else:
            if is_winner(current_player, board):
                print(f"The game is over. The winner is: {current_player} !")
                break
            elif is_board_full(board):
                print("The game is over. It's a tie.")
                break
            else:
                if current_player == player_1:
                    current_player = player_2
                else:
                    current_player = player_1


def validate_move_input(answer):
    '''
    Validates the user input for the move.
    Checks if it's in the correct column and row range.
    Args:
        answer (str): user input for move on the board (e.g. a3)

    Returns:
        tuple or bool:
            (row, column) (tuple): for correct user input
            False:  incorrect user input
    '''
    if len(answer) == 2:
        if answer[0] in COLUMNS:
            if answer[1] in ROWS:
                column = COLUMNS[answer[0]]
                row = ROWS[answer[1]]
                return (row, column)
            else:
                print("The row is out of range. Try again.")
                return False

        else:
            print("The column is out of range. Try again.")
            return False

    elif len(answer) > 2:
        print("Input is too long. Try again.")
        return False
    else:
        print("Check if you put in the correct column and row, it seems that something is missing!"
              "Please put in your answer as a letter+number e.g. 'A1', 'B3' etc."
              "Try again.")
        return False


def handle_player_move(current_player, board):
    '''
    Handles one player's move. It prompts the user for input, validates it
    and then updates the board with the move.

    Args:
        current_player (str): symbol for current player
        board (list): the current game board

    Returns:
        str or None:
            'exit': the user wants to exit the game
            None: continue as normal

    '''
    while True:
        answer = get_valid_move_input()
        if answer is None:
            return 'exit'
        else:
            result = validate_move_input(answer)
            if result is False:
                continue
            else:
                (row, column) = result
                if board[row][column] == '':
                    board[row][column] = current_player
                    display_board(board)
                    break
                else:
                    print("This spot is already taken, choose another one!")


def display_board(board):
    '''
    Prints the current board and adds column labels and row numbers.

    Args:
        board (list): the current game board
    '''
    print("  a  b  c")
    for i, row in enumerate(board):
        row_number = str(i + 1)
        print(f"{row_number}  {' | '.join(cell or ' ' for cell in row)}")
        if i < 2:
            print("  ---+---+---")


def is_winner(current_player, board):
    '''
    Checks whether current_player has won the game.

    Args:
        current_player (str): symbol of current player
        board (list): the current game board

    Returns:
        bool:
            True: current player has won
            False: current player did not win
    '''
    if ((board[0][0] == board[0][1] == board[0][2] != '') or
        (board[1][0] == board[1][1] == board[1][2] != '') or
        (board[2][0] == board[2][1] == board[2][2] != '') or
        (board[0][0] == board[1][0] == board[2][0] != '') or
        (board[0][1] == board[1][1] == board[2][1] != '') or
        (board[0][2] == board[1][2] == board[2][2] != '') or
        (board[0][0] == board[1][1] == board[2][2] != '') or
            (board[0][2] == board[1][1] == board[2][0] != '')):
        return True
    return False


def is_board_full(board):
    '''
    Checks whether the board is full for a tie.

    Args:
        board (list): the current game board

    Returns:
        bool:
            True: it's a tie
            False: not a tie
    '''
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                return False
    return True


def main():
    '''
    Tic Tac Toe game initialization
    '''
    # first show the players the player board and game instructions
    print_game_instructions()
    player_1 = player_1_symbol
    player_2 = player_2_symbol
    # game play continues until the game is exited by the players
    while True:
        board = create_board()
        result = play_game_round(player_1, player_2, board)
        if result == 'exit':
            break
        # ask the players if they want to continue
        keep_playing = ask_to_continue()
        if keep_playing:
            continue
        else:
            break


if __name__ == "__main__":
    main()
