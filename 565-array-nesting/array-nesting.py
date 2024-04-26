class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        if len(nums) == 1:return 1
        v, mx = [False] * len(nums), 1 
        for i in range(len(nums)):
            if not v[i]:
                c = 0
                while not v[i]:
                    v[i] = True
                    c += 1
                    i = nums[i]
                if c > mx:mx = c
                if mx > len(nums) // 2:return mx
        return mx
        