class Solution:
    def reverseBits(self, n: int) -> int:
        rslt=0

        for i in range(32):
            if n>>i&1:
                rslt|=1<<31-i
        
        return rslt