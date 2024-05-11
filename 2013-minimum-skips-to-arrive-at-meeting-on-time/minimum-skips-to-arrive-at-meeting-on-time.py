class Solution:
    def minSkips(self, dist: List[int], speed: int, time: int) -> int:
        """
        dp(n , k) calculates minimum time required 
        to cross n first roads with k available skips
        """
        @lru_cache(None)
        def dp(n, skips):
            if skips < 0: return inf
            if n <= 0: return 0
            if n == len(dist):
                return dp(n - 1, skips) + dist[n - 1]
            skip = dp(n - 1, skips - 1) + dist[n - 1]
            noskip = ((dp(n - 1, skips) + dist[n - 1] + speed - 1) // speed) * speed 
            return min(skip, noskip)

        n = len(dist)
        for i in range(n):
            if dp(n , i) <= speed * time: return i
        return -1