class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        while sum(nums)>sum(ans):
            ans.append(nums.pop())
        if sum(nums)==sum(ans):
            ans.append(nums.pop())
        return ans