class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        start,end = -1, -1
        res = 0
        for i in range(len(nums)):
            if nums[i] > right:
                start = end = i
                continue
                
            if nums[i] >= left:
                end = i
                
            res += end - start
        return res