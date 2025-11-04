## <u>AIM</u>  
To generate a magic square of size n × n where n is an odd integer (≥ 3).  

---

## Algorithm  

1. *Input Validation*  
   - Read integer n.  
   - If n < 3 or n is even → print error and exit.  

2. *Initialize Square*  
   - Create a 2D vector `square[n][n]` initialized with 0.  

3. *Siamese Method (for odd n)*  
   - Place `1` in the middle of the top row.  
   - For each next number (2 to n²):  
     - Move one step **up** and **right**.  
     - If the move goes **out of bounds**:  
       - Wrap around (top → bottom, right → left).  
     - If the target cell is already filled:  
       - Move **down one row** instead and place the number.  
   - Continue until all n² numbers are placed.  

4. *Output*  
   - Print the generated n × n magic square.  
   - Each row, column, and diagonal will sum to the same constant:  
     \[
     \text{Magic Constant} = \frac{n(n^2+1)}{2}
     \]  

---

## Time Complexity  
- Filling n × n matrix requires one pass.  
- *Time Complexity:* O(n²)  

---

## Space Complexity  
- Requires a 2D array of size n × n.  
- *Space Complexity:* O(n²)  

---

## Use Cases  
- *Mathematics:* Demonstrates number patterns and properties of magic squares.  
- *Cryptography & Puzzles:* Basis for constructing number-based puzzles and encoding schemes.  

---
