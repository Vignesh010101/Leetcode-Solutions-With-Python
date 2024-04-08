class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck)
        cv = list(counts.values())
        l = len(cv)
        if 1 in cv :
            return False
        for i in range(l-1) :
            for j in range(1+i, l) :
                if gcd(cv[i], cv[j]) == 1 :
                    return False
        return True