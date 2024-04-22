class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = 0
        curr = 0
        
        for i in range(len(nums) - 1):
            if curr == 0 and nums[i + 1] - nums[i] != 0:
                length += 1
                curr = nums[i + 1] - nums[i]
                
            if curr < 0 and nums[i + 1] - nums[i] > 0:
                length += 1
                curr = nums[i + 1] - nums[i]
                
            elif curr > 0 and nums[i + 1] - nums[i] < 0:
                length += 1
                curr = nums[i + 1] - nums[i]
                
            else:
                continue
                
        return length + 1