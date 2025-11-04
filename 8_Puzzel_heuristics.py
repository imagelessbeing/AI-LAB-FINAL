import heapq

class State:
    def __init__(self, grid, id_, parent_id):
        self.id = id_
        self.parent_id = parent_id
        self.s = [row[:] for row in grid]  # deep copy

def goal_test(current, goal):
    for i in range(3):
        for j in range(3):
            if current.s[i][j] != goal.s[i][j]:
                return False
    return True

def visited(closed, cur):
    for state in closed:
        if goal_test(state, cur):
            return True
    return False

def heuristic_value(current, goal):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if current.s[i][j] != 0 and current.s[i][j] != goal.s[i][j]:
                misplaced += 1
    return misplaced

def generate_moves(current, id_counter):
    moves = []
    blank_i, blank_j = -1, -1

    # find blank space
    for i in range(3):
        for j in range(3):
            if current.s[i][j] == 0:
                blank_i, blank_j = i, j
                break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for di, dj in directions:
        new_i, new_j = blank_i + di, blank_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_grid = [row[:] for row in current.s]
            new_grid[blank_i][blank_j], new_grid[new_i][new_j] = new_grid[new_i][new_j], new_grid[blank_i][blank_j]
            new_state = State(new_grid, id_counter[0], current.id)
            id_counter[0] += 1
            moves.append(new_state)

    return moves

def main():
    id_counter = [1]

    print("Please enter the initial state (use 0 for blank):")
    initial_grid = [[int(x) for x in input().split()] for _ in range(3)]
    initial = State(initial_grid, id_counter[0], -1)
    id_counter[0] += 1

    print("Please enter the goal state (use 0 for blank):")
    goal_grid = [[int(x) for x in input().split()] for _ in range(3)]
    goal = State(goal_grid, 0, -1)

    if goal_test(initial, goal):
        print("Puzzle already solved.")
        return

    # priority queue: (heuristic, state)
    heap = []
    closed = []

    heapq.heappush(heap, (heuristic_value(initial, goal), initial))
    closed.append(initial)

    found = False
    found_goal = None

    while heap:
        _, current = heapq.heappop(heap)

        if goal_test(current, goal):
            found = True
            found_goal = current
            break

        for child in generate_moves(current, id_counter):
            if not visited(closed, child):
                heapq.heappush(heap, (heuristic_value(child, goal), child))
                closed.append(child)

    if found:
        path = []
        cur = found_goal
        while True:
            path.append(cur)
            if cur.parent_id == -1:
                break
            for state in closed:
                if state.id == cur.parent_id:
                    cur = state
                    break

        print("\nPuzzle Solved.")
        print("Path is:")
        for p in reversed(path):
            for row in p.s:
                print(' '.join(map(str, row)))
            print("->")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()