class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        N = len(nums)
        diffs = []
        sl, sr = 0, sum(nums)
        for i in range(N - 1):
            sl += nums[i]
            sr -= nums[i]
            diffs.append(sl - sr)
        diffs.append(math.inf)
        
        cl, cr = Counter(), Counter(diffs)
        res = cl[0] + cr[0]
        for i in range(N):
            d = k - nums[i]
            res = max(res, cl[d] + cr[-d])
            cl[diffs[i]] += 1
            cr[diffs[i]] -= 1
        return res