class Solution:
    def isPathCrossing(self, path: str) -> bool:
        P=set()
        P.add((0, 0))
        x, y= 0, 0
        for c in path:
            if c=='N': y+=1
            elif c=='S': y-=1
            elif c=='E': x+=1
            else: x-=1
            if (x, y) in P : return True
            P.add((x, y))
        return False