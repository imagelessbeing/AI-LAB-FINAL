
## <u>AIM</u>
To solve the 8 Puzzle Problem using **Depth First Search (DFS)** 

---

## Algorithm

1. **State Structure**
   - Maintain a `state` structure with:
     - `id` → unique identifier of the state
     - `parent_id` → id of the state from which this was generated
     - `s[3][3]` → 3×3 integer array for puzzle configuration

2. **Goal Test**
   - Function `goal_test()` checks if the current state matches the goal state.

3. **Move Generation**
   - Function `generate_moves()` finds the position of the blank (0) tile.
   - Based on the blank tile’s position, generate all possible valid moves:
     - Move **Up** 
     - Move **Down** 
     - Move **Left** 
     - Move **Right** 
   - For example:
     - If blank is at `(0,0)`, moves: Right, Down
     - If blank is at `(1,1)`, moves: Up, Down, Left, Right

4. **DFS Search**
   - Use a **stack** to store states to explore.
   - Push the initial state onto the stack, mark it visited.
   - Maintain a **closed list** to store visited states.
   - While the stack is not empty:
     1. Pop the top state.
     2. If it is the goal state → reconstruct and print the path using `parent_id`.
     3. Otherwise:
        - Generate possible moves from this state.
        - For each new state:
          - If it is **not in closed list**, assign a new `id` and set its `parent_id` to the current state’s `id`, then push it to the stack.

5. **Path Reconstruction**
   - Once the goal state is found, use `parent_id` links to trace back to the initial state.
   - Print the sequence of states.

---

## Time Complexity
- **Worst-case time complexity**:  
  \[
  O(branching factor^maximum depth)
  \]  
 
- **Space complexity**:  
  DFS uses \( O(bm) \) for the stack plus space for the closed list.

---

## Use Cases
- Understanding DFS traversal in a finite state problem.
- State representation and path reconstruction.


