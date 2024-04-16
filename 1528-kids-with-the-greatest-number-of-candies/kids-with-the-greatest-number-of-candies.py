class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum =max(candies)
        result=[]
        for i in range(len(candies)):
            total = candies[i] + extraCandies
            result.append(total >= maximum)
        return result
        