class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges: 
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        least = None
        queue = deque([(0, 0)])
        seen = [[] for _ in range(n)]
        while queue: 
            t, u = queue.popleft()
            if u == n-1: 
                if least is None: least = t
                elif least < t: return t 
            if (t//change) & 1: t = (t//change+1)*change # waiting for green
            t += time
            for v in graph[u]: 
                if not seen[v] or len(seen[v]) == 1 and seen[v][0] != t: 
                    seen[v].append(t)
                    queue.append((t, v))