class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy=float(-inf)
        sell=0
        
        for prc in prices:
            buy=max(buy,sell-prc)
            sell=max(sell,buy+prc-fee)

        return sell