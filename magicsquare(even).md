## <u>AIM</u>  
To generate a magic square of size n × n where n is an even integer (≥ 4).

---

## Algorithm

1. *Input Validation*  
   - Read integer n.  
   - If n < 4 or n is odd → print error and exit.  

2. *Initialize Square*  
   - Create a 2D vector square[n][n] initialized with 0.

3. *Case 1: Doubly Even Order (n % 4 == 0)*  
   - Fill numbers 1 to n² sequentially.  
   - For each cell (i, j):  
     - If (i % 4 == j % 4) *or* (i % 4 + j % 4 == 3), assign n*n + 1 - num.  
     - Otherwise assign num.  
   - This ensures diagonally symmetric replacements maintain the magic property.

4. *Case 2: Singly Even Order (n % 4 != 0)*  
   - Divide into 4 sub-squares of size n/2 × n/2.  
   - Generate a magic square for the n/2 sub-square using the *Siamese method* (odd-order).  
   - Place these sub-squares into the larger matrix with value shifts:  
     - Top-left → val  
     - Bottom-right → val + subSize  
     - Top-right → val + 2*subSize  
     - Bottom-left → val + 3*subSize  
   - Perform swaps between certain columns to maintain the magic property.

5. *Output*  
   - Print the generated n × n magic square.  
   - Each row should sum to the same constant, and all columns and diagonals will also sum to this constant.

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

## Code 
```cpp

#include <iostream>
#include <vector>
using namespace std;

void generateEvenMagicSquare(int n) {
    if (n < 4 || n % 2 != 0) {
        cout << "Enter an even number >= 4.\n";
        return;
    }

    vector<vector<int>> square(n, vector<int>(n));

    if (n % 4 == 0) {
        int num = 1;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                square[i][j] = ((i % 4 == j % 4) || ((i % 4 + j % 4) == 3)) ? n * n + 1 - num++ : num++;
    } else {
        int half = n / 2, subSize = half * half;
        vector<vector<int>> sub(half, vector<int>(half));

        int i = 0, j = half / 2;
        for (int num = 1; num <= subSize; num++) {
            sub[i][j] = num;
            int ni = (i - 1 + half) % half;
            int nj = (j + 1) % half;
            if (sub[ni][nj] != 0) i = (i + 1) % half;
            else { i = ni; j = nj; }
        }

        for (int r = 0; r < half; r++)
            for (int c = 0; c < half; c++) {
                int val = sub[r][c];
                square[r][c] = val;
                square[r + half][c + half] = val + subSize;
                square[r][c + half] = val + 2 * subSize;
                square[r + half][c] = val + 3 * subSize;
            }

        int k = (half - 1) / 2;
        for (int r = 0; r < half; r++)
            for (int c = 0; c < k; c++)
                swap(square[r][c], square[r + half][c]);
        for (int r = 0; r < half; r++)
            for (int c = n - k + 1; c < n; c++)
                swap(square[r][c], square[r + half][c]);
    }

    cout << "Magic square of size " << n << ":\n";
    for (auto &row : square) {
        for (int val : row) cout << val << "\t";
        cout << "\n";
    }
}

int main() {
    int n;
    cout << "Enter an even number for Magic Square: ";
    cin >> n;
    generateEvenMagicSquare(n);
    return 0;
}

```

---

## Output

<img width="384" height="116" alt="Screenshot 2025-08-24 at 9 52 40 PM" src="https://github.com/user-attachments/assets/4b9d6d28-ebb5-49e5-b54b-8a6b5741afe7" />



