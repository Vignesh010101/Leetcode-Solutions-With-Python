class Solution: #Dijkstra's Algorithm
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)

        for x,y,t in meetings:
            graph[x].append((y,t))
            graph[y].append((x,t))

        heap = [(0,firstPerson)] #time,person
        for nei,time in graph[0]:
            heapq.heappush(heap,(time,nei))
        
        visited = set([0])

        while heap:
            time,person = heapq.heappop(heap)

            if person in visited:
                continue

            visited.add(person)

            for nei,t in graph[person]:
                if t>=time:
                    heapq.heappush(heap,(t,nei))

        return visited