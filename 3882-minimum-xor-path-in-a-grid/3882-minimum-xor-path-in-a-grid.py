class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        
        for j in range(1, n):
            for val in dp[j - 1]:
                dp[j].add(val ^ grid[0][j])
                
        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            for val in dp[0]:
                new_dp[0].add(val ^ grid[i][0])
            dp[0] = new_dp[0]
            
            for j in range(1, n):
                for val in dp[j]:
                    new_dp[j].add(val ^ grid[i][j])
                for val in dp[j - 1]:
                    new_dp[j].add(val ^ grid[i][j])
                dp[j] = new_dp[j]
                
        return min(dp[n - 1])