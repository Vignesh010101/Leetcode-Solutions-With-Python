class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        
        minx=min(c[0] for c in ops)
        miny=min(c[1] for c in ops)

        return minx*miny