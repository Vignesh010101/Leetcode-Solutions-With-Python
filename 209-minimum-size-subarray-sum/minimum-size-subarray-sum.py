class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        rslt=math.inf
        sm=0
        j=0

        for i,num in enumerate(nums):
            sm+=num
            while sm>=target:
                rslt=min(rslt,i-j+1)
                sm-=nums[j]
                j+=1

        
        return rslt if rslt!=math.inf else 0