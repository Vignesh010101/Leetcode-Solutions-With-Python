class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = [[] for _ in values]
        for u, v, t in edges: 
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        ans = 0 
        stack = [(0, values[0], 0, 1)]
        while stack: 
            time, val, u, mask = stack.pop()
            if u == 0: ans = max(ans, val)
            for v, t in graph[u]: 
                if time + t <= maxTime: 
                    if not mask & 1<<v: stack.append((time+t, val+values[v], v, mask ^ 1<<v))
                    else: stack.append((time+t, val, v, mask))
        return ans 