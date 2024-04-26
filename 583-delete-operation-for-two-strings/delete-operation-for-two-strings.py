class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pattern_dict = {}
        for i,l in enumerate(word2):
            if l in pattern_dict:
                pattern_dict[l].append(i)
            else:
                pattern_dict[l] = [i]
                
        n = max(len(word1),len(word2))
        dp = [n+1] * (n+1)
        for l in word1:
            if l not in pattern_dict:
                continue
            for i in reversed(pattern_dict[l]):
                index = bisect.bisect_left(dp,i)
                dp[index] = i
        return len(word1)+len(word2)-2*bisect.bisect_left(dp,n+1)