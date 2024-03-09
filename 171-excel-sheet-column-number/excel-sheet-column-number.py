class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        for v in columnTitle:
            ans=ans*26+ord(v)-ord('@')
        return ans

