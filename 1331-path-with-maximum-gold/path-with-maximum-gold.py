class Solution:
    rows=[1,-1,0,0]
    cols=[0,0,-1,1]

    def dfs(self,grid,x,y,m,n):
        if x<0 or x>=m or y<0 or y>=n or grid[x][y]==0:
            return 0

        curr=grid[x][y]
        grid[x][y]=0
        maxi_gold=curr

        for i in range(4):
            xnew=x+self.rows[i]
            ynew=y+self.cols[i]
            maxi_gold=max(maxi_gold,curr+self.dfs(grid,xnew,ynew,m,n))

        grid[x][y]=curr
        return maxi_gold

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        maxgold=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    maxgold=max(maxgold,self.dfs(grid,i,j,m,n))

        return maxgold
        