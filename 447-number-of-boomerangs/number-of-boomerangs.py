class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans=0
        for x1, y1 in points:
            dist=[(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)   for x2, y2 in points ]
            count=collections.Counter(dist)
            for c in count.values():
                ans+=c*(c-1)
        return ans