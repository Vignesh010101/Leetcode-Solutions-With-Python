class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allCaps = False

        for i in word:
            if ord(i)<=90:
                allCaps =True
            else:
                allCaps = False
                break
        if allCaps:
            return True

        for i in range(1, len(word)):
            if ord(word[i])<97:
                return False

        
        return True