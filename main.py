# Tic Tac Toe game
separator = "========================================"

print ("Welcome to Tic Tac Toe"
       "\n========================================"
       "\nGAME RULES:"
       "\nEach player can place one mark (or stone) "    
       "\nper turn on the 3x3 grid. The WINNER is "
       "\nwho succeeds in placing three of their "
       "\nmarks in a:"
       "\n* horizontal,"
       "\n* vertical or"
       "\n* diagonal row"""
       "\n========================================"
       "\nLet's start the game")

def print_board(board):
    print("+---+---+---+")
    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    print("+---+---+---+")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    print("+---+---+---+")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    print("+---+---+---+")

def get_move(player):
    move = input(f"Player {player}, please enter your move (1-9): ")
    print (separator)
    return int(move) - 1

def is_valid_move(move, board):
    row = move // 3
    col = move % 3
    return board[row][col] == " "

def make_move(move, player, board):
    row = move // 3
    col = move % 3
    board[row][col] = player

def is_win(player, board):
    for i in range(3):
        # check rows
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        # check columns
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    print_board(board)
    while True:
        move = get_move(player)
        if not is_valid_move(move, board):
            print("Invalid move, please try again")
            continue
        make_move(move, player, board)
        print_board(board)
        if is_win(player, board):
            print(f"Congratulations, player {player} won!")
            break
        if is_tie(board):
            print("It's a tie!")
            break
        player = "O" if player == "X" else "X"

play_game()
