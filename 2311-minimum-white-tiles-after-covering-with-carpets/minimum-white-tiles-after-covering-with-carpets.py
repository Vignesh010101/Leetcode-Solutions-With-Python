class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
        @cache
        def fn(i, n):
            """Return min while tiles at k with n carpets left."""
            if n < 0: return inf 
            if i >= len(floor): return 0 
            if floor[i] == '1': return min(fn(i+carpetLen, n-1), 1 + fn(i+1, n))
            return fn(i+1, n)
        
        return fn(0, numCarpets)