class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ttl=0

        for i,x in enumerate(tickets):
            if i<=k:
                ttl+=min(tickets[i],tickets[k])
            else:
                ttl+=min(tickets[i],tickets[k]-1)
        
        return ttl