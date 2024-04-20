class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        vy=[]
        vy.append(0)
        vy.append(1)
        for i in range(2,n+1):
            if i%2==0:
                vy.append(vy[i//2])
            else:
                vy.append(vy[i//2]+vy[(i//2)+1])
        
        if n==0:
            return 0
        return max(vy)