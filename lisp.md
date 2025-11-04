## <u>AIM</u>  
To implement a Tic-Tac-Toe game using lisp.

---

## Algorithm

### 1. Board Representation 
- Board stored as a 1D array of size `9`  
- `nil` → empty  
- `'X` → human  
- `'O` → computer  

### 2. Display Board
- Function `print-board` prints each cell  
- Uses `-` for empty cells  
- Prints newline after every 3 cells  

### 3. Winning Move Check (`POSSWIN`)
- Function `winner` checks all 8 possible winning lines  
- Condition:  
  ```lisp
  if (a = b = c ≠ nil)
      winner = a
  ```

### 4. Make a Move (`GO`)
- Function `best-move` tries each empty cell  
- Temporarily places `'O`  
- Calls `minimax` to evaluate score  
- Chooses move with maximum score  

### 5. Check Win Condition
- If `winner(board)` = `'X` → player wins  
- If `winner(board)` = `'O` → computer wins  

### 6. Check Draw
- Function `full-board-p(board)`  
  ```lisp
  (notany #'null board)
  ```
- If true and no winner → draw  

### 7. Helper Function (`MAKE2` / `minimax`)
- Recursive evaluation of moves  
- `'O` (maximizing) → choose max score  
- `'X` (minimizing) → choose min score  
- Scoring logic:  
  ```text
  X wins → -10 + depth
  O wins → +10 - depth
  Draw   → 0
  ```

### 8. Game Loop
1. Display board  
2. Human plays `'X`  
3. Check win/draw  
4. Computer plays `'O` using `best-move`  
5. Check win/draw  
6. Repeat until game ends  

---

## Time Complexity  
- In the worst case, the algorithm explores **every possible game state** of Tic-Tac-Toe.
- There are **9 cells**, and each move reduces the available positions by one.

Hence, total possible board states ≈  
```
9! = 9 × 8 × 7 × ... × 1 = 362,880
```
However, due to pruning through terminal checks (`winner` and `full-board-p`), not all states are explored.

- Worst-case (no pruning): `O(9!)`
- Average practical case (with early wins/draws): `O(b^d)`  
  where  
  `b = branching factor ≈ 9`  
  `d = depth of game ≈ 9`
 
- *Time Complexity:* O(9!)  

---

## Space Complexity  
- The main space is used by:
  1. The board array → `O(9)`
  2. Recursive call stack of `minimax` → depth = 9
  
- *Space Complexity:* O(9)

---
 
## Use Cases  
- *Educational Purpose:* Helps learn how use lisp in simple algorithms .
- *Game Development:* Can be used as a base for building simple AI opponents in Tic-Tac-Toe.  

---
