class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #consider indeg & outdeg
        trusting=[0]*(n+1)
        trusted=[0]*(n+1)
        for e in trust:
            trusting[e[0]]+=1 #outdeg
            trusted[e[1]]+=1 #indeg
        for i in range(1, n+1):
            if trusting[i]==0 and trusted[i]==n-1:
                return i
        return -1
        
        