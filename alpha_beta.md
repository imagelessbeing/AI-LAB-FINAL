## AIM
To implement **Alpha-Beta Pruning** for a two-player game scenario

---

## Algorithm

1. **State Structure**  
   Each state is represented as a `struct State`:
   - `x, y` → coordinates of the node  
   - `g` → cost from start to current node  
   - `h` → heuristic estimate to goal (Manhattan distance)  
   - `f` → total value (used for evaluation)  
   - `solved` → true if goal reached  
   - `isMaxNode` → true for MAX nodes, false for MIN nodes  
   - `children` → vector of pointers to child states

2. **Heuristic Function**  
   - `heuristic(State* s, State* goal)` calculates **Manhattan distance** from the current state to the goal.

3. **Goal Test**  
   - `isGoalState(State* node, State* goal)` checks if the current coordinates match the goal coordinates.

4. **Move Generation**  
   - Each node can move **Up, Down, Left, Right** inside the 5×5 grid.  
   - For each valid move, a new `State` object is created and added to `children`.

5. **Alpha-Beta Pruning**  
   - `alphaBetaSearch()` recursively evaluates states:  
     - MAX nodes try to **maximize** the value  
     - MIN nodes try to **minimize** the value  
     - Alpha and Beta values prune branches that cannot influence the final decision.  
   - Pruning logs are printed when a branch is skipped.

6. **Path Printing**  
   - `printPath()` prints the path from start to goal showing MAX/MIN nodes and `f` values.  
   - Stops after printing a depth of 10 for readability.

7. **Memory Cleanup**  
   - `cleanup()` recursively deletes all dynamically allocated states to avoid memory leaks.

---

## Time Complexity
- Worst-case complexity is **O(b^d)** where `b` is branching factor (up to 4) and `d` is the maximum search depth.  
- Alpha-Beta pruning reduces unnecessary evaluations compared to naive Minimax.

---

## Code

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <algorithm>
#include <climits>
using namespace std;

struct State {
    int x, y;
    double g, h, f;
    bool solved;
    bool isMaxNode; 
    vector<State*> children;
    
    State(int x, int y, double g, bool isMax) : x(x), y(y), g(g), h(0), f(0), solved(false), isMaxNode(isMax) {}
};

double heuristic(State* s, State* goal) {
    return abs(s->x - goal->x) + abs(s->y - goal->y);
}

bool isGoalState(State* node, State* goal) {
    return (node->x == goal->x && node->y == goal->y);
}

double alphaBetaSearch(State* node, State* goal, double alpha, double beta, 
                    int depth, int maxDepth) {
    
    if (depth >= maxDepth || isGoalState(node, goal)) {
        node->f = node->g + heuristic(node, goal);
        if (isGoalState(node, goal)) {
            node->solved = true;
            node->f = node->g; 
        }
        return node->f;
    }
    
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    
    node->children.clear();
    for (int k = 0; k < 4; k++) {
        int nx = node->x + dx[k];
        int ny = node->y + dy[k];
        if (nx >= 0 && ny >= 0 && nx < 5 && ny < 5) {
            State* child = new State(nx, ny, node->g + 1, !node->isMaxNode);
            node->children.push_back(child);
        }
    }
    
    if (node->children.empty()) {
        node->f = (node->isMaxNode) ? -1e9 : 1e9; 
        return node->f;
    }
    
    double bestValue;
    
    if (node->isMaxNode) {
        bestValue = -1e9;
        for (State* child : node->children) {
            double childValue = alphaBetaSearch(child, goal, alpha, beta, depth + 1, maxDepth);
            bestValue = max(bestValue, childValue);
            alpha = max(alpha, bestValue);
            
            if (beta <= alpha) {
                cout << "Pruning at MAX node (" << node->x << "," << node->y << ")" 
                    << " alpha=" << alpha << " beta=" << beta << endl;
                break; 
            }
        }
    } else {
        bestValue = 1e9;
        for (State* child : node->children) {
            double childValue = alphaBetaSearch(child, goal, alpha, beta, depth + 1, maxDepth);
            bestValue = min(bestValue, childValue);
            beta = min(beta, bestValue);
            
            if (beta <= alpha) {
                cout << "Pruning at MIN node (" << node->x << "," << node->y << ")" 
                    << " alpha=" << alpha << " beta=" << beta << endl;
                break; 
            }
        }
    }
    
    node->f = bestValue;
    return bestValue;
}

void printPath(State* node, State* goal, int depth = 0) {
    if (!node) return;
    
    cout << string(depth * 2, ' ') << "(" << node->x << "," << node->y << ") "
        << (node->isMaxNode ? "MAX" : "MIN") << " f=" << node->f << endl;
    
    if (isGoalState(node, goal)) {
        cout << string(depth * 2, ' ') << "GOAL REACHED!" << endl;
        return;
    }
    
    State* bestChild = nullptr;
    double bestValue = node->isMaxNode ? -1e9 : 1e9;
    
    for (State* child : node->children) {
        if (node->isMaxNode && child->f > bestValue) {
            bestValue = child->f;
            bestChild = child;
        } else if (!node->isMaxNode && child->f < bestValue) {
            bestValue = child->f;
            bestChild = child;
        }
    }
    
    if (bestChild && depth < 10) { 
        printPath(bestChild, goal, depth + 1);
    }
}

void cleanup(State* node) {
    if (!node) return;
    for (State* child : node->children) {
        cleanup(child);
    }
    delete node;
}

int main() {
    int sx, sy, gx, gy;
    cout << "Enter start coordinates (x y): ";
    cin >> sx >> sy;
    cout << "Enter goal coordinates (x y): ";
    cin >> gx >> gy;
    
    int maxDepth;
    cout << "Enter maximum search depth: ";
    cin >> maxDepth;
    
    State* start = new State(sx, sy, 0, true);
    State* goal = new State(gx, gy, 0, false); 
    
    double result = alphaBetaSearch(start, goal, -1e9, 1e9, 0, maxDepth);
    
    cout << "\nFinal result: " << result << endl;
    printPath(start, goal);
    
    cleanup(start); 
    
    return 0;
}
```
## Output 
<img width="476" height="257" alt="Screenshot 2025-09-20 at 10 49 28 AM" src="https://github.com/user-attachments/assets/8a69ba1f-8710-4b28-978d-85be0e0fdd12" />
