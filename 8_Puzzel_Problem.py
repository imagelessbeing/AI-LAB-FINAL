def is_goal(state):
    return state == [[1,2,3],[4,5,6],[7,8,0]]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move_tile(state, x1, y1, x2, y2):
    new_state = [row[:] for row in state] 
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            neighbor = move_tile(state, x, y, nx, ny)
            neighbors.append(neighbor)
    return neighbors

def dfs(start_state):
    stack = [start_state]
    visited = []

    while stack:
        current = stack.pop()

        if current in visited:
            continue
        visited.append(current)

        if is_goal(current):
            print("Goal reached!")
            for row in current:
                print(row)
            return

        for neighbor in get_neighbors(current):
            stack.append(neighbor)

    print("No solution found.")

que = [[1,5,6],
       [4,0,2],
       [3,7,8]]

dfs(que)