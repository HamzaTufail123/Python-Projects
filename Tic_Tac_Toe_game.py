board = ["-"] * 9
game_on = True
current_player = "X"


def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2] + "      1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "      4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "      7 | 8 | 9")
    print()


def players():
    global current_player
    while True:
        p1 = input("Player 1, choose X or O: ").upper()
        if p1 in ["X", "O"]:
            current_player = p1
            break
        else:
            print("Invalid input. Please choose X or O.")


def player_position():
    global current_player
    while True:
        position = input(f"{current_player}'s Turn - choose position (1-9): ")
        if position in [str(i) for i in range(1, 10)]:
            position = int(position) - 1
            if board[position] == "-":
                board[position] = current_player
                break
            else:
                print("That position is already taken.")
        else:
            print("Invalid input. Please choose a number from 1 to 9.")


def check_winner():
    global game_on
    win_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != "-":
            display_board()
            print(f"Congratulations! Player {board[pattern[0]]} wins!")
            game_on = False
            return

    if "-" not in board:
        display_board()
        print("It's a tie.")
        game_on = False


def flip_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"


def play_game():
    global board, game_on, current_player
    board = ["-"] * 9
    game_on = True
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    display_board()
    players()

    while game_on:
        display_board()
        player_position()
        check_winner()
        if game_on:
            flip_player()


play_game()
