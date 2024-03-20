class Solution:
    def rob(self, nums: List[int]) -> int:
        prevhouse=nums[0]
        prevbfrhouse=0
        for i in range(1,len(nums)):
            tmp=prevhouse
            prevhouse=max(prevhouse,prevbfrhouse+nums[i])
            prevbfrhouse=tmp
        
        return prevhouse