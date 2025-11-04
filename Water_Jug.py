from collections import deque

def water_jug_bfs(jug1, jug2, target):
    q = deque([(0, 0)])
    
    visited = set((0, 0))
    
    while q:
        x, y = q.popleft()
        
        print(f"Jug1: {x}, Jug2: {y}")
        
        if x == target or y == target:
            print("Reached the target!")
            return True

        next_states = [
            (jug1, y),      
            (x, jug2),      
            (0, y),         
            (x, 0),         
            (min(jug1, x + y), 0 if x + y <= jug1 else y - (jug1 - x)),  # Pour jug2 -> jug1
            (0 if x + y <= jug2 else x - (jug2 - y), min(jug2, x + y))   # Pour jug1 -> jug2
        ]
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                q.append(state)
    
    print("No solution possible.")
    return False

water_jug_bfs(5, 3, 4)   