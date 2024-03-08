class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt=collections.Counter(nums)
        maxfrq=max(cnt.values())
        return sum(frq==maxfrq for frq in cnt.values())*maxfrq