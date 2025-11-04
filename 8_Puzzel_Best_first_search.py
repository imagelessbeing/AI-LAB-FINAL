import heapq

def is_goal(state):
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    if state == goal:
        return True
    else:
        return False

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

def move_tile(state, x1, y1, x2, y2):
    new_state = []
    for row in state:
        new_state.append(row[:])
    temp = new_state[x1][y1]
    new_state[x1][y1] = new_state[x2][y2]
    new_state[x2][y2] = temp
    return new_state

def get_neighbors(state):
    pos = find_zero(state)
    x = pos[0]
    y = pos[1]
    neighbors = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for d in directions:
        new_x = x + d[0]
        new_y = y + d[1]
        if new_x >= 0 and new_x < 3 and new_y >= 0 and new_y < 3:
            neighbor_state = move_tile(state, x, y, new_x, new_y)
            neighbors.append(neighbor_state)
    return neighbors

def heuristic(state):
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                h = h + 1
    return h

def best_first_search(start_state):
    heap = []
    heapq.heappush(heap, (heuristic(start_state), start_state))
    visited = []

    while len(heap) > 0:
        current_tuple = heapq.heappop(heap)
        current = current_tuple[1]

        if current in visited:
            continue
        visited.append(current)

        if is_goal(current):
            print("Goal reached!")
            for r in current:
                print(r)
            return

        neighbors = get_neighbors(current)
        for n in neighbors:
            if n not in visited:
                heapq.heappush(heap, (heuristic(n), n))

    print("No solution found.")

que = [[1,5,6],
       [4,0,2],
       [3,7,8]]

best_first_search(que)