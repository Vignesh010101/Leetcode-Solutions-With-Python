class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(sequence)<len(word):
            return 0
        
        v=1
        ans=0

        while v*word in sequence:
            ans+=1
            v+=1

        return ans
