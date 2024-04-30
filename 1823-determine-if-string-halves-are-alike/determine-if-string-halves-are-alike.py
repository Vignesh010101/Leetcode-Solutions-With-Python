class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        lt, rt = 0, 0

        mid=len(s)//2
        
        for l,r in zip(s[:mid],s[mid:]):
            if l in vowels:
                lt+=1
            if r in vowels:
                rt+=1
        
        return lt==rt