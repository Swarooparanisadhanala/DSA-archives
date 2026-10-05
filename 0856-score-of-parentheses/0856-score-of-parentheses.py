class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Base score at level 0
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # If v == 0, it was "()", score is 1.
                # Otherwise, it was "(A)", score is 2 * v.
                stack[-1] += max(2 * v, 1)
                
        return stack[0]