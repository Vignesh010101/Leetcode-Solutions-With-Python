class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort=sorted(nums)
        start=0
        end=len(nums)-1
        if sort==nums or len(nums)==1:
            return 0

        for x in range(len(nums)):
            if nums[start]==sort[start]:
                start+=1
            if nums[end]==sort[end]:
                end-=1
            if start==end:
                return 0
        
        return end-start+1