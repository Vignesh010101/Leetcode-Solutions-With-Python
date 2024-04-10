class Solution:
    def removeDuplicates(self, s: str) -> str:
        stck=[]
        for char in s:
            if not stck or stck[-1]!=char:
                stck.append(char)
            else:
                stck.pop()
        
        return ''.join(stck)