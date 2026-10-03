class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # Stack keeps track of indices. 
        # Initialize with -1 as a base index for boundary length calculations.
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current ')' is unmatched; store its index as the new base
                    stack.append(i)
                else:
                    # Length of current valid substring is (current_index - last_unmatched_index)
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len