import math

BOARD = [2] * 10  # 1-indexed for consistency
WIN_LINES = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]


def display_board():
    for i in range(1, 10):
        if BOARD[i] == 2:
            symbol = '_'
        elif BOARD[i] == 3:
            symbol = 'X'
        else:
            symbol = 'O'
        print(symbol, end=" ")
        if i % 3 == 0:
            print()
    print()


def make2():
    if BOARD[5] == 2:
        return 5
    sides = [2, 4, 6, 8]
    for pos in sides:
        if BOARD[pos] == 2:
            return pos
    return 0


def posswin(player):
    target_product = 18 if player == 3 else 50
    for line in WIN_LINES:
        p1, p2, p3 = line
        prod = BOARD[p1] * BOARD[p2] * BOARD[p3]
        if prod == target_product:
            if BOARD[p1] == 2:
                return p1
            if BOARD[p2] == 2:
                return p2
            if BOARD[p3] == 2:
                return p3
    return 0


def go(position, player):
    if 1 <= position <= 9 and BOARD[position] == 2:
        BOARD[position] = player


def check_win(player):
    product_target = 27 if player == 3 else 125
    for line in WIN_LINES:
        p1, p2, p3 = line
        prod = BOARD[p1] * BOARD[p2] * BOARD[p3]
        if prod == product_target:
            return True
    return False


def is_draw():
    return all(BOARD[i] != 2 for i in range(1, 10))


def minimax(is_maximizing):
    if check_win(3):
        return +1
    if check_win(5):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(1, 10):
            if BOARD[i] == 2:
                BOARD[i] = 3
                best = max(best, minimax(False))
                BOARD[i] = 2
        return best
    else:
        best = math.inf
        for i in range(1, 10):
            if BOARD[i] == 2:
                BOARD[i] = 5
                best = min(best, minimax(True))
                BOARD[i] = 2
        return best


def generate_move():
    best_val = -math.inf
    best_move = -1
    for i in range(1, 10):
        if BOARD[i] == 2:
            BOARD[i] = 3
            move_val = minimax(False)
            BOARD[i] = 2
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move


def main():
    global BOARD
    BOARD = [2] * 10

    print("You are O. Computer is X.\n")
    display_board()

    while True:
        # Human move
        while True:
            try:
                human_move = int(input("Enter your move (1-9): "))
                if 1 <= human_move <= 9 and BOARD[human_move] == 2:
                    go(human_move, 5)
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

        display_board()

        if check_win(5):
            print("You won!")
            break
        if is_draw():
            print("Game is a draw!")
            break

        # Computer move
        comp_move = generate_move()
        print(f"Computer moves at position: {comp_move}")
        go(comp_move, 3)
        display_board()

        if check_win(3):
            print("Computer won!")
            break
        if is_draw():
            print("Game is a draw!")
            break

    print("Game Over!")


if __name__ == "__main__":
    main()