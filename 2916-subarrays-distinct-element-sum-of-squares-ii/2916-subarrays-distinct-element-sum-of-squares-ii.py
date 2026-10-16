class Node:
    def __init__(self):
        self.count_total = 0
        self.sq_total = 0
        self.lazy = 0
        self.left = None
        self.right = None

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        root = Node()
        
        def push(tleft, tright, node):
            if node.left is None:
                node.left = Node()
            if node.right is None:
                node.right = Node()
                
            if node.lazy != 0:
                L = tright - tleft + 1
                val = node.lazy
                new_sq_total = (node.sq_total + 2 * val * node.count_total + L * val * val) % MOD
                new_count_total = (node.count_total + L * val) % MOD
                
                node.sq_total = new_sq_total
                node.count_total = new_count_total
                
                if tleft != tright:
                    node.left.lazy += val
                    node.right.lazy += val
                node.lazy = 0

        def update(tleft, tright, node, ql, qr):
            push(tleft, tright, node)
            if qr < tleft or tright < ql:
                return
            if ql <= tleft and tright <= qr:
                node.lazy += 1
                push(tleft, tright, node)
                return
            
            mid = (tleft + tright) // 2
            update(tleft, mid, node.left, ql, qr)
            update(mid + 1, tright, node.right, ql, qr)
            
            node.count_total = (node.left.count_total + node.right.count_total) % MOD
            node.sq_total = (node.left.sq_total + node.right.sq_total) % MOD

        ans = 0
        num2lasti = {}
        
        for i, num in enumerate(nums):
            lasti = num2lasti.get(num, -1)
            update(0, n - 1, root, lasti + 1, i)
            num2lasti[num] = i
            ans = (ans + root.sq_total) % MOD
            
        return ans