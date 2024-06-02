class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = inf
        
        # -1 in binary is '111111111'
        current = -1

        n = len(nums)
        left = 0
        count = Counter()
        
        for right in range(n):

            current &= nums[right]

            for idx in range(30):
                b = (nums[right] >> idx) & 1
                # record the bit count in each position
                if b:
                    count[idx] += 1
            
            # update the result
            res = min(res, abs(k - current))
            
            # AND values will decrease to 0 when the size of the subarray increase
            # if the current subarray AND is < k, we shrink the subarray
            while current < k:
                for idx in range(30):
                    b = (nums[left] >> idx) & 1
                    if b:
                        count[idx] -= 1
                    
                    # if the current subarray has all '1' in current bit, we need to set back the AND of current bit
                    # current subarray nums[left + 1: right + 1]
                    # length == right - left
                    if count[idx] == right - left:
                        current |= (1 << idx)
                # update the result
                res = min(res, abs(k - current))
                left += 1
                
        return res