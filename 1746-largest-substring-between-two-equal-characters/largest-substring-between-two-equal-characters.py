class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n=len(s)
        alpha=[-1]*26 #initial position for every letter
        maxLen=-1 
        for i, c in enumerate(s):
            if alpha[ord(c)-ord('a')]!=-1: # letter c already found
                maxLen =max(maxLen, i-alpha[ord(c)-ord('a')]-1)
            else: # first found for the letter c
               alpha[ord(c)-ord('a')]=i
        return maxLen 
        