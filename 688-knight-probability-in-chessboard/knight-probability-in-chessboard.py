class Solution:
    def dp(self,x,y,n,visited,k):
        if k<0:
            return 1
        if (x<0 or x>=n) or (y<0 or y>=n):
            return 0
        if (x,y,k) in visited:
            return visited[(x,y,k)]
        a=self.dp(x+2,y+1,n,visited,k-1)*1/8
        b=self.dp(x+2,y-1,n,visited,k-1)*1/8
        c=self.dp(x-2,y+1,n,visited,k-1)*1/8
        d=self.dp(x-2,y-1,n,visited,k-1)*1/8
        e=self.dp(x+1,y+2,n,visited,k-1)*1/8
        f=self.dp(x+1,y-2,n,visited,k-1)*1/8
        g=self.dp(x-1,y+2,n,visited,k-1)*1/8
        h=self.dp(x-1,y-2,n,visited,k-1)*1/8
        visited[(x,y,k)]=a+b+c+d+e+f+g+h
        return a+b+c+d+e+f+g+h
        
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        return self.dp(row,column,n,{},k)