import random

# Print Board
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

# Check Winner
def check_winner(board):
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

# AI Rule-Based Strategy
def ai_move(board):
    # 1. Win if possible
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_winner(board) == "O":
                    return
                board[i][j] = " "

    # 2. Block opponent
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_winner(board) == "X":
                    board[i][j] = "O"
                    return
                board[i][j] = " "

    # 3. Take center
    if board[1][1] == " ":
        board[1][1] = "O"
        return

    # 4. Take corners
    for (i, j) in [(0,0), (0,2), (2,0), (2,2)]:
        if board[i][j] == " ":
            board[i][j] = "O"
            return

    # 5. Take sides
    for (i, j) in [(0,1), (1,0), (1,2), (2,1)]:
        if board[i][j] == " ":
            board[i][j] = "O"
            return

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

        if all(" " not in row for row in board):
            print("Draw!")
            return

        # AI Move
        ai_move(board)
        print("AI Played:")
        print_board(board)

        if check_winner(board):
            print("AI Wins!")
            return

    print("Draw!")

play_game()