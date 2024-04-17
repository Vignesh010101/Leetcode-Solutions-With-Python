class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        strr=""
        indice=list(indices)
        for i in range(len(s)):
            anj=indice.index(i)
            strr+=s[anj]

        return strr