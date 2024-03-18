class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        rslt=0
        arw=-math.inf
        for pnt in sorted(points, key=lambda x:x[1]):
            if pnt[0]>arw:
                rslt+=1
                arw=pnt[1]
        
        return rslt