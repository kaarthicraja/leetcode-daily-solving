from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_index = {}
        start = None
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start = (r, c)
                elif ch == 'L':
                    litter_index[(r, c)] = len(litter_index)

        L = len(litter_index)
        full_mask = (1 << L) - 1
        if full_mask == 0:
            return 0

        max_energy = energy
        sr, sc = start

        best = [[[-1] * (full_mask + 1) for _ in range(n)] for _ in range(m)]
        best[sr][sc][0] = max_energy

        q = deque()
        q.append((sr, sc, max_energy, 0, 0))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c, e, mask, moves = q.popleft()
            if e <= 0:
                continue
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                if classroom[nr][nc] == 'X':
                    continue

                new_energy = e - 1
                if classroom[nr][nc] == 'R':
                    new_energy = max_energy

                new_mask = mask
                if (nr, nc) in litter_index:
                    new_mask = mask | (1 << litter_index[(nr, nc)])

                if new_mask == full_mask:
                    return moves + 1

                if new_energy > best[nr][nc][new_mask]:
                    best[nr][nc][new_mask] = new_energy
                    q.append((nr, nc, new_energy, new_mask, moves + 1))

        return -1