class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        oddsCount = 0
        evensCount = 0
        for n in position:
            if n % 2 == 0:
                evensCount +=1
            else:
                oddsCount += 1
        return min(oddsCount, evensCount)