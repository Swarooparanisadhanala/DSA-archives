from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        valid_islands = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    # Start DFS for the current island
                    current_sum = 0
                    stack = [(r, c)]
                    visited[r][c] = True
                    
                    while stack:
                        curr_r, curr_c = stack.pop()
                        current_sum += grid[curr_r][curr_c]
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] > 0:
                                visited[nr][nc] = True
                                stack.append((nr, nc))
                    
                    if current_sum % k == 0:
                        valid_islands += 1
                        
        return valid_islands