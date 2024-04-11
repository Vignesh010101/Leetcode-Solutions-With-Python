class Solution:
    def balancedStringSplit(self, s: str) -> int:
        s = s.replace("R", "-1,").replace("L", "1,")
        ls = list(map(lambda x : 1 if x == "1" else -1, s[:-1].split(",")))
        c = 0
        k = 0
        for i in ls :
            if k == 0 :
                c += 1
            k += i
        return c