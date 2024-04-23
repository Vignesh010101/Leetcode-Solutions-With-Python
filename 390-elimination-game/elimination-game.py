class Solution:
    def lastRemaining(self, n: int) -> int:
        mask = 1
        while mask <= n:  # left shift mask until mask > n
            mask <<= 1
        mask = (mask >> 1) - 1  # we don't want the left most bit
        return 1 + ((n | 0x55555555) & mask)  # fill all odd bits and apply the mask