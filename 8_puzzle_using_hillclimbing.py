import copy

class Puzzle:
    def __init__(self, board, zero_row, zero_col, heuristic=0):
        self.board = board
        self.zero_row = zero_row
        self.zero_col = zero_col
        self.heuristic = heuristic

    def calculate_heuristic(self, goal):
        dist = 0
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                if val != 0:
                    for x in range(3):
                        for y in range(3):
                            if goal[x][y] == val:
                                dist += abs(i - x) + abs(j - y)
        return dist

    def get_neighbors(self):
        neighbors = []
        moves = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

        for dr, dc in moves:
            new_r, new_c = self.zero_row + dr, self.zero_col + dc
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                new_board = copy.deepcopy(self.board)
                new_board[self.zero_row][self.zero_col], new_board[new_r][new_c] = new_board[new_r][new_c], new_board[self.zero_row][self.zero_col]
                neighbors.append(Puzzle(new_board, new_r, new_c))
        return neighbors

    def is_goal(self, goal):
        return self.board == goal


def hill_climbing(start, goal):
    start.heuristic = start.calculate_heuristic(goal)

    while True:
        if start.is_goal(goal):
            return start

        neighbors = start.get_neighbors()
        next_state = start
        min_heuristic = start.heuristic

        for n in neighbors:
            n.heuristic = n.calculate_heuristic(goal)
            if n.heuristic < min_heuristic:
                min_heuristic = n.heuristic
                next_state = n

        if min_heuristic >= start.heuristic:
            return start  # Local maxima reached

        start = next_state


def main():
    start = Puzzle(
        [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]],
        zero_row=1, zero_col=1
    )

    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    result = hill_climbing(start, goal)

    print("Result board after hill climbing:")
    for row in result.board:
        print(" ".join(map(str, row)))

    if result.is_goal(goal):
        print("Goal reached!")
    else:
        print("Stopped at local maxima, goal not reached.")


if __name__ == "__main__":
    main()