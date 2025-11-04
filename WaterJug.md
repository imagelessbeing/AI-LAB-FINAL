## <u>AIM</u>  
To solve the classic Water Jug problem using a simulation approach that performs sequential operations to measure a target volume.

---

## Algorithm

1. **Initialize Jug Capacities and States**  
   - Input capacities of jug X and jug Y.  
   - Maintain current volumes `X0` and `Y0` initialized to 0.

2. **Check Feasibility**  
   - Verify that the goal volume is less than or equal to the maximum jug capacity.  
   - Verify that the goal volume is a multiple of the greatest common divisor (GCD) of X and Y.  
   - If not feasible, print an error message and exit.

3. **Operations**  
   - **Fill X**: Fill jug X to its capacity.  
   - **Fill Y**: Fill jug Y to its capacity.  
   - **Empty X**: Empty jug X completely.  
   - **Empty Y**: Empty jug Y completely.  
   - **Pour X to Y**: Pour water from jug X into jug Y until jug Y is full or jug X is empty.  
   - **Pour Y to X**: Pour water from jug Y into jug X until jug X is full or jug Y is empty.

4. **Simulation Loop**  
   - Start with both jugs empty `(X0, Y0) = (0, 0)`.  
   - Repeat until either jug contains the goal volume:  
     - If jug X is empty, fill jug X.  
     - Else if jug Y is not full, pour from X to Y.  
     - Else if jug Y is full, empty jug Y.  
   - After each operation, print the current state.

5. **Goal Test**  
   - Check if `X0 == goal` or `Y0 == goal`. If yes, the goal is reached.

---

## Time Complexity  
- Linear in the number of steps until goal is reached; bounded by jug capacities.

---

## Space Complexity  
- Constant space, tracking only current volumes and constants.

---

## Use Cases  
- Classic puzzle problem solving.  
- Demonstrates rule based approach.

---
