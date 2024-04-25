class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)
        dp[(0,0)] = 0
        ans = 0

        for s in strs:
            zero,one = s.count('0'),s.count('1')
            nextDp = dp.copy()
            for key,val in dp.items():
                countZero,countOne = zero+key[0],one+key[1]
                if countZero<=m and countOne<=n:
                    nextDp[(countZero,countOne)] = max(nextDp[(countZero,countOne)],1+val)
                    ans = max(ans,nextDp[(countZero,countOne)])
            dp = nextDp

        return ans