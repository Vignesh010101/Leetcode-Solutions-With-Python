class Solution:
    def getMoneyAmount(self, n: int) -> int:
               
        @cache
        def dfs(l,r):
            if r-l == 4 : return 2*l + 4
            if r-l == 3 : return 2*l + 2
            if r-l == 2 : return l + 1
            if r-l == 1 : return l
            
            return min((m + max(dfs(l,m-1), dfs(m+1,r)) for m in range(r-3,l,-4)), default=0)

        if n <= 2 : return n-1
        if n == 3 : return 2
        
        return dfs(1,n)