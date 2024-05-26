class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        ans = 0
        n = len(favorite)
        cycles_of_2 = []
        seen = [False for _ in range(n)]
        for node in range(n):
            if seen[node]:
                continue
            if favorite[favorite[node]] == node:
                cycles_of_2.append((node, favorite[node]))
                seen[node] = True
                seen[favorite[node]] = True
        for node in range(n):
            if seen[node]:
                continue
            cycle_length = self.find_cycle(node, 1, {}, seen, favorite)
            ans = max(ans, cycle_length)
        
        if len(cycles_of_2) != 0:
            revfavorite = defaultdict(list)
            for node, fav in enumerate(favorite):
                if favorite[fav] != node:
                    revfavorite[fav].append(node)
            total_tail = 0
            for x, y in cycles_of_2:
                max_tail = self.max_depth(x, revfavorite) + self.max_depth(y, revfavorite)
                total_tail += max_tail
            ans = max(ans, 2 * len(cycles_of_2) + total_tail)
        return ans

    def find_cycle(self, node, length, path, seen, favorite):
        if seen[node]:
            return -1
        seen[node] = True
        path[node] = length
        if favorite[node] in path:
            return path[node] - path[favorite[node]] + 1
        return self.find_cycle(favorite[node], length+1, path, seen, favorite)
    
    def max_depth(self, node, graph, depth=0):
        res = depth
        for neigh in graph[node]:
            res = max(res, self.max_depth(neigh, graph, depth+1))
        return res