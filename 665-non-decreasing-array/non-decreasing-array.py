class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt=0
        v=len(nums)
        for i in range(1,v):
            if nums[i]<nums[i-1]:
                cnt+=1
                if cnt>1:
                    return False
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]

        return True