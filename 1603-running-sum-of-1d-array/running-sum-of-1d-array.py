class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            runsum=0
            for j in range(i+1):
                runsum+=nums[j]
            ans.append(runsum)
        return ans