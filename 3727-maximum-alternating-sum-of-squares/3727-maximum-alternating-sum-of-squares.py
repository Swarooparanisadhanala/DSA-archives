class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Step 1: Square all elements and sort them
        squares = sorted([x * x for x in nums])
        
        # Step 2: Split into smaller half (to subtract) and larger half (to add)
        n = len(squares)
        mid = n // 2
        
        # Elements from index 0 to mid-1 are subtracted
        # Elements from index mid to n-1 are added
        ans = sum(squares[mid:]) - sum(squares[:mid])
        
        return ans