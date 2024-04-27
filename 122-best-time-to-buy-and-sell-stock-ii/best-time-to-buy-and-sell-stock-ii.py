class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell=0
        hold=-math.inf

        for prc in prices:
            sell=max(sell,hold+prc)
            hold=max(hold,sell-prc)
        
        return sell
