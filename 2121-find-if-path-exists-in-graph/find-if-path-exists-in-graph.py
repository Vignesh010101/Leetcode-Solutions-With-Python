class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        queue=deque([source])
        visited=set([source])

        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            for adjacent in graph[node]:
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(adjacent)
        
        return False