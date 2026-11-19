class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        return min(
            nums[-1] - nums[2],  # Drop 2 smallest
            nums[-2] - nums[1],  # Drop 1 smallest, 1 largest
            nums[-3] - nums[0],  # Drop 2 largest
        )