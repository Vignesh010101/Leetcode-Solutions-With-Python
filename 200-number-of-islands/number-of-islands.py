class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        no_of_islands=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    no_of_islands+=1
                    queue=deque([(i,j)])
                    while queue:
                        x,y=queue.popleft()
                        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='1':
                            grid[x][y]='0'
                            for dx, dy in directions:
                                queue.append((x+dx,y+dy))
        
        return no_of_islands
