from numpy import convolve
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if not n <= target <= n*k: return 0
        MOD = 1000_000_007
        dice =[1]*k
        res = [1]
        for _ in range(n):
            res = convolve(dice, res) % MOD
        return res[target-n+1-1]