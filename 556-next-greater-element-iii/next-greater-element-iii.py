class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=list(str(n))
        i=len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            return -1

        j=len(nums)-1
        while j>i-1 and nums[j]<=nums[i-1]:
            j-=1
        nums[i-1],nums[j]=nums[j],nums[i-1]
        nums[i:]=nums[i:][::-1]
        res=int(''.join(nums))
        return res if res<2**31 else -1