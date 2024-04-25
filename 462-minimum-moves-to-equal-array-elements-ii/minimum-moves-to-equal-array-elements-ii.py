class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]            
        count = 0        
        for n in nums:
            if n == median:
                continue
            count += abs(n - median)
        return count