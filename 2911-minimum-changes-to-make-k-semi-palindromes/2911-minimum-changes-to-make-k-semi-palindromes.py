class Solution:

  def minimumChanges(self, s: str, k: int) -> int:
    n = len(s)

    # Function to calculate changes to make a specific slice s[i...j] a palindrome
    def min_changes_palindrome(sub: str) -> int:
      changes = 0
      l, r = 0, len(sub) - 1
      while l < r:
        if sub[l] != sub[r]:
          changes += 1
        l += 1
        r -= 1
      return changes

    # Precompute cost[i][j]: min changes to make s[i...j] a semi-palindrome
    cost = [[float("inf")] * n for _ in range(n)]

    for i in range(n):
      for j in range(i + 1, n):
        length = j - i + 1
        min_c = float("inf")
        # Find all proper divisors of length
        for d in range(1, length):
          if length % d == 0:
            current_cost = 0
            # Check each of the d groups
            for group_start in range(d):
              group_str = "".join(
                s[k_idx] for k_idx in range(i + group_start, j + 1, d)
              )
              current_cost += min_changes_palindrome(group_str)
            min_c = min(min_c, current_cost)
        cost[i][j] = min_c

    # DP table initialization
    # dp[i][p] -> min changes to partition suffix s[i:] into p parts
    memo = {}

    def dp(i: int, parts: int) -> int:
      if parts == 1:
        if i >= n:
          return float("inf")
        return cost[i][n - 1]

      if i >= n or n - i < parts:
        return float("inf")

      if (i, parts) in memo:
        return memo[(i, parts)]

      res = float("inf")
      # Try ending the current semi-palindrome at index j
      # A semi-palindrome must have length at least 2, and we need to leave enough characters for remaining parts
      for j in range(i + 1, n - parts + 2):
        res = min(res, cost[i][j] + dp(j + 1, parts - 1))

      memo[(i, parts)] = res
      return res

    return dp(0, k)