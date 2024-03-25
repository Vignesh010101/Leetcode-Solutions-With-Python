class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        rslt=[]
        for num in nums:
            nums[abs(num)-1]*=-1
            if nums[abs(num)-1]>0:
                rslt.append(abs(num))

        return rslt