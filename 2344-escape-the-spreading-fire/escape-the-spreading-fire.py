class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fire = deque([])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    grid[r][c] = -1
                    fire.append((r,c))
        while fire:
            x, y = fire.popleft()
            t = grid[x][y]
            for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
                a, b = dx+x, dy+y
                if 0<=a<row and 0<=b<col and grid[a][b] == 0:
                    grid[a][b] = t - 1
                    fire.append((a,b))
        ans = []
        q = deque([(0,0,10**9)])
        t = 1
        seen = set([(0,0)])
        while q:
            t += 1
            for _ in range(len(q)):
                x, y, wait = q.popleft()
                for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
                    a, b = dx+x, dy+y
                    if 0<=a<row and 0<=b<col and (a,b) not in seen:
                        if a==row-1 and b==col-1:
                            if grid[a][b] == 0:
                                ans.append(wait)
                            elif t <= -grid[a][b]:
                                new = -grid[a][b] - t
                                low = new if new < wait else wait                                
                                ans.append(low)
                        elif grid[a][b] == 0:
                            seen.add((a,b))
                            q.append((a,b,wait))
                        elif t < -grid[a][b]:
                            seen.add((a,b))
                            new = -grid[a][b] - t - 1
                            low = new if new < wait else wait
                            q.append((a,b,low))
        return max(ans) if ans else -1