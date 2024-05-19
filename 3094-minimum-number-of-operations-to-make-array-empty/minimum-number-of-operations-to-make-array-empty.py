class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return max(sum(ceil(v/3) if v>1 else -inf for v in Counter(nums).values()),-1)