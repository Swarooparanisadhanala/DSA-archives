
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        pref = [0] * n
        timer = 0

        # Iterative DFS
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                tin[u] = timer
                timer += 1
                up[0][u] = u if p == -1 else p
                pref[u] = (pref[p] if p != -1 else 0) ^ (1 << (ord(s[u]) - 97))
                for k in range(1, LOG):
                    up[k][u] = up[k - 1][up[k - 1][u]]
                stack.append((u, p, 1))
                for v in reversed(g[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            d = depth[u] - depth[v]
            for k in range(LOG):
                if d & (1 << k):
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u, v = up[k][u], up[k][v]
            return up[0][u]

        bit = [0] * (n + 2)

        def update(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def prefix(i):
            res = 0
            i += 1
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def change_subtree(u, val):
            update(tin[u], val)
            update(tout[u] + 1, val)

        chars = list(s)
        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u, c = int(parts[1]), parts[2]
                delta = (1 << (ord(chars[u]) - 97)) ^ (1 << (ord(c) - 97))
                if delta:
                    change_subtree(u, delta)
                    chars[u] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                mask = (
                    pref[u] ^ prefix(tin[u])
                    ^ pref[v] ^ prefix(tin[v])
                    ^ (1 << (ord(chars[w]) - 97))
                )
                ans.append(mask & (mask - 1) == 0)

        return ans
