# Minimum Moves to Clean the Classroom

Difficulty: Medium
Topic: Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix
LeetCode: https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

## Problem

You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

- 'S': Starting position of the student

- 'L': Litter that must be collected (once collected, the cell becomes empty)

- 'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)

- 'X': Obstacle the student cannot pass through

- '.': Empty space

You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

 

Example 1:

Input: classroom = ["S.", "XL"], energy = 2

Output: 2

Explanation:

- The student starts at cell (0, 0) with 2 units of energy.

- Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.

- A valid sequence of moves to collect all litter is as follows:

- Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.

- Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.

- The student collects all the litter using 2 moves. Thus, the output is 2.

Example 2:

Input: classroom = ["LS", "RL"], energy = 4

Output: 3

Explanation:

- The student starts at cell (0, 1) with 4 units of energy.

- A valid sequence of moves to collect all litter is as follows:

- Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.

- Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.

- Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.

- The student collects all the litter using 3 moves. Thus, the output is 3.

Example 3:

Input: classroom = ["L.S", "RXL"], energy = 3

Output: -1

Explanation:

No valid path collects all 'L'.

 

Constraints:

- 1 <= m == classroom.length <= 20

- 1 <= n == classroom[i].length <= 20

- classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'

- 1 <= energy <= 50

- There is exactly one 'S' in the grid.

- There are at most 10 'L' cells in the grid.

## Approach

Model the problem as a shortest-path search over states (row, col, remaining energy, bitmask of collected litter) and run BFS, since every move costs exactly 1. Key pruning: for a fixed (row, col, bitmask), a state with higher remaining energy always dominates one with lower energy (it can do everything the lower one can, plus more), so we only enqueue a state if it strictly improves the best energy seen for that (row, col, bitmask). This keeps the explored state space bounded by m*n*2^L*energy instead of exploding combinatorially.

**Brute-force alternative:** Try every possible order/path of visiting the 'L' cells with DFS/backtracking over all move sequences, tracking energy as you go; this explores exponentially many paths and revisits the same (position, energy) many times, making it infeasible even for small grids.

## Algorithm

1. Scan the grid to find the start 'S', assign each 'L' cell a bit index (0..L-1), and compute full_mask = (1<<L)-1.
2. If there is no litter (full_mask == 0), return 0 immediately.
3. Initialize a 3D array best[r][c][mask] = -1 storing the best (max) energy ever recorded for that state; set best[start][mask=0] = energy (the max capacity).
4. Push the initial state (start_row, start_col, energy, mask=0, moves=0) into a FIFO queue.
5. While the queue is not empty, pop a state (r, c, e, mask, moves).
6. For each of the 4 neighbors (nr, nc): skip if out of bounds or an obstacle 'X', and skip the move entirely if current energy e == 0 (student is stuck unless already on 'R', which was already handled when the state was created).
7. Compute new_energy = e - 1; if the neighbor cell is 'R', override new_energy = max capacity energy.
8. Compute new_mask = mask | (1 << litter_index) if the neighbor is an uncollected litter cell, else new_mask = mask.
9. If new_mask == full_mask, all litter is collected, so return moves + 1.
10. Otherwise, if new_energy > best[nr][nc][new_mask], update best[nr][nc][new_mask] = new_energy and enqueue (nr, nc, new_energy, new_mask, moves + 1).
11. If the queue empties without reaching full_mask, return -1 (impossible).

## Complexity

Time: O(m * n * energy * 2^L)
Space: O(m * n * energy * 2^L)

## Edge Cases

- No litter in the grid at all (returns 0 immediately)
- Litter unreachable due to obstacles or insufficient energy with no reset in between (returns -1)
- Energy hits exactly 0 on a non-reset cell, correctly halting further expansion from that state
- Multiple reset 'R' cells usable repeatedly to refill energy
- Student revisiting an already-collected litter cell (mask bit already set, no-op)
- Start cell adjacent to litter requiring zero energy overhead

## Tests

12/12 passed

## Key Learning

Augmenting BFS state with extra dimensions (bitmask for subsets, resource/energy level) to turn a constrained pathfinding problem into a plain shortest-path search; Bitmask representation for 'visited subset' tracking when the subset size is small (<=10 here); Dominance pruning: discarding states that are provably no better than an already-recorded state (higher energy for same position+mask always dominates lower energy), which keeps BFS tractable; Recognizing uniform edge weight (each move costs 1) means plain BFS suffices instead of Dijkstra

## Review

Score: 8.8/10

Strengths:
- Correctly identifies the state as (row, col, energy, bitmask) and BFS is a sound choice since every move costs exactly 1
- The energy-domination pruning (only enqueue if energy strictly improves best[r][c][mask]) is a genuinely non-trivial and correct insight — it soundly collapses an otherwise exponential energy dimension because BFS processes moves in non-decreasing order, so a later state with equal-or-higher energy always dominates
- Handles recharge (reset to max, not additive), obstacles, and early-return on collecting all litter correctly
- L=0 edge case (no litter) returns 0 immediately without unnecessary search
- Clean, minimal variable naming and no unnecessary abstraction

Weaknesses:
- The domination-pruning invariant is the crux of the algorithm but has zero inline comments — a future reader (including the learner in a few months) will need to re-derive why 'new_energy > best[...]' is safe
- Space complexity is stated as O(m*n*energy*2^L), but the persistent best[][][] table is only O(m*n*2^L); the energy factor only bounds the transient BFS queue, so the stated bound is technically correct as an upper bound but conflates two different structures
- Storing `moves` in every queue tuple is slightly wasteful — a level-by-level BFS (processing the queue in whole layers) would avoid carrying a redundant counter per node, though this is a minor constant-factor nitpick

Key takeaway: When a search state includes a resource that only helps (like remaining energy), you can prune the state space by keeping only the Pareto-dominant instance per (position, other-state) pair — i.e., discard any newly reached state whose resource level doesn't strictly exceed the best seen so far.

---

*Generated by DSA Daily Agent. This solution was prepared automatically; submitting it on LeetCode is always a manual step.*
