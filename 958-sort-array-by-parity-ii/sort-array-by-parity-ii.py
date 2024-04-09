class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evn=[]
        od=[]
        lst=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                evn.append(nums[i])
            else:
                od.append(nums[i])

        for i in range(len(evn)):
            lst.append(evn[i])
            lst.append(od[i])
        return lst