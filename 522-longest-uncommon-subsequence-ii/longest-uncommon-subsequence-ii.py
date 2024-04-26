class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(a: str, b: str) -> bool:
            i = 0
            for char in b:
                if i < len(a) and a[i] == char:
                    i += 1
            return i == len(a)
        
        strs.sort(key=lambda s: -len(s))
        
        for i, s in enumerate(strs):
            if all(not isSubsequence(s, strs[j]) for j in range(len(strs)) if j != i):
                return len(s)
        
        return -1