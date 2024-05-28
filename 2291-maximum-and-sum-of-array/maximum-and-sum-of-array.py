class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        
        @cache
        def fn(k, m): 
            if k == len(nums): return 0 
            ans = 0 
            for i in range(numSlots): 
                if m & 1<<2*i == 0 or m & 1<<2*i+1 == 0: 
                    if m & 1<<2*i == 0: mm = m ^ 1<<2*i
                    else: mm = m ^ 1<<2*i+1
                    ans = max(ans, (nums[k] & i+1) + fn(k+1, mm))
            return ans 
        
        return fn(0, 0)