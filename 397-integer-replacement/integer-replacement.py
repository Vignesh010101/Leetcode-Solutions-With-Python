class Solution:
    def integerReplacement(self, n: int) -> int:
        dp={}
        dp[0]=0
        dp[1]=0
        moves=0
        def recur(n):
            if n in dp:
                return dp[n]
            if n%2==0:
                dp[n]=1+recur(n//2)
            else:
                dp[n]=1+min(recur(n-1),recur(n+1))
            return dp[n]
        return recur(n)