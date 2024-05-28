class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        pp = pow(power, k-1, modulo)
        hs = ii = 0 
        for i, ch in enumerate(reversed(s)): 
            if i >= k: hs -= (ord(s[~(i-k)]) - 96)*pp
            hs = (hs * power + (ord(ch) - 96)) % modulo
            if i >= k-1 and hs == hashValue: ii = i 
        return s[~ii:~ii+k or None]