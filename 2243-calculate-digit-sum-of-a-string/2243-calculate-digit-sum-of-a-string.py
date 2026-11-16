class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Repeat the process as long as the string length is greater than k
        while len(s) > k:
            next_round = []
            
            # Step 1 & 2: Divide into groups of size k and calculate their digit sums
            for i in range(0, len(s), k):
                group = s[i:i + k]
                digit_sum = sum(int(char) for char in group)
                next_round.append(str(digit_sum))
            
            # Step 3: Merge consecutive groups together to form the new string
            s = "".join(next_round)
            
        return s