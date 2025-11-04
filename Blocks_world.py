from copy import deepcopy

class State:
    def __init__(self):
        self.on = []       # list of (block, on_what)
        self.moves = []    # list of move descriptions


def is_goal(state, goal):
    for block, target in goal:
        found = any(b == block and o == target for b, o in state.on)
        if not found:
            return False
    return True


def get_clear_blocks(state):
    all_blocks = [b for b, _ in state.on]
    has_something_on_top = [o for _, o in state.on if o != "Table"]
    return [b for b in all_blocks if b not in has_something_on_top]


def children(current):
    next_states = []
    clear_blocks = get_clear_blocks(current)

    for x in clear_blocks:
        # Find what x is currently on
        under = next(o for b, o in current.on if b == x)

        # Move x to table
        if under != "Table":
            new_state = deepcopy(current)
            for i, (b, o) in enumerate(new_state.on):
                if b == x:
                    new_state.on[i] = (b, "Table")
                    break
            move = f"Move {x} to Table"
            new_state.moves.append(move)
            next_states.append(new_state)

        # Move x onto another clear block y
        for y in clear_blocks:
            if y == x:
                continue
            new_state = deepcopy(current)
            for i, (b, o) in enumerate(new_state.on):
                if b == x:
                    new_state.on[i] = (b, y)
                    break
            move = f"Move {x} onto {y}"
            new_state.moves.append(move)
            next_states.append(new_state)

    return next_states


def dfs(start, goal, depth_limit):
    stack = [start]
    while stack:
        current = stack.pop()
        if is_goal(current, goal):
            print("Goal reached!\nSequence of moves:")
            for m in current.moves:
                print(m)
            return True

        if len(current.moves) < depth_limit:
            for ns in children(current):
                stack.append(ns)
    return False


def main():
    n = int(input("Enter number of blocks: "))
    start = State()
    goal = []

    print("\nEnter start state (format: Block On):")
    for _ in range(n):
        block, on = input().split()
        start.on.append((block, on))

    print("\nEnter goal state (format: Block On):")
    for _ in range(n):
        block, on = input().split()
        goal.append((block, on))

    depth_limit = int(input("\nEnter depth limit: "))

    if not dfs(start, goal, depth_limit):
        print("Goal not found within depth limit.")


if __name__ == "__main__":
    main()