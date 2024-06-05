class Solution:
    def distinctSequences(self, n: int) -> int:
        
        @lru_cache
        def fn(n, p0, p1): 
            """Return total number of distinct sequences."""
            if n == 0: return 1
            ans = 0
            for x in range(1, 7): 
                if x not in (p0, p1) and gcd(x, p0) == 1: ans += fn(n-1, x, p0)
            return ans % 1_000_000_007
        
        return fn(n, -1, -1)