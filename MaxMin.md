## <u>AIM</u>
To implement a **Tic-Tac-Toe** game using the `Minimax` algorithm.

---

## <u>Algorithm</u>

1. **Board Representation**
   - Use a 1D array `BOARD[10]` (index `1–9`) for the 3×3 grid.
   - Values: `2` = empty, `3` = computer (`X`), `5` = human (`O`).
   - Winning combinations stored in `WIN_LINES[8][3]`.

2. **Display Board**
   - Print the current state of the board with symbols `X`, `O`, or `_` for empty.

3. **Move Generation**
   - **Human Move:** Input validated for empty cells.
   - **Computer Move:** Use `Minimax` algorithm to select the optimal move.
   - **Special Move (`MAKE2`)**: Picks center first or sides if center is occupied.

4. **Winning & Draw Checks**
   - `checkWin(player)` determines if a player has won.
   - `isDraw()` checks if all cells are filled without a winner.

5. **Minimax Algorithm**
   - Recursively evaluates all possible moves.
   - `isMaximizing = true` → computer’s turn, maximize score.
   - `isMaximizing = false` → human’s turn, minimize score.
   - Terminal states: win (`+1`), lose (`-1`), draw (`0`).

6. **Gameplay Loop**
   - Alternate human and computer turns.
   - Display board after each move.
   - Announce winner or draw when the game ends.

---

## <u>Time Complexity</u>
- Worst case: `O(9!)` due to exhaustive evaluation of all moves by `Minimax`.

---

## <u>Space Complexity</u>
- `O(9)` for `BOARD` array plus recursion stack in `Minimax`.

---

## <u>Use Cases</u>
- Demonstrates **game AI** using `Minimax`.
- Ensures **unbeatable computer strategy** for small games like `Tic-Tac-Toe`.
- Can be extended to other **games** like chess.

---
