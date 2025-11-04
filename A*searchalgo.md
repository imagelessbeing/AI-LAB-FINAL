## <u>AIM</u>
A* Search Algorithm for nxn matrics.

---
## Algorithm

1. **State Structure**
   - Maintain a `state` structure with:
     - `id` → unique identifier of the state  
     - `parent_id` → id of the state from which this was generated  
     - `x, y` → coordinates of the cell  
     - `g` → cost from start to current state  
     - `h` → heuristic cost from current to goal (Manhattan distance)  
     - `f` → total cost `f = g + h`

2. **Goal Test**
   - Function `goal_test()` checks if the current state coordinates match the goal coordinates.

3. **Visited Check**
   - Function `visited()` ensures the current state is not already explored in the `closed` list.

4. **Heuristic Function**
   - Function `heuristic()` calculates the Manhattan distance between current state and goal:  
     ```
     h = |x_current - x_goal| + |y_current - y_goal|
     ```

5. **Move Generation**
   - Function `generate_moves()` generates all valid moves in **8 directions**:
     - Top-left, Top, Top-right  
     - Left, Right  
     - Bottom-left, Bottom, Bottom-right  
   - Moves are allowed only if within grid boundaries and the cell is **not blocked**.  
   - **Move Cost**:
     - Horizontal/Vertical → `g = 1.0`  
     - Diagonal → `g = 1.5`
       
6. **A* Search**
   - Maintain an **open list** for states to explore and a **closed list** for visited states.  
   - While open list is not empty:
     1. Select the state with **minimum `f` value**.
     2. If it is the goal → reconstruct the path.
     3. Otherwise:
        - Generate children using `generate_moves()`.
        - If a child is **not visited**, assign `id` and `parent_id`, then add to open list.

7. **Path Reconstruction**
   - Once goal is reached, trace back from `found_goal` to start using `parent_id`.  
   - Print the sequence of coordinates along with `g`, `h`, `f` values.

---

## Time Complexity  
O(maximum branching factor ^ depth of solution) 

---

## Space Complexity
O(maximum branching factor ^ depth of solution)  

---

## Use Cases
- Pathfinding on a grid with obstacles.  
- Understanding **A* search with Manhattan heuristic**.  
- Visualizing 8-directional movement cost calculation and path reconstruction.

---


