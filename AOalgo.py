import math

class State:
    def __init__(self, x, y, g=0, h=0, f=0, solved=False, is_and_node=False):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = f
        self.solved = solved
        self.is_and_node = is_and_node
        self.children = []

def heuristic(s, goal):
    return abs(s.x - goal.x) + abs(s.y - goal.y)

def AOStar(node, goal, all_states, visited):
    if node.solved:
        return
    if (node.x, node.y) in visited:
        return
    visited.add((node.x, node.y))

    successors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = node.x + dx, node.y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            child = State(nx, ny, node.g + 1)
            child.h = heuristic(child, goal)
            child.f = child.g + child.h
            successors.append(child)
            all_states.append(child)
            node.children.append(child)

    if not successors:
        node.f = float('inf')
        return

    min_cost = float('inf')
    for child in node.children:
        AOStar(child, goal, all_states, visited)
        min_cost = min(min_cost, child.f)

    node.f = node.g + min_cost
    if node.x == goal.x and node.y == goal.y:
        node.solved = True


def main():
    sx, sy = map(int, input("Enter start coordinates (x y): ").split())
    gx, gy = map(int, input("Enter goal coordinates (x y): ").split())

    start = State(sx, sy)
    goal = State(gx, gy)

    all_states = [start]
    visited = set()

    AOStar(start, goal, all_states, visited)

    print(f"Final cost from start to goal: {start.f:.2f}")

if __name__ == "__main__":
    main()