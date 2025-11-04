import math

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

# Check winner
def check_winner(board):
    # Rows, Columns, Diagonals
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    if ["X", "X", "X"] in win_states:
        return "X"
    elif ["O", "O", "O"] in win_states:
        return "O"
    return None

# Check if moves are left
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Minimax Algorithm
def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    if winner == "O":
        return 10 - depth
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

# Find best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Main Game Loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe (You = X, AI = O)\n")
    print_board(board)

    for _ in range(9):
        # Human Move
        row, col = map(int, input("Enter row and col (0-2): ").split())
        if board[row][col] != " ":
            print("Invalid Move! Try again.")
            continue
        board[row][col] = "X"
        print_board(board)

        if check_winner(board):
            print("You Win!")
            return

        if not is_moves_left(board):
            print("Draw!")
            return

        # AI Move
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = "O"
        print("AI Played:")
        print_board(board)

        if check_winner(board):
            print("AI Wins!")
            return

    print("Draw!")

play_game()