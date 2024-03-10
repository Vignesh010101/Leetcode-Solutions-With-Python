class Solution:
    def numTrees(self, n: int) -> int:
        rslt=[1,1]+[0]*(n-1)

        for i in range(2,n+1):
            for j in range(i):
                rslt[i]=rslt[i]+rslt[j]*rslt[i-j-1]
            
        return rslt[n]