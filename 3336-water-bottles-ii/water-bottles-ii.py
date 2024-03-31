class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        rest=numBottles

        temp=rest
        while temp>=numExchange:
            rest+=1
            temp-=numExchange
            temp+=1
            numExchange+=1
        
        return rest
solution=Solution()
print(solution.maxBottlesDrunk(9,3))