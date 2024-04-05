class Solution:
    def makeGood(self, s: str) -> str:
        stck=[]
        for c in s:
            if stck and abs(ord(c)-ord(stck[-1]))==32:
                stck.pop()
            else:
                stck.append(c)

        return ''.join(stck)