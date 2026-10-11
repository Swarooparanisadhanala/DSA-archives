class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        # 1-indexed loop from 1 to n
        for i in range(1, n + 1):
            if n % i == 0:
                # nums is 0-indexed, so we use nums[i - 1]
                total_sum += nums[i - 1] ** 2
                
        return total_sum