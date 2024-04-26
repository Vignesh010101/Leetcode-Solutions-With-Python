class Solution:
    def __init__(self):
        self.lst=[]

    def fn(self,i,j,nums,lst,n):
        if i==n:
            return
        if j==-1 or nums[j]<=nums[i]:
            self.fn(i+1,i,nums,lst+[nums[i]],n)
            if len(lst)>=1 and lst+[nums[i]] not in self.lst:
                self.lst.append(lst+[nums[i]])
        self.fn(i+1,j,nums,lst,n)
        return

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        self.fn(0,-1,nums,[],n)
        return self.lst