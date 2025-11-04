## <u>AIM</u>  
To implement a Tic-Tac-Toe game using modified 2nd approach.

---

## Algorithm

1. **Board Representation**  
   - Use an integer array `BOARD[10]` (1-based indexing) where:  
     - `2` → empty  
     - `3` → computer's move ('X')  
     - `5` → human's move ('O')

2. **Magic Square Mapping**  
   - Use a `magicSquare[10]` array that maps board positions to a magic square numbering (1 to 9) with sums of any winning line equal to 15.  
   - Positions mapped as:  
     `{0, 8, 3, 4, 1, 5, 9, 6, 7, 2}` (index 0 unused)

3. **Display Board**  
   - Print the board using symbols:  
     - `'_'` for empty, `'X'` for computer, `'O'` for human.

4. **Check Possible Winning Move (`POSSWIN`)**  
   - For a given player, check all pairs of positions occupied by that player.  
   - Calculate the missing magic square number to reach 15.  
   - If the corresponding position is empty, return that position as a winning/blocking move.

5. **Make a Move (`GO`)**  
   - Place the player's mark on the board if the position is valid and empty.

6. **Check Win Condition**  
   - Use predefined winning lines.  
   - Compute product of values at these positions:  
     - `27` (3*3*3) means computer wins  
     - `125` (5*5*5) means human wins.

7. **Check Draw**  
   - Game is a draw if no empty positions remain and no winner.

8. **Take Center or Sides (`MAKE2`)**  
   - If center (position 5) is free, take it.  
   - Else take one of the sides (positions 2, 4, 6, 8).

9. **Game Loop**  
   - Alternates between human and computer turns.  
   - Human inputs a valid move.  
   - Computer chooses a move based on:  
     - Winning move if available.  
     - Block opponent’s winning move.  
     - Take center or sides.  
     - Take any available spot otherwise.  
   - After each move, check for win or draw.  
   - End game on win/draw.

---

## Time Complexity  
- Move decisions involve iterating through positions and pairs → \( O(n^2) \) where \( n=9 \), practically constant.

---

## Space Complexity  
- Uses fixed arrays for board and magic square → \( O(1) \).


## Use Cases  
- Demonstrates an alternate method (magic square) for move calculation in Tic-Tac-Toe.  
- Illustrates use of mathematical properties (magic square sums) for game logic.

## Space Complexity  
- Memory usage depends on the number of visited states and the size of the priority queue.

---

## Use Cases  
- Demonstrates how heuristic information can guide search in a finite state problem.  
- Illustrates state representation, successor generation, and solution path reconstruction.

---
