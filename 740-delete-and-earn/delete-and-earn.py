class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        list1=[0]*10001
        for i in nums:
            list1[i]+=i
        rob1,rob2=0,0
        for n in list1:
            rob1,rob2,=rob2,max(rob1+n,rob2)
        return rob2