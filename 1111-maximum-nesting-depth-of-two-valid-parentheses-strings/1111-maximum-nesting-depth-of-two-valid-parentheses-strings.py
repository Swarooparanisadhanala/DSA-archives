class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        depth = 0
        for char in seq:
            if char == '(':
                depth += 1
                res.append(depth % 2)
            else:
                res.append(depth % 2)
                depth -= 1
        return res     