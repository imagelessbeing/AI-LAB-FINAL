import math

class State:
    def __init__(self, x, y, g, is_max_node):
        self.x = x
        self.y = y
        self.g = g
        self.h = 0
        self.f = 0
        self.solved = False
        self.is_max_node = is_max_node
        self.children = []

def heuristic(s, goal):
    return abs(s.x - goal.x) + abs(s.y - goal.y)

def is_goal_state(node, goal):
    return node.x == goal.x and node.y == goal.y

def alpha_beta_search(node, goal, alpha, beta, depth, max_depth, visited):
    if depth >= max_depth or is_goal_state(node, goal):
        node.f = node.g + heuristic(node, goal)
        if is_goal_state(node, goal):
            node.solved = True
            node.f = node.g
        return node.f

    pos = (node.x, node.y)
    if pos in visited:
        return node.f
    visited.add(pos)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for k in range(4):
        nx, ny = node.x + dx[k], node.y + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            child = State(nx, ny, node.g + 1, not node.is_max_node)
            node.children.append(child)

    if not node.children:
        node.f = -1e9 if node.is_max_node else 1e9
        visited.remove(pos)
        return node.f

    if node.is_max_node:
        best_value = -1e9
        for child in node.children:
            child_value = alpha_beta_search(child, goal, alpha, beta, depth + 1, max_depth, visited)
            best_value = max(best_value, child_value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                print(f"Pruning at MAX node ({node.x},{node.y}) alpha={alpha} beta={beta}")
                break
    else:
        best_value = 1e9
        for child in node.children:
            child_value = alpha_beta_search(child, goal, alpha, beta, depth + 1, max_depth, visited)
            best_value = min(best_value, child_value)
            beta = min(beta, best_value)
            if beta <= alpha:
                print(f"Pruning at MIN node ({node.x},{node.y}) alpha={alpha} beta={beta}")
                break

    node.f = best_value
    visited.remove(pos)
    return best_value

def print_path(node, goal, depth=0):
    if not node:
        return
    print(" " * (depth * 2) + f"({node.x},{node.y}) {'MAX' if node.is_max_node else 'MIN'} f={node.f:.2f}")
    if is_goal_state(node, goal):
        print(" " * (depth * 2) + "GOAL REACHED!")
        return

    best_child = None
    best_value = -1e9 if node.is_max_node else 1e9

    for child in node.children:
        if node.is_max_node and child.f > best_value:
            best_value = child.f
            best_child = child
        elif not node.is_max_node and child.f < best_value:
            best_value = child.f
            best_child = child

    if best_child and depth < 10:
        print_path(best_child, goal, depth + 1)

def main():
    sx, sy = map(int, input("Enter start coordinates (x y): ").split())
    gx, gy = map(int, input("Enter goal coordinates (x y): ").split())
    max_depth = int(input("Enter maximum search depth: "))

    start = State(sx, sy, 0, True)
    goal = State(gx, gy, 0, False)
    visited = set()

    result = alpha_beta_search(start, goal, -1e9, 1e9, 0, max_depth, visited)
    print(f"\nFinal result: {result:.2f}\n")
    print_path(start, goal)

if __name__ == "__main__":
    main()