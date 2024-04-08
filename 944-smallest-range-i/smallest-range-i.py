class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        x=max(nums)
        y=min(nums)
        return max(0,(x-k)-(y+k))