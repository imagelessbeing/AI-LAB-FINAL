import math

class State:
    def __init__(self, x, y, g=0, h=0, f=0, parent_id=-1, node_id=0):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f
        self.id = node_id
        self.parent_id = parent_id

def goal_test(current, goal):
    return current.x == goal.x and current.y == goal.y

def visited(closed, cur):
    for node in closed:
        if node.x == cur.x and node.y == cur.y:
            return True
    return False

def heuristic(current, goal):
    # Manhattan distance heuristic
    return abs(current.x - goal.x) + abs(current.y - goal.y)

def generate_moves(current, id_counter, goal, n, board):
    moves = []
    dir_x = [-1, -1, -1, 0, 0, 1, 1, 1]
    dir_y = [-1, 0, 1, -1, 1, -1, 0, 1]

    for k in range(8):
        new_x = current.x + dir_x[k]
        new_y = current.y + dir_y[k]

        if 0 <= new_x < n and 0 <= new_y < n and board[new_x][new_y] == 0:
            next_state = State(new_x, new_y)
            next_state.id = id_counter[0]
            id_counter[0] += 1
            next_state.parent_id = current.id
            next_state.g = current.g + (1.0 if dir_x[k] == 0 or dir_y[k] == 0 else 1.5)
            next_state.h = heuristic(next_state, goal)
            next_state.f = next_state.g + next_state.h
            moves.append(next_state)
    return moves

def main():
    n = int(input("Enter board size n: "))
    board = [[0] * n for _ in range(n)]

    start_x, start_y = map(int, input("Enter start cell (row col): ").split())
    goal_x, goal_y = map(int, input("Enter destination cell (row col): ").split())

    blocks = int(input("Enter number of blocked cells: "))
    print("Enter blocked cells (row col):")
    for _ in range(blocks):
        bx, by = map(int, input().split())
        board[bx][by] = 1

    id_counter = [1]
    start = State(start_x, start_y, g=0)
    start.id = id_counter[0]
    id_counter[0] += 1
    start.parent_id = -1

    goal = State(goal_x, goal_y)
    start.h = heuristic(start, goal)
    start.f = start.g + start.h

    open_list = [start]
    closed = []
    found = False
    found_goal = None

    while open_list:
        best_idx = min(range(len(open_list)), key=lambda i: open_list[i].f)
        current = open_list.pop(best_idx)

        if visited(closed, current):
            continue
        closed.append(current)

        if goal_test(current, goal):
            found = True
            found_goal = current
            break

        for child in generate_moves(current, id_counter, goal, n, board):
            if not visited(closed, child):
                open_list.append(child)

    if found:
        path = []
        cur = found_goal
        while True:
            path.append(cur)
            if cur.parent_id == -1:
                break
            for node in closed:
                if node.id == cur.parent_id:
                    cur = node
                    break

        print("\nPath found:")
        for p in reversed(path):
            print(f"({p.x},{p.y}) g={p.g:.1f} h={p.h:.1f} f={p.f:.1f}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()