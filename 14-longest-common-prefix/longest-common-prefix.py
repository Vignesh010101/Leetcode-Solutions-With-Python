class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=""
        vy=sorted(strs)
        first=vy[0]
        last=vy[-1]

        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return result
            result+=first[i]

        return result