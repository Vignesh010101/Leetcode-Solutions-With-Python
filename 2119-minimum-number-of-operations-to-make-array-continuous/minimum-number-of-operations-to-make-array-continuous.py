class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        qu= deque()
        maxlen=1

        for num in sorted(set(nums)):
            while qu and num-qu[0]>=n:
                qu.popleft()

            qu.append(num)
            maxlen=max(maxlen, len(qu))

        return n-maxlen