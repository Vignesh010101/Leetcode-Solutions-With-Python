class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hghtsorted=sorted(heights)
        cnt=0
        for i in range(len(heights)):
            if hghtsorted[i]!=heights[i]:
                cnt+=1
        
        return cnt