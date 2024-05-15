from heapq import heappush, heappop

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        adj = [[] for i in range(n)]
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        inf = 10**18
        track = [[inf, inf] for i in range(n)]

        track[0] = [0, passingFees[0]]
        heap = [(passingFees[0], 0, 0)]

        while heap:
            fee, time, u = heappop(heap)
            if track[u][0] > fee:
                track[u][0] = fee
                track[u][1] = time
            elif track[u][1] > time:
                track[u][0] = fee
                track[u][1] = time
            else:
                continue
            
            if u == n-1:
                return fee
            
            for v, w in adj[u]:
                if time + w <= maxTime and (time+w < track[v][1] or fee+passingFees[v] < track[v][0]):
                    heappush(heap, (fee+passingFees[v], time+w, v))
        return -1
            
            






        