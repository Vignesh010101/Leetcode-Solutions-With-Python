class Solution:
    def makesquare(self, arr: List[int]) -> bool:
		# no way to make the square if total length not divisble by 4
        if sum(arr) % 4:
            return False
        
		# target side length
        side = sum(arr) // 4
        
        @lru_cache(None)
        def dp(k, mask, s):
			# finish all four sides
            if k == 4:
                return True
			# move on to next side if current one finished
            if not s:
                return dp(k+1, mask, side)
            
            for i in range(len(arr)):
				# if current matchstick used or longer than remaining side length to fill then skip
                if mask & (1 << i) or s < arr[i]: continue
                if dp(k, mask ^ (1 << i), s - arr[i]):
                    return True
            return False
        
        return dp(0, 0, side)