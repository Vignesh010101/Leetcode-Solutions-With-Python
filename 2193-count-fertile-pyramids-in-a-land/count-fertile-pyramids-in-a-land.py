class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        
        def count(grid):
            m, n = len(grid), len(grid[0])
            degree = [[0 for _ in range(n)] for _ in range(m)]
            for x in range(1, m):
                for y in range(1, n-1):
                    if grid[x][y] == grid[x-1][y-1] == grid[x-1][y] == grid[x-1][y+1] == 1:
                        degree[x][y] = 1 + min(degree[x-1][y-1], degree[x-1][y], degree[x-1][y+1])
                        
            return sum(sum(row) for row in degree)
        
        return count(grid) + count(grid[::-1])       