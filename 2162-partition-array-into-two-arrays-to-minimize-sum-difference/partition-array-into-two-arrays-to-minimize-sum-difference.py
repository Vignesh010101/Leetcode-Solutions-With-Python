from itertools import chain, combinations, pairwise
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        h, ss, nums = len(nums)//2, 4*sum(nums), sorted(8*n for n in nums)
        four_ret = min(
            abs(x1 - x2)
            for i in range(h+1)
            for x1, x2 in pairwise(sorted(chain(
                map(sum, combinations(nums[h:], h-i)),
                (ss-sum(l)+1 for l in combinations(nums[:h], i)),
            )))
            if x1%2 != x2%2
        )
        return (four_ret + four_ret % 4 - 2)//4