class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left = len(cells) 
        right = left + 1
        parent = list(range(right + 1))
        rank = [0] * (right + 1)
        directions = [(i, j) for i in (0, -1, 1) for j in (0, -1, 1)][1:]

        def find(x):
            while parent[x] != x:
                x, parent[x] = parent[x], parent[parent[x]]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return
            if rank[y] > rank[x]:
                x, y = y, x
            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

        water = {} 
        for idx, (i, j) in enumerate(cells):
            i -= 1
            j -= 1
            water[(i, j)] = idx
            if j == 0:
                union(left, idx)
            if j == col - 1:
                union(right, idx)
            for di, dj in directions:
                i2, j2 = i + di, j + dj
                if (i2, j2) in water:
                    union(water[(i2, j2)], idx)
            if find(left) == find(right):
                return idx 
        return idx + 1 