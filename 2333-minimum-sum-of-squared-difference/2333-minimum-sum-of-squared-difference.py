class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        # Step 1: Compute absolute differences and store frequencies
        max_diff = 0
        count = [0] * 100001
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            count[d] += 1
            if d > max_diff:
                max_diff = d
                
        # Step 2: Greedily reduce the largest differences
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
            
            # Number of operations needed to bring these differences down to d - 1
            # We can use at most `total_k` operations
            ops = min(total_k, count[d])
            
            count[d] -= ops
            count[d - 1] += ops
            total_k -= ops
            
            if total_k == 0:
                break
                
        # Step 3: Calculate the minimum sum of squared differences
        ans = 0
        for d in range(1, len(count)):
            if count[d] > 0:
                ans += count[d] * (d ** 2)
                
        return ans