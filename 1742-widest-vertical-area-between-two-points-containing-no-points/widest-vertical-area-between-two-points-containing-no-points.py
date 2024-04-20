class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        n=len(points)
        ans=0
        for i in range(1,n):
            ans=max(ans,(points[i][0]-points[i-1][0]))
        return ans    
        