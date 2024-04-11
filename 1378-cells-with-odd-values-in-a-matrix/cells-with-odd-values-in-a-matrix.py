class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows,cols = [0]*m,[0]*n
    
        for r,c in indices: rows[r] += 1; cols[c] += 1
        
        return sum(
            1
            for r in rows
            for c in cols
            if (r + c) % 2
        )
        