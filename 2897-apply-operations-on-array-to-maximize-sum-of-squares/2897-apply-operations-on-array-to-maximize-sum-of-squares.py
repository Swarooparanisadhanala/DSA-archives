class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        
        # Count the frequency of each bit across all numbers
        for num in nums:
            for b in range(31):
                if (num >> b) & 1:
                    bit_counts[b] += 1
                    
        # Reconstruct the k largest possible numbers greedily
        chosen_nums = [0] * k
        for b in range(31):
            for i in range(min(bit_counts[b], k)):
                chosen_nums[i] |= (1 << b)
                
        # Calculate the sum of squares modulo 10^9 + 7
        ans = 0
        for num in chosen_nums:
            ans = (ans + num * num) % MOD
            
        return ans