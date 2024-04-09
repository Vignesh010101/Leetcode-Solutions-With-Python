class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        cs = list(accumulate(arr))
        try:
            i1 = cs.index(cs[-1] // 3)
            i2 = cs.index(2 * cs[-1] // 3, i1 + 1, len(arr) - 1)
            return cs[-1] % 3 == 0
        except ValueError:
            return False