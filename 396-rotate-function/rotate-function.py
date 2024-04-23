class Solution(object):
    def maxRotateFunction(self, nums: List[int])-> int: 
        s=sum(nums)

        d=sum(elem * idx for idx, elem in enumerate(nums)) #first find our number 1: dynamic programming solution
        sol = d
        for pivot in range(len(nums)-1,-1,-1): # pivot: we move backwards
            d+=s-len(nums)*nums[pivot] # get next d value
            sol=max(d,sol)
        return sol
        