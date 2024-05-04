

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        maximum=0
        adj=defaultdict(list)
        for i in range(len(times)):
            adj[times[i][0]].append((times[i][1],times[i][2]))
            maximum=max(maximum,times[i][0])

        print(adj)

        q=[]
        times=[sys.maxsize]*n
        
        times[k-1]=0
        heapq.heapify(q)
        heapq.heappush(q,(0,k))

        while q:
            d,u=heapq.heappop(q)
            for v,t in adj[u]:
                if(times[v-1]>times[u-1]+t):
                    times[v-1]=times[u-1]+t
                    heapq.heappush(q,(times[v-1],v))
        print(times)
        return max(times) if sys.maxsize not in times else -1