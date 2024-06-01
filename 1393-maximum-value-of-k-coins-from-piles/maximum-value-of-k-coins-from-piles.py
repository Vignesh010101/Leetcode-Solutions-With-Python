class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @lru_cache(None)
        def dfs(coins, moves):
            if len(piles) == coins: return 0

            ans, curr, pile = dfs(coins+1, moves), 0, piles[coins]

            for j in range(min(len(pile), moves)):
                curr += pile[j]
                ans = max(ans, curr + dfs(coins+1, moves-j-1))

            return ans
        
        return dfs(0,k)