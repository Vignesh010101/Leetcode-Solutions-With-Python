class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = []
        res = []
        dup = sorted(nums)
        vals = {}
        for i in range(n):
            if dup[i] not in vals:
                vals[dup[i]] = i
        for i in range(n):
            res.append(vals[nums[i]])
        return res