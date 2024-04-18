class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    m=len(grid)
    n=len(grid[0])

    islands=0
    nghbrs=0

    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                islands+=1
                if i+1<m and grid[i+1][j]==1:
                    nghbrs+=1
                if j+1<n and grid[i][j+1]==1:
                    nghbrs+=1
    
    return islands * 4 - nghbrs * 2
