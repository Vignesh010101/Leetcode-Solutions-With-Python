class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        reaching=0

        while i<len(nums) and i<=reaching:
            reaching=max(reaching, i+nums[i])
            i+=1
        
        return i==len(nums)