class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        fianlly_xor=0

        for v in nums:
            fianlly_xor=fianlly_xor^v

        cnt=0
        while k or fianlly_xor:
            if (k%2)!=(fianlly_xor%2):
                cnt+=1
            
            k//=2
            fianlly_xor//=2
        
        return cnt
        
