class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_1=0
        hold_1=-math.inf

        for price in prices:
            sell_1=max(sell_1,hold_1+price)
            hold_1=max(hold_1,-price)
        return sell_1
