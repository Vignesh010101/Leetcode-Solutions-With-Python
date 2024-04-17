class Solution:
    def countOdds(self, low: int, high: int) -> int:
        od=(high-low)//2
        if low%2==1 or high%2==1:
            od+=1
        return od