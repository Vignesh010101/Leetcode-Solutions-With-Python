class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s=defaultdict(int)
        cnt=0
        for a in [0] + list(accumulate(nums)):
            cnt+=s[a-k]
            s[a]+=1

        return cnt