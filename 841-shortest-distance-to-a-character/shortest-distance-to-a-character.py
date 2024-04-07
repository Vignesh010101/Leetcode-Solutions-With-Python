class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a=[]
        b=[]
        for i in range(len(s)):
            if s[i]==c:
                a.append(i)
        for i in range(len(s)):
            c=[]
            for j in a:
                c.append(abs(i-j))
            b.append(min(c))
        return b

        