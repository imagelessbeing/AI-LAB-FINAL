## <u>AIM</u>  
To solve the 8-puzzle problem using the **Hill Climbing** heuristic search algorithm with Manhattan distance.

---

## Algorithm

1. **State Representation**  
   - Represent the puzzle board as a 3×3 matrix.  
   - Track the position of the empty tile (0) as `(zero_row, zero_col)`.  
   - Maintain a heuristic value indicating estimated distance to goal.

2. **Heuristic Calculation**  
   - Use the **Manhattan distance** heuristic: sum of distances of each tile from its goal position.

3. **Neighbor Generation**  
   - Generate all possible next states by sliding a tile adjacent to the empty space into the empty space.  
   - Valid moves: up, down, left, right (if within bounds).

4. **Hill Climbing Search**  
   - Start from the initial puzzle state.  
   - At each step, compute neighbors and their heuristic values.  
   - Move to the neighbor with the lowest heuristic if it improves over the current state.  
   - Stop if no neighbor has better heuristic (local maximum) or goal is reached.

5. **Goal Test**  
   - Check if current board configuration matches the goal board.

---

## Time Complexity  
- Depends on the number of states explored before getting stuck in a local maximum or reaching goal.  
- Typically faster than exhaustive search but can get stuck prematurely.

---

## Space Complexity  
- Stores current state and neighbors, so \(O(b)\) where \(b\) is branching factor (up to 4 moves).

---

## Use Cases  
- Illustrates heuristic-based local search algorithms.  
- Useful for solving small puzzles with admissible heuristics.
  
---

## Code 

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct state {
    int id;
    int parent_id;
    int s[3][3];
};

bool goal_test(state current, state goal) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (current.s[i][j] != goal.s[i][j]) {
                return false;
            }
        }
    }
    return true;
}

bool visited(vector<state> closed, state cur) {
    for (int idx = 0; idx < (int)closed.size(); idx++) {
        if (goal_test(closed[idx], cur)) {
            return true;
        }
    }
    return false;
}

int heuristic_value(state current, state goal) {
    int misplaced = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (current.s[i][j] != 0 && current.s[i][j] != goal.s[i][j]) {
                misplaced++;
            }
        }
    }
    return misplaced;
}

vector<state> generate_moves(state current, int &id_counter) {
    vector<state> moves;
    int blank_i = -1, blank_j = -1;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (current.s[i][j] == 0) {
                blank_i = i;
                blank_j = j;
            }
        }
    }

    int dir_i[4] = {-1, 1, 0, 0};
    int dir_j[4] = {0, 0, -1, 1};

    for (int k = 0; k < 4; k++) {
        int new_i = blank_i + dir_i[k];
        int new_j = blank_j + dir_j[k];

        if (new_i >= 0 && new_i < 3 && new_j >= 0 && new_j < 3) {
            state next;
            for (int x = 0; x < 3; x++) {
                for (int y = 0; y < 3; y++) {
                    next.s[x][y] = current.s[x][y];
                }
            }
            next.id = id_counter++;
            next.parent_id = current.id;
            int temp = next.s[blank_i][blank_j];
            next.s[blank_i][blank_j] = next.s[new_i][new_j];
            next.s[new_i][new_j] = temp;
            moves.push_back(next);
        }
    }
    return moves;
}

void heapify(vector<pair<int, state>> &heap, int n, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && heap[left].first < heap[smallest].first)
        smallest = left;
    if (right < n && heap[right].first < heap[smallest].first)
        smallest = right;

    if (smallest != i) {
        swap(heap[i], heap[smallest]);
        heapify(heap, n, smallest);
    }
}

pair<int, state> Min(vector<pair<int, state>> &heap) {
    pair<int, state> root = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    heapify(heap, heap.size(), 0);
    return root;
}

int main() {
    state initial, goal;
    int id_counter = 1;

    cout << "Please enter the initial state (use 0 for blank):\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> initial.s[i][j];
        }
    }
    initial.id = id_counter++;
    initial.parent_id = -1;

    cout << "Please enter the goal state (use 0 for blank):\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> goal.s[i][j];
        }
    }

    if (goal_test(initial, goal)) {
        cout << "Puzzle already solved.\n";
        return 0;
    }

    vector<pair<int, state>> heap; 
    vector<state> closed;

    heap.push_back({heuristic_value(initial, goal), initial});
    closed.push_back(initial);

    bool found = false;
    state found_goal;

    while (!heap.empty()) {
        pair<int, state> current_pair = Min(heap);
        state current = current_pair.second;

        if (goal_test(current, goal)) {
            found = true;
            found_goal = current;
            break;
        }

        vector<state> children = generate_moves(current, id_counter);
        for (int i = 0; i < (int)children.size(); i++) {
            if (!visited(closed, children[i])) {
                heap.push_back({heuristic_value(children[i], goal), children[i]});
                int idx = heap.size() - 1;
                while (idx != 0 && heap[(idx - 1) / 2].first > heap[idx].first) {
                    swap(heap[idx], heap[(idx - 1) / 2]);
                    idx = (idx - 1) / 2;
                }
                closed.push_back(children[i]);
            }
        }
    }

    if (found) {
        vector<state> path;
        state cur = found_goal;
        while (true) {
            path.push_back(cur);
            if (cur.parent_id == -1) break;
            for (int i = 0; i < (int)closed.size(); i++) {
                if (closed[i].id == cur.parent_id) {
                    cur = closed[i];
                    break;
                }
            }
        }

        cout << "Puzzle Solved.\n";
        cout << "Path is :\n";
        for (int p = (int)path.size() - 1; p >= 0; p--) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    cout << path[p].s[i][j] << ' ';
                }
                cout << '\n';
            }
            cout << "->\n";
        }
    } else {
        cout << "No solution found.\n";
    }
}
```
---

## Output
<img width="261" height="74" alt="Screenshot 2025-08-24 at 9 26 09 PM" src="https://github.com/user-attachments/assets/4f962b74-719b-4538-a015-1d19d50f2068" />



