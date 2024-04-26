from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def score_diff(lo, hi):
            if lo == hi:
                return nums[lo]

            return max(nums[lo]-score_diff(lo+1, hi), nums[hi]-score_diff(lo, hi-1))

        return score_diff(0, len(nums)-1) >= 0