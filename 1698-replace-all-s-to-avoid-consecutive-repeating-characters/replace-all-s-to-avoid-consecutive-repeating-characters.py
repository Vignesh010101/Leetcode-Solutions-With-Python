class Solution:
    def modifyString(self, s: str) -> str:
        l = len(s)
        if l == 1 :
            return "a"
        while "?" in s :
            idx = s.index("?")
            if 0 < idx < l - 1:
                canbe = list(filter(lambda x : x != s[idx + 1] and x != s[idx - 1], list("abc")))[0]
                s = s.replace("?", canbe, 1)
                continue
            if idx == 0 :
                canbe = list(filter(lambda x : x != s[idx + 1], list("abc")))[0]
                s = s.replace("?", canbe, 1)
                continue
            if idx == l - 1 :
                canbe = list(filter(lambda x : x != s[idx - 1], list("abc")))[0]
                s = s.replace("?", canbe, 1)
        return s