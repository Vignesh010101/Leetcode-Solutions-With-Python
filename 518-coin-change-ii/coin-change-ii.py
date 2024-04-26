class Solution:
    def dp(self,i,coins,tr,dct):
        if tr==0:
            return 1
        if i==0:
            if tr%coins[0]==0:
                return 1
            return 0
        if (i,tr) in dct:
            return dct[(i,tr)]
        x=0
        if coins[i]<=tr:
            x=self.dp(i,coins,tr-coins[i],dct)
        y=self.dp(i-1,coins,tr,dct)
        dct[(i,tr)]=x+y
        return dct[(i,tr)]

    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        # dp=[[0]*(amount+1) for i in range(n)]
        prev=[0]*(amount+1)
        # for i in range(n):
        #     dp[i][0]=1
        prev[0]=1
        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i]=1
        for i in range(1,n):
            curr=[0]*(amount+1)
            curr[0]=1
            for j in range(amount+1):
                x=0
                if j>=coins[i]:
                    x=curr[j-coins[i]]
                y=prev[j]
                curr[j]=x+y
            prev=curr
        return prev[amount]