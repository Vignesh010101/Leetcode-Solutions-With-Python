class Solution:
    def maxPower(self, s: str) -> int:
        mx = 1
        cache = []
        prev = ""
        for c in range(len(s)) :

            if s[c] == prev :
                mx += 1
                if c == len(s) - 1 :
                    cache.append(mx)
            else :
                cache.append(mx)
                mx = 1
            prev = s[c]
        return max(cache)