class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        cnt=0
        j=0

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                j=i

            cnt+=i-j+1
        
        return cnt
solution=Solution()