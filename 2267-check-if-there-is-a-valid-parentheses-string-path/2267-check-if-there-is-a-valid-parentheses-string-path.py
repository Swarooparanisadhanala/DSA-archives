from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # A valid path must have an even length (m + n - 1)
        if (m + n - 1) % 2 != 0:
            return False
            
        # Path cannot start with ')' or end with '('
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        @cache
        def dfs(r: int, c: int, balance: int) -> bool:
            # Update current balance based on the parenthesis at (r, c)
            balance += 1 if grid[r][c] == '(' else -1

            # If closing brackets exceed opening brackets, path is invalid
            if balance < 0:
                return False

            # Reached bottom-right cell
            if r == m - 1 and c == n - 1:
                return balance == 0

            # Move down or right
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
            if c + 1 < n and dfs(r, c + 1, balance):
                return True

            return False

        return dfs(0, 0, 0)