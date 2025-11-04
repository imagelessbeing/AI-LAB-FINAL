## AIM
To implement **AO\* (And-Or) Search** 

---

## Algorithm

1. **State Structure**  
   Each state is represented as a `struct State`:
   - `x, y` → coordinates of the node  
   - `g` → cost from start to current node  
   - `h` → heuristic estimate to goal (Manhattan distance)  
   - `f` → total estimated cost (`f = g + h`)  
   - `solved` → true if goal reached  
   - `isAndNode` → true if AND node (used in generalized AO\* problems)  
   - `children` → vector of pointers to child states

2. **Heuristic Function**  
   - `heuristic(State* s, State* goal)` calculates **Manhattan distance** from the current state to the goal.

3. **AO\* Search Function**  
   - `AOStar()` recursively evaluates nodes:  
     - Skips nodes that are already solved or visited  
     - Generates all valid successors by moving **Up, Down, Left, Right** in the 5×5 grid  
     - Updates `f` values as `g + min(child_f)` for OR nodes  
     - Marks node as `solved` if goal reached

4. **Visited Set**  
   - Prevents revisiting nodes using a `set<pair<int,int>>` of coordinates.

5. **Memory Management**  
   - All dynamically allocated states are stored in `allStates` and deleted at the end to avoid memory leaks.

---

## Time Complexity
- In the worst case, AO\* explores **all reachable nodes**, giving **O(b^d)** complexity, where `b` is branching factor (up to 4) and `d` is maximum depth.  
- AO\* uses heuristic estimates to prune unnecessary paths, improving efficiency over naive search.

---
