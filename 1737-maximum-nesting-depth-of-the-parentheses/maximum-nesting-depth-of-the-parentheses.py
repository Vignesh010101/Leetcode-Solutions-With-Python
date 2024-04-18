class Solution:
    def maxDepth(self, s: str) -> int:
        res=0
        open=0

        for c in s:
            if c=='(':
                open+=1
                res=max(res,open)
            elif c==')':
                open-=1
        
        return res