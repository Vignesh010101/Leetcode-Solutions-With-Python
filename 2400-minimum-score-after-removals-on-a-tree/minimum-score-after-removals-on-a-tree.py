class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        children = [set() for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        for i in range(n):
            if len(g[i]) != 1: root = i
        prefix_xor = [nums[i] for i in range(n)]
        visited = [0 for _ in range(n)]
        def dfs(node: int) -> None:
            visited[node] = 1
            for nxt in g[node]:
                if visited[nxt]: continue
                dfs(nxt)
                children[node].add(nxt)
                children[node] |= children[nxt]
                prefix_xor[node] ^= prefix_xor[nxt]

        dfs(root)
        res = float("inf")
        for i in range(1, n - 1):
            for j in range(i):
                [a, b], [c, d] = edges[i], edges[j]
                if b in children[a]: a, b = b, a
                if d in children[c]: c, d = d, c
                if c in children[a]: cur_xors = [prefix_xor[c], prefix_xor[a] ^ prefix_xor[c], prefix_xor[root] ^ prefix_xor[a]]
                elif a in children[c]: cur_xors = [prefix_xor[a], prefix_xor[a] ^ prefix_xor[c], prefix_xor[root] ^ prefix_xor[c]]
                else: cur_xors = [prefix_xor[a], prefix_xor[c], prefix_xor[root] ^ prefix_xor[a] ^ prefix_xor[c]]
                res = min(res, max(cur_xors) - min(cur_xors))

        return res